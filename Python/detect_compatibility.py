import table_module
import sys
import os

"""
Detects compatibility for two exports, given the following folder format:

<arg_1>\db\<table_name>\<table.tsv files>
<arg_2>\db\<table_name>\<other table.tsv files>

for example, you pass in "\mod1" and "\mod2" it will detect all instances where mod1 and mod2
both use the same entry_key.

For example if one mod promises to increase upkeep by 50% for every unit, and another mod promises
it will double unit sizes, one will find that both of those changes require editing entries in
main_units_tables, and a list of all of the entries in that table will be the output.
"""
# TODO look for __data as name of files
# TODO look to see if the mod has the same file names, which would cause crash
def main(args):
    if len(args) != 2:
        sys.stderr.write("Error!\nUsage is \'python detect_compatibility.py mod1_dir mod2_dir\'\n")
        return -1
    else:
        mod1_Directory = os.path.join(args[0],"db")
        mod2_Directory = os.path.join(args[1],"db")

        mod1_Lst = os.listdir(mod1_Directory)
        mod2_Lst = os.listdir(mod2_Directory)
        tableFolderSet = set()
        mod1_FolderSet = set()
        mod2_FolderSet = set()
        for tf in mod1_Lst:
            tableFolderSet |= {tf}
            mod1_FolderSet |= {tf}
        for tf in mod2_Lst:
            tableFolderSet |= {tf}
            mod2_FolderSet |= {tf}
        #mod1_Notmod2 = mod1_FolderSet - mod2_FolderSet
        #mod2_Notmod1 = mod2_FolderSet - mod1_FolderSet
        bothDirs = mod2_FolderSet & mod1_FolderSet

        if len(bothDirs) > 0:
            for folder in bothDirs:
                mod1_tablefolder = os.path.join(mod1_Directory,folder)
                mod2_tablefolder = os.path.join(mod2_Directory,folder)

                mod1_table = table_module.concatTablesInFolder(mod1_tablefolder)
                mod2_table = table_module.concatTablesInFolder(mod2_tablefolder)
                run = True
                if mod1_table == None:
                    sys.stderr.write("Issue with " + mod1_Directory + "\\" + folder + "\n")
                    run = False
                if mod2_table == None:
                    sys.stderr.write("Issue with " + mod2_Directory + "\\" + folder + "\n")
                    run = False
                if(run):
                    both_keys = ( set(mod1_table.entries.keys()) & set(mod2_table.entries.keys()) )

                    if len(both_keys) > 0:
                        sys.stdout.write("\nFolder: " + folder + " has compatibility issues. Both mods edit the following entries: \n")
                        for b in both_keys:
                            sys.stdout.write(str(b) + "\n")


        else:
            sys.stderr.write("No shared folder names in both mod 1 directory and mod 2 directory!\n")


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
