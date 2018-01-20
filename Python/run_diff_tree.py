import table_module
import sys
import os

"""
Runs the run_diff commands for every file in a tree, given the following folder format:

<arg_1>\db\<table_name>\<table.tsv files>
<arg_2>\db\<table_name>\<other table.tsv files>

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
    if len(args) != 2:
        sys.stderr.write("Error!\nUsage is \'python run_diff_tree.py baseDirectory modDirectory\'\n")

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

                table_module.run_diff(baseTableFolder, modTableFolder)
                sys.stderr.write("Output under Results folder\n")
        else:
            sys.stderr.write("No shared folder names in both mod directory and base directory!\n")


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
