from table_module import *
import table_module
import sys
import os

"""
Runs the run_diff commands for every file in a tree, given the following folder format:

<arg_1>\<table_name>\<table.tsv files>
<arg_2>\<table_name>\<other table.tsv files>

for example, you pass in "\mod_files" and "\base_files" where mod files holds the "new"
changes, compared to the "\base_files" folder (normally base_files would be the unedited
CA files exported for comparison)

This will look at each table name subfolder (such as "main_units_tables") in mod_files directory,
then concatenate that into one table object, and compare it against the corresponding table object
generated from the base_files directory (against the old, or pre-changed version of those files)

Then all diff results will be outputted to a Results folder, specifying what changes were made to
each table based on table name (so a separate file for changes made to main_units_tables).

No CSV will be generated if there are no changes
"""
def main(args):
    if len(args) != 3:
        sys.stderr.write("Error!\nUsage is \'python apply_differences.py oldBaseDir oldModDir newBaseDir\'\n")
        sys.stderr.write("Example: \'python apply_differences.py base_files mod_files\'\n")
        return -1
    else:
        oldBaseDir = args[0]
        oldModDir = args[1]
        newBaseDir = args[2]
        outputDir = newBaseDir + "_UPDATED"

        oldBaseLst = os.listdir(oldBaseDir)
        oldModLst = os.listdir(oldModDir)
        newBaseLst = os.listdir(newBaseDir)

        newFolderSet = set()
        baseFolderSet = set()
        modFolderSet = set()
        for tf in oldBaseLst:
            baseFolderSet |= {tf}
        for tf in oldModLst:
            modFolderSet |= {tf}
        for tf in newBaseLst:
            newFolderSet |= {tf}
        baseNotMod = baseFolderSet - modFolderSet
        modNotBase = modFolderSet - baseFolderSet
        allDirs = modFolderSet & baseFolderSet
        allDirs = allDirs & newFolderSet
        if len(baseNotMod) > 0:
            sys.stderr.write("Base directory has some folders not present in mod directory: \n")
            for d in baseNotMod:
                sys.stderr.write("\t- " + d + "\n")
        if len(modNotBase) > 0:
            sys.stderr.write("Mod directory has some folders not present in base directory: \n" + str(modNotBase) + "\n")
            for d in modNotBase:
                sys.stderr.write("\t- " + d + "\n")

        print allDirs
        try:
            os.makedirs(outputDir)
        except:
            pass

        if len(allDirs) > 0:
            for folder in allDirs:
                baseTableFolder = oldBaseDir + "\\" + folder
                modTableFolder = oldModDir + "\\" + folder
                newTableFolder = newBaseDir + "\\" + folder

                apply_diff_tree(baseTableFolder, modTableFolder, newTableFolder, outputDir)



        else:
            sys.stderr.write("No shared folder names in both mod directory and base directory!\n")




if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
