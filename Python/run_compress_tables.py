import table_module
import sys
import os

"""
Compresses tables in a directory's folders, the way the total war loader does at launch time.
Spits out table files in a new directory.
"""
def main(args):
    if len(args) != 2:
        sys.stderr.write("Error!\nUsage is \'python run_compress_tables.py directory new_name\'\n")
        sys.stderr.write("Example: \'python run_compress_tables.py mod_directory new_name\'\n")
        return -1
    else:
        root_directory = args[0]
        new_name = args[1]
        newDirectory = os.path.join(root_directory,"db_COMPRESSED")
        directory = os.path.join(root_directory, "db")

        folderList = os.listdir(directory)

        for folder in folderList:
            tableFolder = os.path.join(directory,folder)
            table = table_module.concatTablesInFolder(tableFolder)
            table.fileName = new_name

            if(table != None):
                if(len(table.entries) == 0):
                    sys.stderr.write("Ignoring table: " + table.name + " because it contains no entries.\n")
                else:
                    table.print_to_file(os.path.join(newDirectory,folder))


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
