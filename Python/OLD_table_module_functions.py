
"""
Updates all dependencies in every table that references this clone

dirTables is modified so that every dependent table will be modified with cloned values

WARNING: UNFINISHED
"""
def update_dependencies(dirTables, node, clone, LOG):
    try:
        nodeTable = dirTables[node.folder]
    except KeyError:
        LOG.write("Folder " + node.folder + " not found in dirTables.\n")
        return "FAIL: Node folder not found"
    LOG.write("Updating dependencies for " + node.folder + "/" + node.column + "\n")

    cloneval = clone.get_clone_val()
    baseval = clone.get_base_val()

    if cloneval == None:
        LOG.write("FAIL: Clone value invalid!\n")
        return "FAIL: Clone val invalid."
    LOG.write("Clone val: " + str(cloneval) + "\n")
    LOG.write("Base val: " + str(baseval) + "\n")

    # only update dependents if the node is a root
    if (node.type == "ROOT"):

        # for every dependent table
        for lnk in node.links:
            match = False
            lnk_node = lnk.get_other_node(node)
            lnk_node_table = dirTables[lnk_node.folder]["data__"]
            LOG.write("Processing link to " + lnk_node.folder + "/" +lnk_node.column + "\n" )

            # for every entry in that table
            for ek in lnk_node_table.entries.keys():
                entry = lnk_node_table.entries[ek]

                # if the entry holds a reference to the original entry...
                if entry[lnk_node.column] == baseval:
                    warning, ref_clone = lnk_node_table.make_clone(ek, lnk_node.column, cloneval) # clone that entry
                    LOG.write("\tMatch found for " + ek + '. \n\t\tCloning with EK: ' + ref_clone.entryKey + "\n")
                    if warning != "":
                        LOG.write("\t\t" + str(warning) + "\n")
                    match = True
            if match == False:
                LOG.write("\tNo matches found for this Link Node.\n")

    else:
        LOG.write("FAIL: Not root node!\n")
        return "FAIL: NOT ROOT NODE"



"""
A clone is an entry to a table which copies every value from another entry, but it
has it's own entry key, and possibly other edits.

WARNING: UNFINISHED
"""
class Clone:
    def __init__(self):
        self.entryKey = "Default" # has to actually be the value found in the table for key column
        self.base_entryKey = None # the entryKey for the base entry that this one is based on
        self.table = None # a pointer to the table object
        self.diff_column = None

    def __str__(self):
        return str(self.entryKey) + " ---> " + self.base_entryKey

    def get_clone_val(self):
        return self.table.entries[self.entryKey][self.diff_column]


    def get_base_val(self):
        return self.table.entries[self.base_entryKey][self.diff_column]




"""
Takes a tablediff object, which stores the changes between two tables, and yet another table object,
"mod table", which is the new table to apply these changes to.

The usage of this would be to send...
    1) tablediff(oldWarhammerTable, myOldModTable)
    2) table(newWarhammerTable)
Where the changes between newWarhammerTable and oldWarhammerTable DON'T concern us, but the changes between
oldWarhammerTable and myOldModTable should be applied to the newWarhammerTable, leaving all else in that
table the same.

THI IS TO BE USED AFTER A PATCH BY CA WHICH CHANGES MANY ASPECTS OF THE TABLE THAT YOU DON'T CARE ABOUT,
SO YOU JUST WANT TO RE-DO THE OLD CHANGES TO THE NEW BASE TABLE.

-- Currently this overrides patchtable object with new changes
"""
def apply_differences(tablediff, patchtable):
    ftype = ".csv"
    if(patchtable.separator != ","):
        ftype = ".tsv"

    for diff in tablediff.differences:
        try:
            entry = patchtable.entries[diff.entryKey]
            entry[diff.column] = diff.newValue
        # the key doesnt exist in the new base, ignore it
        except KeyError:
            sys.stderr.write(patchtable.name + " -\tMissing key in patch table: " + diff.entryKey + "\n")

    return patchtable


"""
Applies differences for one folder set (run once for each folder)

Writes the entire combined folder to the output directory
"""
def apply_diff_tree(baseTableFolder, modTableFolder, newBaseTableFolder):
    baseTable = concatTablesInFolder(baseTableFolder)
    modTable = concatTablesInFolder(modTableFolder)
    newTable = concatTablesInFolder(newBaseTableFolder)

    tablediff = TableDiff(baseTable, modTable) # detects differences between two tables

    if(len(tablediff.differences) == 0):
        sys.stderr.write("Not applying changes for file for: " + baseTable.name + " because there are no differences.\n")
        return None
    else:
        #print "Applying differences for " + newTable.name
        updated_table =apply_differences(tablediff, newTable)
        return updated_table



    """
    returns a clone object of the entry passed, does NOT try to update dependencies
    In other words, it just makes a copy of an entry and renames the entry key
    Uses a clone column to make the new entry, to support tables with more than one key column
    """
    def TABLE.make_clone(self, entryKey, cloneCol, cloneColValue):
        warning = ""
        if (False == (cloneCol in self.keyColumns)):
            warning = "WARNING: Clone Column is not a Key Column. "

        c = Clone()
        c.base_entryKey = entryKey
        c.table = self
        entry = copy.copy(self.entries[entryKey])
        entry[cloneCol] = cloneColValue
        cloneKey = self.get_entry_key(entry)
        if cloneKey == entryKey:
            cloneKey = entryKey + " <" + cloneColValue + ">"
            warning += "Clonekey is being set to " + cloneKey
        c.entryKey = cloneKey
        c.diff_column = cloneCol
        self.entries[cloneKey] = entry
        self.Added_EntryKeys |= {cloneKey}
        self.clones.append(c)

        return warning, c


"""
TODO: Dont do cloning at all? just find and replace?
"""
class Clone_Tree:
    def __init__(self):
        self.name = "Default"
        self.folder_to_clones = {} # maps a folder name to the clones belonging to this tree
        self.tables = set() # a set of tables that this clone tree touches

    def __str__(self):
        return self.name

"""
Creates one unit given its unit data, storing cloned entries in the modDirTables
unit data is a dict of info about the unit we are creating

WARNING: UNFINISHED
"""
def create_unit(unit_data, modDirTables, folder_to_nodes_dict, LOG):
    LOG.write("Creating unit " + unit_data.name + "\n")
    for folder in CREATE_UNIT_ROOT_FOLDERS:
        # load the table object from the directory
        curr_table = modDirTables[folder]["data__"]

        status, new_unit = curr_table.make_clone("wh_main_emp_inf_spearmen_0", "unit", unit_data.name)

        #TODO REPLACE THAT LINE ABOVE ^^^^ with correct parameters

        if status != "":
            LOG.write(status + "\n")

        # get all of the schema nodes corresponding to this folder
        curr_nodes = folder_to_nodes_dict[folder]
        root_found = False
        for node in curr_nodes:
            if node.type == "ROOT":
                if root_found == True:
                    LOG.write("WARNING: Two root nodes found for " +  folder + "\n")
                root_found == True
                result = update_dependencies(modDirTables, node, new_unit, LOG)
                LOG.write("RESULT: " + str(result) + "\n")








"""
finds all ROOT entries in every table with dependencies on this entry

node: the schema node holding the folder, column, and a set of other direct link nodes
value: the value in this folder at that column to find dependencies for.
dependency data: the current set of all dependencies in the strain, to be appended with new entries and returned
dirTables: a lookup for all the table objects, so that individual entries can be searched
"""
def find_dependencies(dirTables, node, value, dependency_data, LOG, depthStr):
    LOG.write(depthStr + "Finding dependencies for " + node.folder + "/" + node.column + " --> " + str(value) + "\n")

    # for every dependent table
    for lnk in node.links:
        lnk_node = lnk.get_other_node(node)
        lnk_node_table = dirTables[lnk_node.folder]["data__"]


            LOG.write(depthStr + "Processing link to " + lnk_node.folder + "/" + lnk_node.column + "\n" )
            found = False
            for lnk_ek in lnk_node_table.entries.keys():
                lnk_entry = lnk_node_table.entries[lnk_ek]
                if lnk_entry[lnk_node.column] == value:
                    found = True
                    dependency_data |= {(lnk_node.folder, lnk_node.column, lnk_ek, )}

                    dependency_data = find_dependencies(dirTables, lnk_node, "NULLSTRING", folders_checked, dependency_data, LOG, depthStr + "\t")

            #data_checked |= {lnk_node.folder}
            if (found == True):
                LOG.write(depthStr + "Found links.\n")

            else:
                LOG.write(depthStr + "No links found.\n")

    LOG.write(depthStr + "No more link nodes to check\n")

    return dependency_data



"""
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
    LOG.write("Linking: " + str(lnk) + "\n")
    """
