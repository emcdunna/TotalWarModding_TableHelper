from table_module import *
import table_module
import sys
import os

"""
Runs the apply_differences commands for every file in a tree, given the following folder format:

<arg_1>\db\<table_name>\<table.tsv files>
<arg_2>\db\<table_name>\<other table.tsv files>
<arg_3>\db\<table_name>\<new table.tsv files>

Note the "db" required subdirectory. This is because this should run off of the folder structure
that will be created when using "export all as TSV" from PFM.

This program will look at all of the changes between oldBaseDir and oldModDir, and re-apply those changes to
the newBaseDir files, and save them to a new directory called "APPLY_DIFF_OUTPUT_DIR".

The point of this would be to take an overhaul mod and run it with the old data.pack export, against the new data.pack
export, to get an overhaul mod working again.

For example if you had an overhaul mod exported at "mod_pack", the old data.pack exported at "old_data" and the new data.pack
exported at "new_data", you would just run "python apply_differences.py old_data mod_pack new_data" to get all of the changes
between mod_pack and old_data applied to the new_data files, leaving all other stuff unchanged.

Ideally this would allow you to carry over edits to melee_attack (for example), without caring about voice_actor name changes. 
"""
def main(args):
    if len(args) != 3:
        sys.stderr.write("Error!\nUsage is \'python apply_differences.py oldBaseDir oldModDir newBaseDir\'\n")
        return -1
    else:
        oldBaseDir = args[0]
        oldModDir = args[1]
        newBaseDir = args[2]
        outputDir = "APPLY_DIFF_OUTPUT_DIR"

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

        #print allDirs
        try:
            os.makedirs(outputDir)
        except:
            pass

        if len(allDirs) > 0:
            for folder in allDirs:
                baseTableFolder = os.path.join(oldBaseDir,folder)
                modTableFolder = os.path.join(oldModDir,folder)
                newTableFolder = os.path.join(newBaseDir,folder)

                # compresses all tables in each folder, and applies differences to a this table object
                updatedTable = apply_diff_tree(baseTableFolder, modTableFolder, newTableFolder)
                if updatedTable != None:
                    try:
                        os.makedirs(os.path.join(outputDir,folder))
                    except:
                        pass
                    o_file = open(os.path.join(outputDir,folder,"updated" + updatedTable.get_file_extension()),'w')
                    o_file.write(updatedTable.get_fileprint_string())



        else:
            sys.stderr.write("No shared folder names in both mod directory and base directory!\n")




if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
