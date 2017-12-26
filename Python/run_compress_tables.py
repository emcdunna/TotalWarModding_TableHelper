import table_module
import sys
import os

"""
Compresses tables in a directory's folders, the way the total war loader does at launch time.
Spits out table files in a new directory.
"""
def main(args):
    if len(args) != 1:
        sys.stderr.write("Error!\nUsage is \'python run_compress_tables.py directory\'\n")
        sys.stderr.write("Example: \'python run_compress_tables.py mod_directory\'\n")
        return -1
    else:
        directory = args[0]
        newDirectory = directory + "_COMPRESSED"
        try:
            os.mkdir(newDirectory)
        except WindowsError as e:
            pass
        folderList = os.listdir(directory)

        for folder in folderList:

            tableFolder = directory + "\\" + folder
            table = table_module.concatTablesInFolder(tableFolder,None)
            if(table != None):
                if(len(table.entries) == 0):
                    sys.stderr.write("Ignoring table: " + table.name + " because it contains no entries.\n")
                else:
                    output = table.get_fileprint_string()
                    o_folder = newDirectory + "\\" + folder
                    try:
                        os.mkdir(o_folder)
                    except WindowsError as e:
                        pass
                    o_name = o_folder + "\\NEW_" + table.name + table.get_file_extension()
                    o_file = open(o_name,'w')
                    o_file.write(output)


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
