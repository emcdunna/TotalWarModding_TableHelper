import table_module
import sys
import os

"""
Applies all of the data for a specific column from the mod file to the base file, leaving all else
the same as the base folder.

"""
def main(args):
    if len(args) != 3:
        sys.stderr.write("Error!\nUsage is \'python run_diff_tree.py base_file mod_file column_name\'\n")
        return -1
    else:
        column = args[2]
        baseFile = open(args[0], 'r')
        modFile = open(args[1], 'r')

        baseTable = table_module.file_loader(baseFile)
        modTable = table_module.file_loader(modFile)

        if (column in baseTable.columns):
            for entryKey in modTable.entries.keys():

                try:
                    baseTable.entries[entryKey][column] = modTable.entries[entryKey][column]

                except:
                    sys.stderr.write("Skipping " + entryKey + " due to key error\n")
            o_file = open("APPLIED_COLUMNS_" + baseTable.name + baseTable.get_file_extension(), 'w')
            o_file.write(baseTable.get_fileprint_string())
        else:
            sys.stderr.write("Invalid column name.\n")


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
