
"""
Loads every table in this directory.
returns a dict of folder name mapped to a list of tables loaded there.
"""
def load_directory_Tables(directory):
    db = os.path.join(directory, "db")
    folders = os.listdir(db)

    dir_tables = {}
    for f in folders:
        path = os.path.join(db,f)
        f_tables = load_folder_Tables(path)
        dir_tables[f] = f_tables

    return dir_tables


"""
returns a dict of column -> set(all possible values)
"""
def get_column_data(table):
    data = {}
    for c in table.columns:
        data[c] = set()

        for ek in table.entries.keys():
            val = table.entries[ek][c]
            data[c] |= {val}
    return data

"""
evaluates two column data sets to determine if they contain the same kind of data (assumedly)
"""
def eval_column_data(col_set_1, col_set_2):
    col_set_1 -= {""} # LEFT
    col_set_2 -= {""} # RIGHT
    # only check one out of the entire set!
    for d in col_set_1:
        if( is_number(d) == True):
            return "NUMBER_LEFT",0
        elif (is_bool(d)):
            return "BOOL_LEFT",0
        else:
            break
    # only check one out of the entire set!
    for d in col_set_2:
        if( is_number(d) == True):
            return "NUMBER_RIGHT",0
        elif (is_bool(d)):
            return "BOOL_RIGHT",0
        else:
            break

    shared = col_set_1 & col_set_2
    if ( len(shared) == 0):
        return "DIFFERENT", 0
    elif (len(shared) == len(col_set_1) ): #(col_set_1 == col_set):
        return "SAME", 1
    else:
        d_1not2 = col_set_1 - col_set_2
        d_2not1 = col_set_2 - col_set_1
        if ( len(d_1not2) == 0) and (len(shared) > 0):
            return "SUBSET_LEFT_OF_RIGHT", float(len(shared)) / len(col_set_1 | col_set_2)
        elif ( len(d_2not1) == 0) and (len(shared) > 0):
            return "SUBSET_RIGHT_OF_LEFT", float(len(shared)) / len(col_set_1 | col_set_2)
        else:
            return "OVERLAP", float(len(shared)) / len(col_set_1 | col_set_2)
    return "ERROR", 0

def is_bool(word):
    if (word.lower() == "false") or (word.lower() == "true"):
        return True
    else:
        return False

"""
Maps evankeys to columns, to expose schema links
"""
def mapSchema(table):
    tup_lst = dict()
    for ek in table.entries.keys():
        entry = table.entries[ek]

        for col in table.columns:
            coldata = entry[col]
            if "evankey" in coldata:
                col_lst = coldata.split("_")
                col_key = col_lst[1]
                # something like 14, unit to map the evankey_14 showing up in that column
                tup_lst[col] = int(col_key)
    return tup_lst

"""
represents a column of data in a table, and how it relates to others in the data tables
"""
class schema_node:
    def __init__(self):
        self.folder = "Default" # the folder name that this schema node represents (like land_units_tables)
        self.column = "Default" # the column name in that table which this schema node represents
        self.type = "Unknown" # MUST BE EITHER ROOT or REFERENCE
        self.links = set()

    def __str__(self):
        word = str(self.folder) + "/" + str(self.column) + "("+ self.type + ")\n"
        for l in self.links:
            if l.left_node == self:
                lnk_text = l.right_node.folder + "/" + l.right_node.column
            else:
                lnk_text = l.left_node.folder + "/" + l.left_node.column
            word += "\t" + lnk_text + "\n"
        return word

"""
A link between two schema nodes, describing the relationship between them
"""
class schema_node_link:
    def __init__(self):
        self.left_node = None
        self.right_node = None

        self.relationship = None # relationship left to right
        self.overlap_ratio = 0

    def __str__(self):
        return self.left_node.folder + "/" +self.left_node.column + "  -->  " + self.right_node.folder +  "/" +self.right_node.column

"""
Scans the schema from a very special pack.
This pack MUST be a cleaned version of an Assembly kit export where an entry from every table has been edited
to change it's string parameter to evankey_<number>, then updating all dependencies.
What this will do for all entries is specifically map a field from one table to the fields in the other tables.

Then, we take this mapping and detect how they are related. Is one a subset of the other? can there be duplicates?

This schema then gets saved in such a way as to be used by an error-checking script later.
"""
def schema_scan(baseDir, evanKeyDir, LOG):
    LOG.write( "STAGE: Loading data_pack directory\n")
    # Loads the data_pack directory tables
    root_dir = baseDir #"Exports/data_pack_1_23_18"
    dirTables = load_directory_Tables(root_dir)
    folder_to_ColumnData = {}
    folder_set = set(dirTables.keys())
    for folder in folder_set:
        tables = dirTables[folder]
        try:
            t = tables["data__"]
            coldata = get_column_data(t)
            folder_to_ColumnData[folder] = coldata # coldata is a dict of column -> all possible values (set)
        except:
            sys.stderr.write("WARNING: Error found for folder " + folder + "\n")

    LOG.write( "STAGE: Creating schema nodes"+ "\n")
    # prepare master schema
    evankey_dir = os.path.join(evanKeyDir,"db")
    folders = os.listdir(evankey_dir)

    master_schema =dict()
    folder_to_nodes_dict = {}
    for folder in folders:
        LOG.write( "-" * 100+ "\n")
        sys.stdout.write("Scanning folder: " + folder + "\n")
        try:
            baseTableFolder = os.path.join(evankey_dir,folder)
            baseTable = concatTablesInFolder(baseTableFolder)

            curr = mapSchema(baseTable) # returns a map of (column: key#) pairs for this folder
            for col in curr.keys():
                keynum = curr[col]
                nd = schema_node()
                nd.folder = folder
                nd.column = col
                nd.type = "REFERENCE"

                try:
                    folder_to_nodes_dict[nd.folder].append(nd)
                except:
                    folder_to_nodes_dict[nd.folder] = [nd]

                if len(baseTable.keyColumns) == 1:
                    if col == baseTable.keyColumns[0]:
                        nd.type = "ROOT"
                try:
                    master_schema[keynum].append( nd )
                except:
                    master_schema[keynum] = [nd]
                LOG.write( str(nd) + "\n")

        except:
            sys.stdout.write("FOLDER ERROR with folder " + folder + "\n")


    LOG.write( "STAGE: Linking nodes together"+ "\n")
    for i in master_schema.keys():
        link_set = master_schema[i]
        if len(link_set) > 0:

            proc_pairs = []
            for nd in link_set:
                for o_nd in link_set:
                    if nd == o_nd:
                        pass
                    else:
                        pair = {nd, o_nd}
                        if pair in proc_pairs:
                            pass
                        else:
                            lnk = schema_node_link()
                            lnk.left_node = nd
                            lnk.right_node = o_nd

                            left_col_set = folder_to_ColumnData[nd.folder][nd.column]
                            right_col_set = folder_to_ColumnData[o_nd.folder][o_nd.column]

                            res = eval_column_data(left_col_set, right_col_set)
                            lnk.relationship = res[0]
                            lnk.overlap_ratio = res[1]

                            # todo: relationships
                            nd.links |= {lnk}
                            o_nd.links |= {lnk}
                            proc_pairs.append(pair)
                            LOG.write("Linking: " + str(pair) + "\n")

    return folder_to_nodes_dict








# EOF
