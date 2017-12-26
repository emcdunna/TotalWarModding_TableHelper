import table_module
import sys

#ex = "..\Warhammer\main_units_tables\"

"""
Simple script to run a diff on two files only. Should be the same folder type (like both
be main_units_tables)
"""
def main(args):
    if len(args) != 2:
        sys.stderr.write("Error!\nUsage is \'python run_diff.py oldFile newFile\'\n")
        sys.stderr.write("Example: \'python run_diff.py old_main_units.tsv new_main_units.tsv\'\n")
        return -1
    oldFileN = args[0]
    newFileN = args[1]
    oldFile = open(oldFileN, 'r')
    newFile = open(newFileN, 'r')

    oldTable = table_module.file_loader(oldFile)
    newTable = table_module.file_loader(newFile)


    tablediff = table_module.TableDiff(oldTable, newTable) # detects differences between two tables

    diff_file = open("Results\\" + newTable.name + "_CHANGES.tsv","w")
    diff_file.write("Changes between " + oldFileN + " (old) and " + newFileN + " (new)\n")
    diff_file.write(tablediff.to_tsv() + "\n")


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
