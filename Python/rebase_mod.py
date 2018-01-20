from table_module import *
import table_module
import sys
import os
import datetime


"""
Runs the rebase commands for every file in a tree, given the following folder format:

<arg_1>\db\<table_name>\<table.tsv files>
<arg_2>\db\<table_name>\<other table.tsv files>
<arg_3>\db\<table_name>\<new table.tsv files>

Note the "db" required subdirectory. This is because this should run off of the folder structure
that will be created when using "export all as TSV" from PFM.

This program will look at all of the changes between oldBaseDir and oldModDir, and re-apply those changes to
the newBaseDir files, and save them to a new directory called "REBASED_MOD_(timestamp)".

The point of this would be to take an overhaul mod and run it with the old data.pack export, against the new data.pack
export, to get an overhaul mod working again.

For example if you had an overhaul mod exported at "mod_pack", the old data.pack exported at "old_data" and the new data.pack
exported at "new_data", you would just run "python rebase_mod.py old_data mod_pack new_data" to get all of the changes
between mod_pack and old_data applied to the new_data files, leaving all other stuff unchanged.

Ideally this would allow you to carry over edits to melee_attack (for example), without caring about voice_actor name changes.

In Git / SVN language, this is like doing a "rebase" to the new remote master (CA's patch)
"""
def main(args):
    if len(args) != 3:
        sys.stderr.write("Error!\nUsage is \'python apply_differences.py oldBaseDir oldModDir newBaseDir\'\n")
        sys.stderr.write("Default output will be REBASED_MOD_<timestamp>\n")
        return -1
    else:
        oldBaseDir = os.path.join(args[0],"db")
        oldModDir = os.path.join(args[1],"db")
        newBaseDir = os.path.join(args[2],"db")
        outputDir = "REBASED_MOD_" + str(datetime.datetime.now()).split(" ")[0]

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
        newNotOld = newFolderSet - baseFolderSet
        oldNotNew = baseFolderSet - newFolderSet
        modNotNew = modFolderSet - newFolderSet
        allDirs = modFolderSet & baseFolderSet
        allDirs = allDirs & newFolderSet

        if len(newNotOld) > 0:
            sys.stderr.write("WARNING: New data.pack directory has some folders not present in old data.pack directory: \n")
            for d in baseNotMod:
                sys.stderr.write("\t- " + d + "\n")

        if len(oldNotNew) > 0:
            sys.stderr.write("WARNING: Old data.pack directory has some folders not present in new data.pack directory: \n")
            for d in baseNotMod:
                sys.stderr.write("\t- " + d + "\n")

        if len(modNotBase) > 0:
            sys.stderr.write("ERROR: Mod directory has some folders not present in old data.pack directory: \n" + str(modNotBase) + "\n")
            for d in modNotBase:
                sys.stderr.write("\t- " + d + "\n")

        if len(modNotNew) > 0:
            sys.stderr.write("ERROR: Mod directory has some folders not present in new data.pack directory: \n" + str(modNotBase) + "\n")
            for d in modNotBase:
                sys.stderr.write("\t- " + d + "\n")

        try:
            os.makedirs(outputDir)
        except:
            pass

        """
        This apply diff will not compress tables into one mega table, and will account for missing keys in new data.pack,
        and will account for if the mod used "data__" table (so if you removed any entries from data__, they will stay
        removed after this, but all "new" entries in the data__ table will still exist)
        """
        if len(allDirs) > 0:
            for folder in allDirs:
                sys.stderr.write("Processing " + folder + "\n")
                print "Processing " + folder
                baseTableFolder = os.path.join(oldBaseDir,folder)
                modTableFolder = os.path.join(oldModDir,folder)
                newTableFolder = os.path.join(newBaseDir,folder)

                basetable_columns = set(concatTablesInFolder(baseTableFolder).columns)
                newtable_columns = set(concatTablesInFolder(newTableFolder).columns)
                added_columns = newtable_columns - basetable_columns
                removed_columns = basetable_columns - newtable_columns

                if basetable_columns != newtable_columns:
                    sys.stderr.write("WARNING: columns have changed for folder " + folder + "\n")
                    sys.stderr.write("Added Columns: \n")
                    for ac in added_columns:
                        sys.stderr.write(ac + "\n")
                    sys.stderr.write("Removed Columns: \n")
                    for rc in removed_columns:
                        sys.stderr.write(rc + "\n")
                    break

                baseTableFolder_tables = load_folder_Tables(baseTableFolder)
                modTableFolder_tables = load_folder_Tables(modTableFolder)
                newTableFolder_tables = load_folder_Tables(newTableFolder)

                btft_set = set(baseTableFolder_tables.keys())
                mtft_set = set(modTableFolder_tables.keys())
                ntft_set = set(newTableFolder_tables.keys())
                print "old base tables"
                print btft_set
                print "mod tables"
                print mtft_set
                print "new base tables"
                print ntft_set

                if (len(btft_set) >1):
                    sys.stderr.write("Warning: found more than one table file in old data.pack export\n")
                    break

                if (len(ntft_set) >1):
                    sys.stderr.write("Warning: found more than one table file in new data.pack export\n")
                    break

                # decide which tables are overwrites and whcih are not
                overwritten_tables = mtft_set & btft_set
                other_tables = mtft_set - btft_set

                print "overwritten tables:"
                print overwritten_tables
                if (mtft_set & btft_set & ntft_set) != overwritten_tables:
                    sys.stderr.write("Missing some overwritten tables!\n")
                    break

                missing_tables = btft_set - ntft_set
                if len(missing_tables) >0:
                    for m in missing_tables:
                        sys.stderr.write("New data.pack missing table from old pack: " + m + "\n")
                    break

                # Rebase every table that is an overwrite of a data.pack one
                for tablekey in overwritten_tables:
                    modtable = modTableFolder_tables[tablekey]
                    basetable = baseTableFolder_tables[tablekey]
                    newtable = newTableFolder_tables[tablekey]

                    # rebases this table, keeping all common entries and re-deleting all removed ones
                    sys.stderr.write("Rebasing " + folder + " - " + tablekey + "\n")
                    rebased_table = rebase_table(basetable,modtable,newtable,True)
                    if rebased_table != None:
                        o_dir = os.path.join(outputDir, folder)
                        try:
                            os.makedirs(o_dir)
                        except:
                            pass
                        rebased_table.print_to_file(o_dir)

                # for all other file names...

                basetable = concatTablesInFolder(baseTableFolder)
                newtable = concatTablesInFolder(newTableFolder)
                for tablekey in other_tables:
                    modtable = modTableFolder_tables[tablekey]
                    sys.stderr.write("Rebasing " + folder + " - " + tablekey + "\n")

                    rebased_table = rebase_table(basetable,modtable,newtable,False)

                    if rebased_table != None:
                        o_dir = os.path.join(outputDir, folder)
                        try:
                            os.makedirs(o_dir)
                        except:
                            pass
                        rebased_table.print_to_file(o_dir)


        else:
            sys.stderr.write("No shared folder names in both mod directory and base directory!\n")




if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
