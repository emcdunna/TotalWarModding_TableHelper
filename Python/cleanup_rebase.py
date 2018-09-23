import sys
import os
from table_module import *

"""
finds issues based off of input data
args    0   the root data_pack directory
args    1   the mod directory

"""
def main(args):
    if len(args) != 3:
        sys.stderr.write("Error: Usage is python cleanup_rebase.py dataPackDirectory modDirectory outputDir\n")
        return -1
    LOG = sys.stdout
    root_dir = args[0]
    input_directory = args[1]
    outputDir = os.path.join(args[2],"db")

    # the dict of all tables in the root directory
    baseDirTables = load_directory_Tables(root_dir)

    # dict of all tables in the test directory
    input_dirTables = load_directory_Tables(input_directory)

    for folder in input_dirTables.keys():
        if True:#try:
            print("#" * 120)
            print("Folder " + folder)
            mod_folder_tables = input_dirTables[folder]
            base_folder_tables = baseDirTables[folder]

            table_names = mod_folder_tables.keys()
            base_table = base_folder_tables["data__"]

            main_table_dict = {}
            miss_table_dict = {}
            rem_table_dict = {}
            add_table_dict = {}
            broken_table_dict = {}
            collision_table_dict = {}
            bt_eks =set(base_table.entries.keys())

            # orient as to which table is which
            for t_name in table_names:
                table = mod_folder_tables[t_name]
                if "_MISSING" in t_name:
                    key = t_name[0:-8]
                    miss_table_dict[key]=table
                elif "_ADDED" in t_name:
                    key = t_name[0:-6]
                    add_table_dict[key]=table
                elif "_REMOVED" in t_name:
                    key = t_name[0:-8]
                    rem_table_dict[key]=table
                elif "_BROKEN-COLUMNS" in t_name:
                    key = t_name[0:-15]
                    broken_table_dict[key]=table
                elif "_COLLISION" in t_name:
                    key = t_name[0:-10]
                    collision_table_dict[key] = table
                else:
                    main_table_dict[t_name]=table

            """
                for each table group, assess the sub table files and compress them intelligently

                This will roll in the "missing" entries into the main file if the original file held more than 80 percent
                of data__.

                This will re-add the added entries back into the main table

                This IGNORES removed entries and BROKENCOLUMN entries
            """
            for key in main_table_dict.keys():
                print("-" * 50)
                print("Table: " + key)
                table = main_table_dict[key]

                mt_eks = set(table.entries.keys())
                share_eks = mt_eks & bt_eks
                share_ratio = (1.0 * len(share_eks)) / len(bt_eks)
                #print "Ratio " + str(share_ratio)
                # merge in missing entries if they should be merged
                if share_ratio > 0.8:

                    try:
                        m_table = miss_table_dict[key]
                        if "data__" == key:
                            print("\tNot adding missing entries to this table, since they were removed on purpose.")
                        else:
                            table = merge_tables(table, m_table)
                            table.fileName += "_FULL_data__"
                            print("\tAdding missing entries to this table and renaming it FULL ")
                    except KeyError:
                        pass

                try:
                    r_table = rem_table_dict[key]
                    print("\tIgnoring Removed table entries (these will remain removed in the cleaned rebase tsv file)")
                except KeyError:
                    pass
                try:
                    b_table = broken_table_dict[key]
                    print(
                        "\tIgnoring Broken Column table entries (these will remain removed in the cleaned rebase tsv file)")
                except KeyError:
                    pass
                try:
                    c_table = collision_table_dict[key]
                    print(
                        "\tIgnoring Collision table entries (these will remain removed in the cleaned rebase tsv file)")
                except KeyError:
                    pass

                # merge added entries back in
                try:
                    a_table = add_table_dict[key]
                    table = merge_tables(table, a_table)
                    print("\tRe-adding \'added\' entries to the table file.")
                except KeyError:
                    pass
                if len(table.entries) != 0:
                    table.print_to_file(os.path.join(outputDir,folder))
                else:
                    print("\tNot writing table file, as it is empty.")

            print("-" * 50)

        #except:
        #   pass



if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
















# EOF
