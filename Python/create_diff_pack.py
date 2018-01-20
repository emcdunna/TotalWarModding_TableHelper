import table_module
import sys
import os

"""

"""
def main(args):
    if len(args) != 2:
        sys.stderr.write("Error!\nUsage is \'python create_diff_pack.py baseDirectory modDirectory\'\n")
        return -1
    else:
        baseDirectory = os.path.join(args[0],"db")
        modDirectory = os.path.join(args[1],"db")

        baseLst = os.listdir(baseDirectory)
        modLst = os.listdir(modDirectory)
        tableFolderSet = set()
        baseFolderSet = set()
        modFolderSet = set()
        for tf in baseLst:
            tableFolderSet |= {tf}
            baseFolderSet |= {tf}
        for tf in modLst:
            tableFolderSet |= {tf}
            modFolderSet |= {tf}
        baseNotMod = baseFolderSet - modFolderSet
        modNotBase = modFolderSet - baseFolderSet
        bothDirs = modFolderSet & baseFolderSet
        if len(baseNotMod) > 0:
            sys.stderr.write("Base directory has some folders not present in mod directory: \n")
            for d in baseNotMod:
                sys.stderr.write("\t- " + d + "\n")
        if len(modNotBase) > 0:
            sys.stderr.write("Mod directory has some folders not present in base directory: \n")
            for d in modNotBase:
                sys.stderr.write("\t- " + d + "\n")
        if len(bothDirs) > 0:
            for folder in bothDirs:
                baseTableFolder = os.path.join(baseDirectory,folder)
                modTableFolder = os.path.join(modDirectory,folder)

                baseTable = table_module.concatTablesInFolder(baseTableFolder)
                modTable = table_module.concatTablesInFolder(modTableFolder)

                new_table = table_module.create_diff_table(baseTable, modTable)

                if new_table != None:
                    o_file = open("Results/DIFF_PACK_" + folder + ".tsv", "w")
                    o_file.write(new_table.get_fileprint_string())
        else:
            sys.stderr.write("No shared folder names in both mod directory and base directory!\n")


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
