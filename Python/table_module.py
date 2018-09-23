import sys
import warhammer2_table_config
import os
import copy
from difflib import SequenceMatcher

CREATE_UNIT_ROOT_FOLDERS = [
"main_units_tables",
"land_units_tables",
"variants_tables",
"melee_weapons_tables",
"missile_weapons_tables"
]


"""
A table obj holds a mapping of keys to values for each entry, and a set of entries
-- an entry is like a line in the table
-- each Key,value pair is a column name and the value at that column
-- entryKey will be a list of column names to use as key columns
"""
class Table:
    def __init__(self):
        self.entries = dict() # entries["wh_main_emp_inf_swordsmen"] -> {"key":"wh_main_emp_inf_swordsmen","meleeAttack":"32" ...}
        self.columns = [] # ["key", "meleeAttack", "meleeDefense", ...]
        self.separator = ","
        self.name = "Default" # FOLDER NAME! Sorry thats confusing
        self.lineTwo = "" # 34, for example saying there are 34 columns?
        self.keyColumns = [None] # a list of every column name that acts as part of the key
        #self.folder = ""
        self.newerKeyColumns = [None] # dict of key columns which were replaced
        self.BrokenCol_EntryKeys = set() # a set of all added entry keys that have column issues
        self.NewRemoved_EntryKeys = set() # a set of all entry keys that have been removed in the new data pack
        self.Collision_EntryKeys = set() # a set of all entry keys that have been edited by both the update and the mod
        self.Added_EntryKeys = set() # a set of all entry keys that were added in the mod
        self.Missing_EntryKeys = set() # a set of every entry key that belongs to an entry key that the data.pack has but the mod folder doesn't
        self.fileName = "Default"
        #self.clones = []

    def __str__(self):
        word = ""
        word += self.name + "\n"
        word += "Key Column(s): " + str(self.keyColumns) + "\n"
        word += stringify_list(self.columns, self.separator) + "\n"
        for ek in self.entries.keys():
            word += self.stringify_entry(ek) + "\n"
        return word

    def replace(self, column, baseval, repval):
        status = "No dependent entry values. "
        for ek in self.entries.keys():
            entry = self.entries[ek]
            if entry[column] == baseval:
                entry[column] = repval
                status = "Replaced dependent entry values."
        return status

    def get_column_data(self,column):
        data = []
        if column in self.columns:
            for ek in self.entries.keys():
                entry = self.entries[ek]
                data.append(entry[column])
        else:
            sys.stderr.write("Column " + column + " not found in Table's columns[]\n")
        return data

    def add_entry(self, entry):
        ek = self.get_entry_key( entry)
        self.entries[ek] = entry
        self.Added_EntryKeys |= {ek}

    # returns the entry key for a particular entry based off the table's entry key metadata
    def get_entry_key(self, entry, file_index=0):

        #print "Entry " + str(entry)
        ek = ""
        i = 1
        #print "Key columns " + str(self.keyColumns)
        FAILED_TO_FIND_KEYS = False
        for keyCol in self.keyColumns: # iterate through each entry key column, add the value of that column to the key string
            if keyCol == None:
                return "NULL_ENTRY_KEY"
            try:
                ek += entry[keyCol]
            except KeyError:
                FAILED_TO_FIND_KEYS = True
                break
            if i < len(self.keyColumns):
                ek += " TO "
                i +=1

        if FAILED_TO_FIND_KEYS == False:
            return ek
        else:
            ek = ""
            i=1
            for keyCol in self.newerKeyColumns:
                if keyCol == None:
                    return "NULL_ENTRY_KEY"
                try:
                    ek += entry[keyCol]
                except KeyError:
                    sys.stderr.write("Missing key for table " + self.name + "/" + self.fileName + "\n\t" + str(entry) + "\n")
                    return "default_key-" + str(file_index)
                if i < len(self.keyColumns):
                    ek += " TO "
                    i += 1
            return ek


    def get_file_extension(self):
        if self.separator == ",":
            return ".csv"
        elif self.separator == "\t":
            return ".tsv"
        else:
            sys.stderr.write("ERROR: Invalid separator!\n")
            return False

    def stringify_entry(self, entrykey):
        line = ""
        entry = self.entries[entrykey]
        j = 0
        for k in self.columns:
            j+=1
            line += entry[k]
            if j < len(self.columns):
                line += self.separator
        return line

    def get_fileprint_string(self,group=None):
        if group == None:
            group = self.entries.keys()
        word = ""
        word += self.name + "\n"
        word += self.lineTwo
        word += (stringify_list(self.columns, self.separator) + "\n")
        for ek in group:
            word += (self.stringify_entry(ek) + "\n")
        return word

    def print_to_file(self, directory):

        try:
            os.makedirs(directory)
        except:
            pass
        ftype = ".csv"
        if self.separator != ",":
            ftype = ".tsv"

        normal_keys = (set(self.entries.keys()) - self.BrokenCol_EntryKeys)
        normal_keys -= self.Collision_EntryKeys
        normal_keys -= self.NewRemoved_EntryKeys
        normal_keys -= self.Added_EntryKeys
        normal_keys -= self.Missing_EntryKeys

        # print broken columns to a file
        if len(self.BrokenCol_EntryKeys) > 0:
            fname = os.path.join(directory, self.fileName + "_BROKEN-COLUMNS" + ftype)
            f = open(fname,"w")
            f.write(self.get_fileprint_string(self.BrokenCol_EntryKeys))
        # print collision to a file
        if len(self.Collision_EntryKeys) > 0:
            fname = os.path.join(directory, self.fileName + "_COLLISION" + ftype)
            f = open(fname,"w")
            f.write(self.get_fileprint_string(self.Collision_EntryKeys))
        # print removed entries to a file
        if len(self.NewRemoved_EntryKeys) > 0:
            fname = os.path.join(directory, self.fileName + "_REMOVED" + ftype)
            f = open(fname,"w")
            f.write(self.get_fileprint_string(self.NewRemoved_EntryKeys))
        # print removed entries to a file
        if len(self.Added_EntryKeys) > 0:
            fname = os.path.join(directory, self.fileName + "_ADDED" + ftype)
            f = open(fname,"w")
            f.write(self.get_fileprint_string(self.Added_EntryKeys))
        # print removed entries to a file
        if len(self.Missing_EntryKeys) > 0:
            fname = os.path.join(directory, self.fileName + "_MISSING" + ftype)
            f = open(fname,"w")
            f.write(self.get_fileprint_string(self.Missing_EntryKeys))

        fname = os.path.join(directory, self.fileName + ftype)

        f = open(fname,"w")
        f.write(self.get_fileprint_string(normal_keys))
        return 0


    def __len__(self):
        return len(self.entries)
"""
Contains a single difference, which is a column name, old val, and new val
"""
class Diff:
    def __init__(self, key, col, old, new):
        self.entryKey = key
        self.column = col
        self.oldValue = old
        self.newValue = new

    def __str__(self):
        return self.entryKey + "[" + self.column + "] <-- " + self.newValue + " (" + self.oldValue + ")"

    def to_tsv(self):
        return self.entryKey + "\t" + self.column + "\t" + self.oldValue + "\t" + self.newValue

"""
TableDiff stores the full set of all differences between two files (statically)
Must be updated if the table objects change
Takes two Table objects and detects all differences.
"""
class TableDiff:
    def __init__(self, told, tnew):
        self.oldTable = told
        self.newTable = tnew
        # differences has
        # entry-key --> column --> (old val, new val)
        self.differences = set()
        self.compare_tables() # run compare tables on itself to update differences

    def compare_tables(self):
        diff = None
        if self.oldTable == None and self.newTable == None:
            diff = Diff("ENTIRE TABLE","ENTIRE TABLE","MISSING","MISSING")
            self.differences |= {diff}
            return
        elif self.newTable == None:
            diff = Diff("ENTIRE TABLE","ENTIRE TABLE","NOT MISSING","MISSING")
            self.differences |= {diff}
            return
        elif self.oldTable == None:
            diff = Diff("ENTIRE TABLE","ENTIRE TABLE","MISSING","NOT MISSING")
            self.differences |= {diff}
            return

        entryKeySet = set(self.oldTable.entries.keys()) | set(self.newTable.entries.keys())

        if self.oldTable.name != self.newTable.name:
            sys.stderr.write("Tables have different names! \n")
            return False

        elif self.oldTable.columns != self.newTable.columns:
            sys.stderr.write("Tables have different columns names! \n")
            for c in self.oldTable.columns:
                if c in self.newTable.columns:
                    pass
                else:
                    sys.stderr.write(self.newTable.name + " (new) is missing " + c + "\n")
            for c in self.newTable.columns:
                if c in self.oldTable.columns:
                    pass
                else:
                    sys.stderr.write(self.oldTable.name + " (old) is missing " + c + "\n")

        # even if columns are different, continue
        for entryKey in entryKeySet:
            oldEntry = None
            newEntry = None
            try:
                oldEntry = self.oldTable.entries[entryKey]
            except KeyError as e:
                try:
                    newEntry = self.newTable.entries[entryKey]
                    diff = Diff(entryKey, "ENTIRE_ENTRY", "MISSING", str(newEntry))
                    self.differences |= {diff}
                except KeyError as e:
                    sys.stderr.write("ERROR processing entry with key " + entryKey + "\n")

            try:
                newEntry = self.newTable.entries[entryKey]
            except KeyError as e:
                try:
                    oldEntry = self.newTable.entries[entryKey]
                    diff = Diff(entryKey, "ENTIRE_ENTRY", str(oldEntry), "MISSING")
                    self.differences |= {diff}
                except KeyError as e:
                    sys.stderr.write("ERROR processing entry with key " + entryKey + "\n")

            if oldEntry != None and newEntry != None:
                for col in self.oldTable.columns: #TODO dont just iterate through oldTable

                    oldv = oldEntry[col]
                    try:
                        newv = newEntry[col]
                    except KeyError as e:
                        newv = "MISSING"
                    if oldv != newv:
                        diff = Diff(entryKey, col, oldv, newv)
                        self.differences = self.differences | {diff}

    def __str__(self):
        word = ""
        for diff in self.differences:
            word += str(diff) + "\n"
        return word

    def to_tsv(self):
        word = "Entry\tColumn\tOld Value\tNew Value\n"
        for diff in self.differences:
            word += diff.to_tsv() + "\n"
        return word



"""
Takes in list of strings, returns a line with strings separated by a "sep" character
"""
def stringify_list(lst, sep):
    line = ""
    j = 0
    for i in lst:
        j+=1
        line += i
        if j < len(lst):
            line += sep
    return line

"""
Takes in string line and separator character
returns lst of items
"""
def parse_line_to_list(line, sep="\t"):
    lst = []
    word = ""
    for i in line:
        if (i == sep) | (i == "\n") | (i == "\r"):
            lst.append(word)
            word = ""
        else:
            word += i
    if word != "":
        lst.append(word)
    return lst

"""
Takes in a CSV/TSV File, stores the results to a table object.
-- needs first column to be entry-names
-- assumes 3rd line is column-keys, and 4+ lines are all data (no blanks at the end)
-- assumes .tsv means will be tab separated, else comma separated
"""
def file_loader(csvFile,renamed_columns={}):
    table = Table()
    old_to_new_renamed = {}
    for a in renamed_columns.keys():
        r = renamed_columns[a]
        old_to_new_renamed[r] = a

    if (csvFile.name[-4:] != ".tsv") and (csvFile.name[-4:] != ".csv"):
        sys.stderr.write("Invalid file: " + csvFile.name + "\n")
        return None

    if ".tsv" in csvFile.name:
        table.separator = "\t"

    table.fileName = os.path.basename(csvFile.name)[0:-4]

    i = 0

    for line in csvFile:
        entry = dict()
        lst = []
        if i == 0:
            lst = parse_line_to_list(line, table.separator)
            if len(lst) > 0:
                table.name = lst[0]
                try:
                    table.keyColumns = warhammer2_table_config.keyDict[table.name] # reference config library
                    table.newerKeyColumns = warhammer2_table_config.NEW_SCHEMA_keyDict[table.name]

                except KeyError as e:
                    sys.stderr.write("Key Columns not found for table: " + table.name + " in WH2 config file\n")
                    return None
            else:
                sys.stderr.write("Empty first line in file: " + csvFile.name + "\n")

        elif i == 1:
            table.lineTwo = line
        elif i == 2:
            tmp_lst = parse_line_to_list(line, table.separator)
            res_columns = []
            for c in tmp_lst:
                if c in old_to_new_renamed.keys():
                    res_columns.append(old_to_new_renamed[c])
                else:
                    res_columns.append(c)

            table.columns = res_columns
            if table.keyColumns[0] == None:
                # TODO: RE-ENABLE THIS sys.stderr.write("WARNING: Table " + table.name + " has an unspecified key column list in Warhammer2_table_config!\n")
                table.keyColumns = table.columns
        else:
            lst = parse_line_to_list(line, table.separator)
            if len(lst) == len(table.columns):
                j = 0
                for col in table.columns:
                    # if this is a renamed column!
                    if col in old_to_new_renamed.keys():
                        col = old_to_new_renamed[col]
                    entry[col] = lst[j]
                    j += 1

                entry_key = table.get_entry_key(entry,i) # contains a dict of col_name: value pairs
                table.entries[entry_key] = entry
            else:
                sys.stderr.write("Mismatched entry: " + line + "\n")
        i += 1
    # print "Adding file: " + csvFile.name + " for " + table.name

    return table



"""
Used to merge two table objects together, which were loaded from different files, and
should allow entries from second table to override entries in the first table.
Returns the base table object which stores both sets of information concatenated together.
"""
def merge_tables(bot_table, top_table):
    if bot_table == None:
        return None
    elif top_table == None:
        return bot_table

    if bot_table.name != top_table.name:
        sys.stderr.write("Merging tables " + bot_table.name + " have different names!\n")
        return None
    elif bot_table.columns != top_table.columns:
        sys.stderr.write("Merging tables have " + bot_table.name + " different columns names!\n")
        return None
    else:
        for entryKey in top_table.entries.keys():
            bot_table.entries[entryKey] = top_table.entries[entryKey]
    return bot_table


"""
Looks for every tsv/csv file in a folder, runs file loader on them, and adds then runs
the merge table command to merge them into one table object
"""
def concatTablesInFolder(folder,renamed_columns={}):
    lst = os.listdir(folder)
    lstTSV = []
    # remove non tsv/csv files
    for l in lst:
        if (".tsv" in l) or (".csv" in l):
            lstTSV.append(l)

    # sort the way the launcher loads, where alphanumerically lower names supercede higher names
    lst = sorted(lstTSV, key=str.lower, reverse=True)

    i = 0
    baseTable = None
    for tsvFile in lst:
        tmpFile = open(folder + "\\" + lst[i], 'r')
        if i == 0:
            baseTable = file_loader(tmpFile,renamed_columns)
            if baseTable == None:
                return None
        else:
            tmpTable = file_loader(tmpFile,renamed_columns)
            baseTable = merge_tables(baseTable,tmpTable)
        i += 1
    if baseTable == None:
        return None
    baseTable.fileName += "_CONCAT"
    return baseTable


"""
Loads all tables in this folder, returns a map of table file's name to its table objects
"""
def load_folder_Tables(folder,renamed_columns={}):
    lst = os.listdir(folder)
    lstTSV = []
    # remove non tsv/csv files
    for l in lst:
        if (".tsv" in l) or (".csv" in l):
            lstTSV.append(l)

    # sort the way the launcher loads, where alphanumerically lower names supercede higher names
    lst = sorted(lstTSV, key=str.lower, reverse=True)

    baseTableMap = dict()
    for tsvFile in lst:
        tmpFile = open(folder + "\\" + tsvFile, 'r')
        baseTable = file_loader(tmpFile,renamed_columns)
        baseTableMap[tsvFile.split(".")[0]] = baseTable
    return baseTableMap


"""
returns a set of differences if the entry exists in both tables and has been edited

Warning: All removed columns will have a null value
"""
def get_entry_diff(ek, basetable, modtable):
    differences = set()
    baseentry = basetable.entries[ek]
    modentry = modtable.entries[ek]

    for col in basetable.columns:
        baseval = baseentry[col]
        try:
            modval = modentry[col]
        except KeyError:
            modval = "NULL"

        if baseval != modval:
            diff = Diff(ek, col, baseval, modval)
            differences |= {diff}
    return differences


"""
Tests if a string could be cast as a number
"""
def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

"""
rebases a table object onto another table object

if overwrite = true then the rebase will not add any entries that were deleted in the mod table
also, if overwrite = false, then the rebase will remove any entire etnries that are not edited in mod table

OVERWRITES MOD TABLE AND RETURNS IT EDITED
"""
def rebase_table(oldTable, modTable, newTable, LOG, overwrite=False, added_columns=[], removed_columns=[], verbose=False):
    ot_entries = set(oldTable.entries.keys())
    mt_entries = set(modTable.entries.keys())
    nt_entries = set(newTable.entries.keys())

    possible_edits = ot_entries & mt_entries # used to re-perform edits
    added_entries = mt_entries - ot_entries # if entries are added AND anything was renamed or columns were added...
    mod_removed_entries = ot_entries - mt_entries # should remain removed...
    new_removed_entries = ot_entries - nt_entries # used to check for errors
    new_entries = nt_entries - ot_entries # entries added in newTable
    missing_entries = (ot_entries - mt_entries) & nt_entries

    # TODO: default to writing these files?
    # TODO: If columns are broken, don't process added entries like this...
    modTable.Added_EntryKeys |= added_entries
    modTable.Missing_EntryKeys |= missing_entries

    if len(mod_removed_entries) > 0:
        for mre in mod_removed_entries:
            if (verbose == True) and (overwrite == True):
                LOG.write("The Mod removed " + mre + " and it will remain removed in the new TSV file.\n")

    if len(missing_entries) > 0:
        for me in missing_entries:
            modTable.entries[me] = copy.copy(newTable.entries[me])

    columns_changed = (len(added_columns) > 0) or (len(removed_columns) > 0)

    # TODO: will this handle the situation where we edited an entry that was removed (or renamed
    # TODO: DO SOMETHING ABOUT WHEN AN ENTRY WAS RENAMED? OR IF ITS REFERENCE WAS?
    if (len(new_removed_entries) > 0) and (overwrite == True or (len(new_removed_entries & mt_entries) > 0)):
        LOG.write("WARNING: This folder contains Newly removed entries! Newly removed entries will be placed in the '..._REMOVED' tsv file\n")


    # must KEEP every entry found in Mod table not found in old base table (since it got added)
    # When supporting certain situations (like column changes), added entries will cause errors
    if columns_changed:
        modTable.columns = copy.copy(newTable.columns) # reset the columns...
        if len(added_entries) > 0:
            LOG.write("WARNING: This folder contains added entries when a table's columns were changed! These entries will be placed in the '..._BROKEN_COLUMNS' tsv file\n")
        for ek in added_entries:
            modTable.BrokenCol_EntryKeys |= {ek}
            entry = modTable.entries[ek]
            for a_col in added_columns:
                entry[a_col] = "MISSING"
    else:
         pass #: they already exist in mod_table...

    # Must add every new entry in newTable
    if overwrite == True:
        for ek in new_entries:
            modTable.entries[ek] = copy.copy(newTable.entries[ek])
            if verbose == True:
                LOG.write("Added entry from new data.pack: " + ek + "\n")

    # apply changes to all edited entries to the new table's version of that entry
    for ek in possible_edits:
        differences = get_entry_diff(ek, oldTable, modTable)
        update_map = dict() # maps column edited to the diff
        removed = False
        # revert the entry to the newTable's version
        try:
            modTable.entries[ek] = copy.copy(newTable.entries[ek]) # revert it to the new entry

        except KeyError:
            LOG.write("WARNING " + ek + " was removed from the new data.pack \n")
            modTable.NewRemoved_EntryKeys |= {ek}
            removed = True

        if removed == False:
            updates = get_entry_diff(ek, oldTable, newTable)
            for u in updates:
                update_map[u.column] = u

        if len(differences) > 0:
            if verbose == True:
                LOG.write("\tRebasing: " + ek + "\n")

            entry = modTable.entries[ek]
            # leave unedited lines in the mod table
            for df in differences:
                change_string = not (is_number(df.newValue))
                try:
                    update_diff = update_map[df.column]
                except KeyError:
                    update_diff = None

                # update collisions when a collision was detected
                if update_diff != None: #and change_string == True:

                    if verbose == True:
                        LOG.write("\t-\tWARNING: Collision at " + str(df.column) + "\n\t\t*\t-> mod val: " + df.newValue + ". new val: " + update_diff.newValue + ". old val: " + df.oldValue + "\n")
                    if change_string == True:
                        modTable.Collision_EntryKeys |= {ek}
                        LOG.write("\t\t*\tCollision entry will ONLY be included in Collision TSV file\n")
                    else:
                        LOG.write("\t\t*\tCollision entry will be assumed safe and remain in standard TSV file\n")
                else:
                    if verbose == True:
                        LOG.write("\t-\t" + str(df) + "\n")
                entry[df.column] = df.newValue

            # Now the entry has only the pack's changed things edited

    LOG.flush()
    return modTable



"""
Runs a diff for the single table (ex. "main_units_tables") folder, to generate diff of
mod table against base table.
"""
def run_diff(baseTableFolder, modTableFolder):
    baseTable = concatTablesInFolder(baseTableFolder)
    modTable = concatTablesInFolder(modTableFolder)

    tablediff = TableDiff(baseTable, modTable) # detects differences between two tables

    if len(tablediff.differences) == 0:
        sys.stderr.write("Not writing diff file for: " + baseTable.name + " because there are no differences.\n")
    else:
        if modTable == None or baseTable == None:
            diff_file = open("Results\\ERR_" + baseTableFolder.split("\\")[-1] + "_CHANGES.tsv","w")
        else:
            diff_file = open("Results\\" + modTable.name + "_CHANGES.tsv","w")
        diff_file.write("Changes between " + baseTableFolder + " (base) and " + modTableFolder + " (mod)\n")
        diff_file.write(tablediff.to_tsv() + "\n")





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
        if is_number(d) == True:
            return "NUMBER_LEFT",0
        elif is_bool(d):
            return "BOOL_LEFT",0
        else:
            break
    # only check one out of the entire set!
    for d in col_set_2:
        if is_number(d) == True:
            return "NUMBER_RIGHT",0
        elif is_bool(d):
            return "BOOL_RIGHT",0
        else:
            break

    shared = col_set_1 & col_set_2
    if len(shared) == 0:
        return "DIFFERENT", 0
    elif len(shared) == len(col_set_1): #(col_set_1 == col_set):
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
        #self.links = set() # schema node links where one link is this node (a DIRECT link)
        self.direct_links = set() # a set of nodes directly linked to this node
        self.indirect_links = set() # a set of all nodes in the same table as this node


    def __str__(self):
        word = "\'" + str(self.folder) + "/" + str(self.column) + "\'" + " ("+ self.type + ")"
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

    def get_other_node(self, node):
        if node == self.left_node:
            return self.right_node
        elif node == self.right_node:
            return self.left_node
        else:
            return None

"""
Scans the schema from a very special pack.
This pack MUST be a cleaned version of an Assembly kit export where an entry from every table has been edited
to change it's string parameter to evankey_<number>, then updating all dependencies.
What this will do for all entries is specifically map a field from one table to the fields in the other tables.

Then, we take this mapping and detect how they are related. Is one a subset of the other? can there be duplicates?

This schema then gets saved in such a way as to be used by an error-checking script later.
"""
def schema_scan(dirTables, evankey_dir, LOG):
    LOG.write( "STAGE: Loading data_pack directory\n")
    # Loads the data_pack directory tables

    folder_to_ColumnData = {}
    folder_set = set(dirTables.keys())
    for folder in folder_set:
        tables = dirTables[folder]
        try:
            t = tables["data__"]
            coldata = get_column_data(t)
            folder_to_ColumnData[folder] = coldata # coldata is a dict of column -> all possible values (set)
        except:
            LOG.write("WARNING: Error found for folder " + folder + "\n")

    LOG.write( "STAGE: Creating schema nodes"+ "\n")
    # prepare master schema
    folders = os.listdir(evankey_dir)

    master_schema =dict()
    folder_to_nodes_dict = {}
    all_nodes = []
    for folder in folders:
        LOG.write( "-" * 100+ "\n")
        LOG.write("Scanning folder: " + folder + "\n")
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
                all_nodes.append(nd)

        except:
            sys.stdout.write("FOLDER ERROR with folder " + folder + "\n")


    LOG.write( "STAGE: Linking nodes together"+ "\n")
    for i in master_schema.keys():
        link_set = master_schema[i]
        if len(link_set) > 0:
            LOG.write("-"*100 + "\nScanning link set:\n")
            proc_pairs = []
            for nd in link_set:
                LOG.write("\t- " + str(nd) + "\n")

                for o_nd in link_set:
                    if nd == o_nd:
                        pass
                    else:
                        nd.direct_links |= {o_nd}
                        # old code went here

            # deal with having too many root nodes
            # assumes node whose folder is shortest is root... its often correct

            shortest_node = None
            for nd in link_set:
                if nd.type == "ROOT":
                    if shortest_node == None:
                        LOG.write("Setting shortest node: " + str(nd) +"\n")
                        shortest_node = nd
                    else:
                        nd_length = len(nd.folder)

                        if nd_length < len(shortest_node.folder):
                            shortest_node.type = "REFERENCE"
                            shortest_node = nd
                            LOG.write("Resetting shortest node: " + str(nd) +"\n")
                        else:
                            nd.type = "REFERENCE"
                            LOG.write("Setting node to reference: " + str(nd) +"\n")

            found = False
            for nd in link_set:
                if nd.type == "ROOT":
                    if found == True:
                        sys.stderr.write("FAILED TO IDENTIFY UNIQUE ROOT FOR NODE: " + str(nd) + "\n")
                    else:
                        found = True
            LOG.write("* Final root node: " + str(shortest_node) + "\n")



    for nd in all_nodes:
        nd.indirect_links = set(folder_to_nodes_dict[nd.folder]) - {nd}

    return folder_to_nodes_dict



"""
returns a table which only contains the entries that differ between the
modTable and the baseTable.
Essentially it deletes out anything that hasn't been edited from the
modTable
"""
def unique_table(baseTable, modTable, LOG):

    if baseTable == None or modTable == None:
        return None
    if baseTable.name != modTable.name:
        return None
    table = copy.deepcopy(modTable)

    joint_eks = set(modTable.entries.keys()) & set(baseTable.entries.keys())
    for jek in joint_eks:
        try:
            baseEntry = baseTable.entries[jek]
            modEntry = modTable.entries[jek]
            if modEntry == baseEntry:
                del table.entries[jek]
                #LOG.write("Deleting Joint Entry Key: " + jek + "\n")
            else:
                LOG.write("Keeping Joint Entry Key: " + jek + "\n")
        except:
            LOG.write("ERROR for Entry Key: " + jek + "\n")

    # TODO: if plausible, this doesn't remove these EKs from being in the sets of broken columns or other
    # Entry key related lists
    return table




"""
takes a modified dirTables array object and compares against base, minimizing all common entries
by running unique_table
"""
def print_unique_tables(baseDirTables, modDirTables, LOG, outputDir):
    for folder in modDirTables.keys():
        modTables = modDirTables[folder]
        baseTables = baseDirTables[folder]
        jointKeys = set(modTables.keys()) & set(baseTables.keys())
        for tk in jointKeys:
            modTable = modTables[tk]
            baseTable = baseTables[tk]
            newTable = unique_table(baseTable, modTable, LOG)
            if newTable == None:
                LOG.write("FAILED to write table " + folder + "/" + tk + "\n" )
            else:
                if len(newTable.entries.keys()) > 0:

                    fpath = os.path.join(outputDir,folder)
                    try:
                        os.makedirs(fpath)
                    except:
                        pass
                    LOG.write("Writing unique table for " + folder + "/" + tk + "\n")
                    newTable.print_to_file(fpath)
                else:
                    LOG.write("Skipping write to " + folder + "/" + tk + "\n")


"""
finds specific data in specific tables, replaces it, and updates all dependencies depending on
the schema link nodes

replaceData is a 2D list of format
[
[ folder name,   column name,     base value,     new value],
[...],
...
]
"""
def replace_data(replaceData, dirTables, folder_to_nodes_dict, LOG):
    for repList in replaceData:
        folder = repList[0]
        column = repList[1]
        baseVal = repList[2]
        repVal = repList[3]

        mainTable = dirTables[folder]["data__"]
        LOG.write("#" * 90 + "\n")
        LOG.write("REPLACING " + folder + "/" + column + ": " + baseVal + " --> " + repVal + "\n")
        result = mainTable.replace(column, baseVal, repVal)
        LOG.write("RESULT: " + str(result) + "\n")
        try:
            nodes = folder_to_nodes_dict[folder]
        except KeyError:
            LOG.write("ERROR: Couldn't find folder " + folder + " in folder_to_nodes_dict.\n")
            sys.stderr.write("ERROR: Couldn't find folder " + folder + " in folder_to_nodes_dict.\n")
            nodes = []
        root_found = False
        for node in nodes:
            if node.type == "ROOT":
                if root_found == True:
                    LOG.write("WARNING: Two root nodes found for " +  folder + "\n")

                up_res = update_replaced_dependencies(dirTables, node, baseVal, repVal, LOG)
                if up_res != None:
                    LOG.write("RESULT: " + str(up_res) +"\n")
                root_found == True





"""
Updates all dependencies for a renamed entry.
"""
def update_replaced_dependencies(dirTables, node, baseval, repval, LOG):
    try:
        nodeTable = dirTables[node.folder]["data__"]
    except KeyError:
        LOG.write("Folder " + node.folder + " not found in dirTables.\n")
        return "FAIL: Node folder not found"
    LOG.write("Updating dependencies for " + node.folder + "/" + node.column + "\n")

    LOG.write("Replaced val: " + str(repval) + "\n")
    LOG.write("Base val: " + str(baseval) + "\n")

    # only update dependents if the node is a root
    if node.type == "ROOT":

        # for every dependent table
        for lnk_node in node.direct_links:
            lnk_node_table = dirTables[lnk_node.folder]["data__"]
            LOG.write("Processing link to " + lnk_node.folder + "/" +lnk_node.column + "\n" )
            result = lnk_node_table.replace(lnk_node.column, baseval, repval) # replace all references
            LOG.write("\t\t" + str(result) + "\n")

    else:
        LOG.write("FAIL: Not root node!\n")
        return "FAIL: NOT ROOT NODE"


"""
Finds every direct link to a folder/column/value path.

We go to the table, and for every entryKey[column] == value match, thats an entry to check

The direct links are just in the node's links.
"""
def find_direct_links(dirTables, node, value, LOG, depthStr = ""):
    data = []
    for lnk_node in node.direct_links:
        lnk_node_table = dirTables[lnk_node.folder]["data__"]
        LOG.write(depthStr + "Direct Link: " + lnk_node.folder + "/" + lnk_node.column + "\n" )

        for lnk_ek in lnk_node_table.entries.keys():
            lnk_entry = lnk_node_table.entries[lnk_ek]

            # if this entry's contains a reference to the root node
            if lnk_entry[lnk_node.column] == value:
                data.append((lnk_node, lnk_ek)) # the node and entry key that match

    return data


"""
Finds every indirect link in a set of entries.

An indirect link is a reverse look up to see where the reference comes from
"""
def find_indirect_links(dirTables, folder_to_nodes_dict, folder, entries, LOG, depthStr = ""):
    data = []
    nodes = folder_to_nodes_dict[folder]
    table = dirTables[folder]["data__"]

    for node in nodes:
        if node.type != "ROOT":
            column = node.column

            values = set()
            for ek in entries:
                entry = table.entries[ek]
                value = entry[column]
                values |= {value}
            # don't do the same value twice
            for value in values:
                LOG.write("Indirect Link: " + folder + "/" + column + " --> " + value + "\n")
                curr_data = find_direct_links(dirTables, node, value, LOG)
                data.append( (node, value, curr_data) )
    return data



"""
Prints the full node web
"""
def print_node_web(folder_to_nodes_dict):
    for folder in folder_to_nodes_dict.keys():
        nodes = folder_to_nodes_dict[folder]
        print("#" * 100)
        print(folder)
        for node in nodes:
            print("-" * 50)
            print("\t" + str(node))
            print("\tDIRECT = [")
            for lnk_node in node.direct_links:
                print("\t\t" + str(lnk_node))
            print("\t]\n\tINDIRECT = {")
            for lnk_node in node.indirect_links:
                print("\t\t" + str(lnk_node))
            print("\t}")


"""
Looks at a table's column data and determines which entry keys match the value
"""
def find_connections(dirTables, node, value):
    nodeTable = dirTables[node.folder]["data__"]
    matching_entries = set()
    for ek in nodeTable.entries.keys():
        entry = nodeTable.entries[ek]
        ek_value = entry[node.column]
        if value == ek_value:
            matching_entries |= {ek}
    return matching_entries


"""
Recrusively finds data links to a folder/column/value path. Direct links are other places that look
up this reference, and indirect links are other references made by entries that hold the root reference

For example, looking up a main units/unit value would search for (direct) references to this main_unit value,
but also look up the other references in the main_unit table like land_unit.
"""
def find_data_links(dirTables, node, value, LOG, processedNodes, depth = "", maxIndirectDepth=8, do_direct = True):
    matching_entries = find_connections(dirTables, node, value)
    nodeTable = dirTables[node.folder]["data__"]
    if (len(matching_entries) == 0) or (value == ""):
        #LOG.write(depth + "- End of reference chain }\n")
        return set()
    LOG.write(depth + "NODE: " + str(node) + " - \'" + value + "\' {\n")
    for m in matching_entries:
        LOG.write(depth + "\tMatch: \'" + m + "\'\n")

    directres = dict()
    indirectres = dict()
    processedNodes |= {node} # this keeps it from running infinitely
    depth += "\t"

    # TODO: Direct links need to be Breadth first
    if do_direct:
        LOG.write(depth + "DIRECT: {\n")

        # DIFFERENT TABLE, SAME VALUE
        # looking for any time someone references this value
        for lnk_node in node.direct_links:
            if lnk_node not in processedNodes:
                res = find_data_links(dirTables, lnk_node, value, LOG, processedNodes, depth + "\t", maxIndirectDepth, False)
                directres[lnk_node] = res
        LOG.write(depth +"}\n")


    LOG.write(depth + "INDIRECT: {\n")
    intdepth = len(depth)
    # SAME TABLE, DIFFERENT VALUE
    # looking all other references that these entries make
    for lnk_node in node.indirect_links:
        if lnk_node not in processedNodes:
            if intdepth <= maxIndirectDepth:
                if (intdepth == 0) or (lnk_node.type != "ROOT"):
                    values = set()
                    for m in matching_entries:
                        values |= {nodeTable.entries[m][lnk_node.column]}

                    indirectres[lnk_node] = dict()
                    for v in values:
                        res = find_data_links(dirTables, lnk_node, v, LOG, processedNodes, depth + "\t", maxIndirectDepth)
                        indirectres[lnk_node][v] = res
                else:
                    LOG.write(depth + "Skipping deep root node " + str(lnk_node) + "\n")
            else:
                LOG.write(depth + "Skipping " + str(lnk_node) + " due to max indirect depth\n")
    LOG.write(depth +"}\n")
    depth = depth[0:-1]
    LOG.write(depth +"}\n")
    return matching_entries, directres, indirectres



"""
Merges every entry in modDirTables into baseDirTables and returns the result
overwrites baseDirTables
"""
def merge_dirTables(baseDirTables, modDirTables, LOG):
    try:
        for folder in modDirTables.keys():
            tables = modDirTables[folder]
            for tk in tables.keys():
                table = tables[tk]
                try:
                    LOG.write("f: " + str(folder) + "\n")
                    LOG.write("tk: " + str(tk) + "\n")
                    b_table = baseDirTables[folder][tk]
                    b_table = merge_tables(b_table, table)
                except KeyError:
                    LOG.write("KEYERROR for " + folder + "\n")
                    baseDirTables[folder][tk] = table
        return baseDirTables
    except KeyError:
        LOG.write("FAILED to get merged dir tables.\n")
        return None



"""
gets a unique dir tables dictionary
overwrites modDirTables
"""
def unique_dirTables(baseDirTables, modDirTables, LOG):
    try:
        for folder in modDirTables.keys():
            m_tables = modDirTables[folder]
            for tk in m_tables.keys():
                m_table = m_tables[tk]
                b_table = baseDirTables[folder][tk]
                m_table = unique_table(b_table, m_table, LOG)
        return modDirTables
    except KeyError:
        LOG.write("FAILED to get unique dir tables.\n ")
        return None




"""
DETECT RENAMED COLUMNS FUNCTIONS:
"""
def similar(a, b):
    res = SequenceMatcher(None, a, b).ratio()
    print("Similarity: " + a + " - " + b + " = " + str(res))
    return res

def column_equivalence(col1,col2):
    s1 = set(col1)
    s2 = set(col2)
    join = s1 & s2

    c1_eq = len(join) / float(len(col1))
    c2_eq = len(join) / float(len(col2))

    if len(join) == 0:
        pass #print("No Equivalency")
    else:
        pass
        #print("C1 equivalency " + str(c1_eq))
        #print("C2 equivalency " + str(c2_eq))
    return (c1_eq, c2_eq)


"""
Will return a dict defining mappings of old columns to new names
"""
def find_renamed_columns(old_table, new_table):
    basetable_columns = set(old_table.columns)
    newtable_columns = set(new_table.columns)
    added_columns = newtable_columns - basetable_columns
    removed_columns = basetable_columns - newtable_columns

    mapping_new_to_old = {}

    for a in added_columns:
        num_matches = 0
        for r in removed_columns:
            name_matching = similar(a,r)
            if name_matching > 0.8:
                num_matches += 1
                mapping_new_to_old[a] = r
            else:
                #print("Evaluating equivalency between " + a + " and " + r)
                a_data = new_table.get_column_data(a)
                r_data = old_table.get_column_data(r)
                (c1_eq, c2_eq) = column_equivalence(a_data, r_data)

                if c1_eq >= 0.5 and c2_eq >= 0.5:
                    #print("Match found " + a + ":" +r)
                    num_matches += 1
                    mapping_new_to_old[a] = r
        if num_matches > 1:
            #print("Warning! More than one match found for new column " + a)
            del mapping_new_to_old[a]
        elif num_matches == 0:
            pass #print("Warning! No match found for column " + a)
    return mapping_new_to_old


def detect_renamed_columns(oldBaseDir, newBaseDir, LOG):
    oldBaseLst = os.listdir(oldBaseDir)
    newBaseLst = os.listdir(newBaseDir)

    newFolderSet = set(newBaseLst)
    baseFolderSet = set(oldBaseLst)

    newNotOld = newFolderSet - baseFolderSet
    oldNotNew = baseFolderSet - newFolderSet

    allDirs = baseFolderSet & newFolderSet

    if len(newNotOld) > 0:
        LOG.write("WARNING: New data.pack directory has some folders not present in old data.pack directory: \n")
        for d in newNotOld:
            LOG.write("\t- " + d + "\n")

    if len(oldNotNew) > 0:
        LOG.write("WARNING: Old data.pack directory has some folders not present in new data.pack directory: \n")
        for d in oldNotNew:
            LOG.write("\t- " + d + "\n")

    if len(allDirs) > 0:

        config_overwrites = {}
        for folder in allDirs:

            baseTableFolder = os.path.join(oldBaseDir, folder)
            newTableFolder = os.path.join(newBaseDir, folder)

            quick_table = concatTablesInFolder(baseTableFolder)
            q2_table = concatTablesInFolder(newTableFolder)
            if q2_table == None or quick_table == None or quick_table.keyColumns[0] == None:
                LOG.write(
                    "ERROR: missing configuration for " + folder + " in Warhammer2_table_config!\nABORTING PROCESS FOR THIS FOLDER\n")
            else:
                basetable_columns = set(quick_table.columns)
                newtable_columns = set(q2_table.columns)
                added_columns = newtable_columns - basetable_columns
                removed_columns = basetable_columns - newtable_columns

                baseTableFolder_tables = load_folder_Tables(baseTableFolder)
                newTableFolder_tables = load_folder_Tables(newTableFolder)
                btft_set = set(baseTableFolder_tables.keys())
                ntft_set = set(newTableFolder_tables.keys())
                missing_tables = btft_set - ntft_set
                if len(missing_tables) > 0:
                    for m in missing_tables:
                        LOG.write("New data.pack missing table from old pack: " + m + "\n")

                if basetable_columns != newtable_columns:

                    if len(btft_set) > 1:
                        LOG.write("WARNING: found more than one table file in old data.pack export\n")

                    if len(ntft_set) > 1:
                        LOG.write("WARNING: found more than one table file in new data.pack export\n")

                    LOG.write("Processing changed columns for folder " + folder + "\n")
                    LOG.write("Added Columns: \n")
                    for ac in added_columns:
                        LOG.write(ac + "\n")
                    LOG.write("Removed Columns: \n")
                    for rc in removed_columns:
                        LOG.write(rc + "\n")

                    basetable = concatTablesInFolder(baseTableFolder)
                    newtable = concatTablesInFolder(newTableFolder)

                    results = find_renamed_columns(basetable, newtable)

                    for k in results.keys():
                        v = results[k]
                        LOG.write("Accepted mapping of " + k + " to " + v)
                    config_overwrites[folder] = results
                else:
                    config_overwrites[folder] = {}
        LOG.flush()
        return config_overwrites
    else:
        LOG.write("No shared folder names in both mod directory and base directory!\n")
        return {}









# Give me some space, goddamn atom
