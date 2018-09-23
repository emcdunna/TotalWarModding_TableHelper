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

Ideally this would allow you to carry over edits to melee_attack (for example), without caring about things like
voice_actor name changes, or new columns or even new entries added to tables

In Git / SVN language, this is like doing a "rebase" to the new remote master (CA's patch)
"""
def main(args):
    if len(args) != 3:
        sys.stderr.write("Error!\nUsage is \'python rebase_mod.py oldBaseDir oldModDir newBaseDir\'\n")

        return -1
    else:

        LOG = sys.stderr

        oldBaseDir = os.path.join(args[0],"db")
        oldModDir = os.path.join(args[1],"db")
        newBaseDir = os.path.join(args[2],"db")
        outputDir = "REBASED_MOD_"+ str(datetime.datetime.now()).split(" ")[0] + "\\db"
        print("Output dir: " + outputDir)
        #outputDir = os.path.join(args[3],"db")

        oldBaseLst = os.listdir(oldBaseDir)
        oldModLst = os.listdir(oldModDir)
        newBaseLst = os.listdir(newBaseDir)

        newFolderSet = set(newBaseLst)
        baseFolderSet = set(oldBaseLst)
        modFolderSet = set(oldModLst)

        baseNotMod = baseFolderSet - modFolderSet
        modNotBase = modFolderSet - baseFolderSet
        newNotOld = newFolderSet - baseFolderSet
        oldNotNew = baseFolderSet - newFolderSet
        modNotNew = modFolderSet - newFolderSet

        allDirs = modFolderSet & baseFolderSet & newFolderSet

        if len(newNotOld) > 0:
            LOG.write("WARNING: New data.pack directory has some folders not present in old data.pack directory: \n")
            for d in newNotOld:
                LOG.write("\t- " + d + "\n")

        if len(oldNotNew) > 0:
            LOG.write("WARNING: Old data.pack directory has some folders not present in new data.pack directory: \n")
            for d in oldNotNew:
                LOG.write("\t- " + d + "\n")

        if len(modNotBase) > 0:
            LOG.write("ERROR: Mod directory has some folders not present in old data.pack directory: \n")
            for d in modNotBase:
                LOG.write("\t- " + d + "\n")

        if len(modNotNew) > 0:
            LOG.write("ERROR: Mod directory has some folders not present in new data.pack directory: \n")
            for d in modNotNew:
                LOG.write("\t- " + d + "\n")

        try:
            os.makedirs(outputDir)
        except:
            pass

        renamed_columns = detect_renamed_columns(oldBaseDir, newBaseDir, open(os.path.join(outputDir,"renamed_cols.txt"),"w"))

        """
        This apply diff will not compress tables into one mega table, and will account for missing keys in new data.pack,
        and will account for if the mod used "data__" table (so if you removed any entries from data__, they will stay
        removed after this, but all "new" entries in the data__ table will still exist)
        """
        if len(allDirs) > 0:
            for folder in allDirs:
                try:
                    folder_renamed_columns = renamed_columns[folder]
                except KeyError:
                    folder_renamed_columns = {}

                try:
                    os.makedirs(os.path.join(outputDir,folder))
                except:
                    pass
                LOG = open(os.path.join(outputDir,folder,"log.txt"),"w")
                LOG.write("-" * 100 + "\n")
                LOG.write("Processing " + folder + "\n")

                baseTableFolder = os.path.join(oldBaseDir,folder)
                modTableFolder = os.path.join(oldModDir,folder)
                newTableFolder = os.path.join(newBaseDir,folder)

                quick_table = concatTablesInFolder(baseTableFolder)
                if quick_table.keyColumns[0] == None:
                    LOG.write("ERROR: missing configuration for " + folder + " in Warhammer2_table_config!\nABORTING PROCESS FOR THIS FOLDER\n")
                else:
                    basetable_columns = set(quick_table.columns)
                    newtable_columns = set(concatTablesInFolder(newTableFolder).columns)
                    added_columns = newtable_columns - basetable_columns
                    removed_columns = basetable_columns - newtable_columns

                    if basetable_columns != newtable_columns:
                        LOG.write("WARNING: columns have changed for folder " + folder + "\n")
                        LOG.write("Added Columns: \n")
                        for ac in added_columns:
                            LOG.write(ac + "\n")
                        LOG.write("Removed Columns: \n")
                        for rc in removed_columns:
                            LOG.write(rc + "\n")
                        LOG.write("""WARNING: Any added entries will be written to a 'Broken' file in the same output directory, as they will have issues that must be manually resolved""")
                        LOG.write("\n")
                    for a in folder_renamed_columns.keys():
                        LOG.write("Treating column " + folder_renamed_columns[a] + " as new column " + a + "\n")
                        added_columns -= {a}
                        removed_columns -= {folder_renamed_columns[a]}
                    baseTableFolder_tables = load_folder_Tables(baseTableFolder,folder_renamed_columns)
                    modTableFolder_tables = load_folder_Tables(modTableFolder,folder_renamed_columns)
                    newTableFolder_tables = load_folder_Tables(newTableFolder,folder_renamed_columns)

                    btft_set = set(baseTableFolder_tables.keys())
                    mtft_set = set(modTableFolder_tables.keys())
                    ntft_set = set(newTableFolder_tables.keys())
                    LOG.write( "old base tables\n")
                    LOG.write( str(btft_set) + "\n")
                    LOG.write( "mod tables" + "\n")
                    LOG.write( str(mtft_set) + "\n")
                    LOG.write( "new base tables"+ "\n")
                    LOG.write( str(ntft_set) + "\n")

                    # Assumes that there will only be data__.tsv and thats it, if there are
                    # more than one CA pack, there might be a lot of issues merging that together
                    # TODO: Determine what we should do here
                    if (len(btft_set) >1):
                        LOG.write("WARNING: found more than one table file in old data.pack export\n")

                    if (len(ntft_set) >1):
                        LOG.write("WARNING: found more than one table file in new data.pack export\n")

                    # decide which tables are overwrites and which are not
                    overwritten_tables = mtft_set & btft_set
                    other_tables = mtft_set - btft_set

                    LOG.write( "overwritten tables:\n")
                    LOG.write( str(overwritten_tables) + "\n")
                    # Checks if the new data pack files also exist for all overwritten tables
                    if (mtft_set & btft_set & ntft_set) != overwritten_tables:
                        LOG.write("Missing some overwritten tables in new data.pack!\n")
                        break

                    missing_tables = btft_set - ntft_set
                    if len(missing_tables) >0:
                        for m in missing_tables:
                            LOG.write("New data.pack missing table from old pack: " + m + "\n")

                    # Rebase every table that is an overwrite of a data.pack one
                    for tablekey in overwritten_tables:
                        modtable = modTableFolder_tables[tablekey]
                        basetable = baseTableFolder_tables[tablekey]
                        newtable = newTableFolder_tables[tablekey]

                        # rebases this table, keeping all common entries and re-deleting all removed ones
                        LOG.write("-" * 40 + "\n")
                        LOG.write("Rebasing " + folder + " - " + tablekey + "\n")
                        rebased_table = rebase_table(basetable,modtable,newtable, LOG, True, added_columns, removed_columns, True)
                        if rebased_table != None:
                            o_dir = os.path.join(outputDir, folder)
                            try:
                                os.makedirs(o_dir)
                            except:
                                pass
                            rebased_table.print_to_file(o_dir)
                        else:
                            LOG.write("Rebased table came back as None\n")

                    # Rebase all non-overwrite tables
                    basetable = concatTablesInFolder(baseTableFolder,folder_renamed_columns)
                    newtable = concatTablesInFolder(newTableFolder,folder_renamed_columns)
                    for tablekey in other_tables:
                        modtable = modTableFolder_tables[tablekey]
                        LOG.write("-" * 40 + "\n")
                        LOG.write("Rebasing " + folder + " - " + tablekey + "\n")

                        rebased_table = rebase_table(basetable,modtable,newtable, LOG, False, added_columns, removed_columns, True)

                        if rebased_table != None:
                            o_dir = os.path.join(outputDir, folder)
                            try:
                                os.makedirs(o_dir)
                            except:
                                pass
                            rebased_table.print_to_file(o_dir)
                        else:
                            LOG.write("Rebased table came back as None\n")


        else:
            LOG.write("No shared folder names in both mod directory and base directory!\n")




if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
