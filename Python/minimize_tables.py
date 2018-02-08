from table_module import *
import sys
import os


"""
Does what in PFM is called "postprocess -> minimize" which basically deletes out any common entry between this
mod and the corresponding data.pack export directory.

The purpose of this is to clean a pack (like when you are exporting a mod from Assembly kit) of all the extra
changes that you don't want.

Will print out tables that ONLY contain edited entries.
"""
def main(args):
    if len(args) != 3:
        sys.stderr.write("Error!\nUsage is \'python minimize_tables.py datapackDir modDir outputDir\'\n")
        return -1
    else:
        baseDirectory = os.path.join(args[0],"db")
        modDirectory = os.path.join(args[1],"db")
        outputDir =  os.path.join(args[2],"db")
        baseLst = set(os.listdir(baseDirectory))
        modLst = set(os.listdir(modDirectory))
        bothDirs = baseLst & modLst

        try:
            os.makedirs(outputDir)
        except:
            pass

        if len(bothDirs) > 0:
            for folder in bothDirs:
                sys.stdout.write("Minimizing folder: " + folder + "\n")
                try:
                    baseTableFolder = os.path.join(baseDirectory,folder)
                    modTableFolder = os.path.join(modDirectory,folder)

                    baseTable = concatTablesInFolder(baseTableFolder)
                    modTable = concatTablesInFolder(modTableFolder)

                    newTable = unique_table(baseTable,modTable, sys.stdout)

                    fpath = os.path.join(outputDir,folder)
                    try:
                        os.makedirs(fpath)
                    except:
                        pass
                    newTable.print_to_file(fpath)
                except:
                    sys.stdout.write("FOLDER ERROR with folder " + folder + "\n")

        else:
            sys.stderr.write("No shared folder names in both mod directory and base directory!\n")


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
