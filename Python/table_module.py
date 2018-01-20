import sys
import warhammer2_table_config
import os
import copy

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
        self.name = "Default"
        self.lineTwo = "" # 34, for example saying there are 34 columns
        self.entryKey = [None] # a list of every column name that acts as part of the key
        self.folder = ""

    def __str__(self):
        word = ""
        word += self.name + "\n"
        word += "Key Column(s): " + str(self.entryKey) + "\n"
        word += stringify_list(self.columns, self.separator) + "\n"
        for ek in self.entries.keys():
            word += self.stringify_entry(ek) + "\n"
        return word

    # returns the entry key for a particular entry based off the table's entry key metadata
    def get_entry_key(self, entry):
        #print "Entry " + str(entry)
        ek = "EK:  "
        i = 1
        #print "Key columns " + str(self.entryKey)

        for keyCol in self.entryKey: # iterate through each entry key column, add the value of that column to the key string
            if keyCol == None:
                return "NULL_ENTRY_KEY"
            ek += entry[keyCol]
            if i < len(self.entryKey):
                ek += "  TO  "
                i +=1
        return ek

    def get_file_extension(self):
        if(self.separator == ","):
            return ".csv"
        elif(self.separator == "\t"):
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
            if (j < len(self.columns)):
                line += self.separator
        return line

    def get_fileprint_string(self):
        word = ""
        word += self.name + "\n"
        word += (self.lineTwo)
        word += (stringify_list(self.columns, self.separator) + "\n")
        for ek in self.entries.keys():
            word += (self.stringify_entry(ek) + "\n")
        return word

    def print_to_file(self, directory):
        ftype = ".csv"
        if(self.separator != ","):
            ftype = ".tsv"
        fname = os.path.join(directory, self.name + ftype)

        f = open(fname,"w")
        f.write(self.get_fileprint_string())

    def __len__(self):
        return len(entries)
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
        entryKeySet = set(self.oldTable.entries.keys()) | set(self.newTable.entries.keys())

        if(self.oldTable.name != self.newTable.name):
            sys.stderr.write("Tables have different names! \n")
            return False

        elif(self.oldTable.columns != self.newTable.columns):
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

            if(oldEntry != None and newEntry != None):
                for col in self.oldTable.columns: #TODO dont just iterate through oldTable

                    oldv = oldEntry[col]
                    try:
                        newv = newEntry[col]
                    except KeyError as e:
                        newv = "MISSING"
                    if(oldv != newv):
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
        if (j < len(lst)):
            line += sep
    return line

"""
Takes in string line and separator character
returns lst of items
"""
def parse_line_to_list(line, sep):
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
def file_loader(csvFile):
    table = Table()
    if (csvFile.name[-4:] != ".tsv") and (csvFile.name[-4:] != ".csv"):
        sys.stderr.write("Invalid file: " + csvFile.name + "\n")
        return None

    if (".tsv" in csvFile.name):
        table.separator = "\t"
    i = 0
    for line in csvFile:
        entry = dict()
        lst = []
        if(i == 0):
            lst = parse_line_to_list(line, table.separator)
            if(len(lst) > 0):
                table.name = lst[0]
                try:
                    table.entryKey = warhammer2_table_config.keyDict[table.name] # reference config library
                except KeyError as e:
                    sys.stderr.write("EntryKey not found for table: " + table.name + "\n")
                    return None
            else:
                sys.stderr.write("Empty first line in file: " + csvFile.name + "\n")

        elif(i==1):
            table.lineTwo = line
        elif(i==2):
            table.columns = parse_line_to_list(line, table.separator)
        else:
            lst = parse_line_to_list(line, table.separator)
            if (len(lst) == len(table.columns)):
                j = 0
                for col in table.columns:
                    entry[col] = lst[j]
                    j+=1
                entry_key = table.get_entry_key(entry) # contains a dict of col_name: value pairs
                table.entries[entry_key] = entry
            else:
                sys.stderr.write("Mismatched entry: " + line + "\n")
        i+=1
    # print "Adding file: " + csvFile.name + " for " + table.name
    return table

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
Used to merge two table objects together, which were loaded from different files, and
should allow entries from second table to override entries in the first table.
Returns the base table object which stores both sets of information concatenated together.
"""
def merge_tables(bot_table, top_table):
    if(bot_table.name != top_table.name):
        sys.stderr.write("Merging tables " + bot_table.name + " have different names!\n")
        return None
    elif(bot_table.columns != top_table.columns):
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
def concatTablesInFolder(folder):
    lst = os.listdir(folder)
    lstTSV = []
    # remove non tsv/csv files
    for l in lst:
        if (".tsv" in l) or (".csv" in l):
            lstTSV.append(l)

    # sort the way the launcher loads, where alphanumerically lower names supercede higher names
    lst = sorted(lstTSV, key=str.lower, reverse=True)
    # TODO CHECK THIS ORDER!

    i = 0
    baseTable = None
    for tsvFile in lst:
        tmpFile = open(folder + "\\" + lst[i], 'r')
        if i == 0:
            baseTable = file_loader(tmpFile)
            if baseTable == None:
                return None
        else:
            tmpTable = file_loader(tmpFile)
            baseTable = merge_tables(baseTable,tmpTable)
        i += 1
    return baseTable


"""
Loads all tables in this folder, returns a map of table file's name to its table objects
"""
def load_folder_Tables(folder):
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
        baseTable = file_loader(tmpFile)
        baseTableMap[tsvFile.split(".")[0]] = baseTable
    return baseTableMap

"""
returns a set of differneces if the entry exists in both tables and has been edited
"""
def get_entry_diff(ek, basetable, modtable):
    differences = set()
    baseentry = basetable.entries[ek]
    modentry = modtable.entries[ek]

    for col in basetable.columns:
        baseval = baseentry[col]
        modval = modentry[col]
        if(baseval != modval):
            diff = Diff(ek, col, baseval, modval)
            differences |= {diff}
    return differences

"""
rebases a table object onto another table object

if overwrite = true then the rebase will not add any entries that were deleted in the mod table
also, if overwrite = false, then the rebase will remove any entire etnries that are not edited in mod table

OVERWRITES MOD TABLE AND RETURNS IT EDITED
"""
def rebase_table(oldTable, modTable, newTable, overwrite=False):
    ot_entries = set(oldTable.entries.keys())
    mt_entries = set(modTable.entries.keys())
    nt_entries = set(newTable.entries.keys())

    possible_edits = ot_entries & mt_entries
    added_entries = mt_entries - ot_entries
    mod_removed_entries = ot_entries - mt_entries
    new_removed_entries = ot_entries - nt_entries
    new_entries = nt_entries - ot_entries
    if (len(new_removed_entries) > 0) and (overwrite == True or (len(new_removed_entries & mt_entries) > 0)):
        sys.stderr.write("ERROR Newly removed entries: \n" + str(new_removed_entries) + "\n")
        return None

    # Must add every new entry in newTable
    if overwrite == True:
        for ek in new_entries:
            modTable.entries[ek] = copy.copy(new_entries.entries[ek])
            # TODO: LOG THIS: sys.stderr.write("Added entry from new data.pack: " + ek + "\n")

    # must KEEP every entry found in Mod table not found in old base table (since it got added)
    # pass: they already exist in mod_table...
    # TODO: When supporting certain situations (like column changes), added entries will cause errors

    # apply changes to all edited entries to the new table's version of that entry
    for ek in possible_edits:
        differences = get_entry_diff(ek, oldTable, modTable)
        modTable.entries[ek] = copy.copy(newTable.entries[ek])
        entry = modTable.entries[ek]
        # leave unedited lines in the mod table
        for df in differences:
            entry[df.column] = df.newValue
            # TODO: Log all of these edits!
        # Now the entry has only the pack's changed things edited

    # TODO: SAFE MODE! report any time a mod edits a value also changed in the update!



    # TODO: Test that removed entries stay removed!
    # TODO: Test everything else!

    return modTable



"""
Runs a diff for the single table (ex. "main_units_tables") folder, to generate diff of
mod table against base table.
"""
def run_diff(baseTableFolder, modTableFolder):
    baseTable = concatTablesInFolder(baseTableFolder)
    modTable = concatTablesInFolder(modTableFolder)

    tablediff = TableDiff(baseTable, modTable) # detects differences between two tables

    if(len(tablediff.differences) == 0):
        sys.stderr.write("Not writing diff file for: " + baseTable.name + " because there are no differences.\n")
    else:
        diff_file = open("Results\\" + modTable.name + "_CHANGES.tsv","w")
        diff_file.write("Changes between " + baseTableFolder + " (base) and " + modTableFolder + " (mod)\n")
        diff_file.write(tablediff.to_tsv() + "\n")



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


















# Give me some space, goddamn atom
