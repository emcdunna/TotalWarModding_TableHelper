import sys
import os
from table_module import *


def print_log_set(data,offset):
    word = ""
    for d in data:
        word += (offset + "* \'" + str(d) +"\'" + "\n")
    return word

def replace_missing_refs(table, column, missing_refs):
    for ek in table.entries.keys():
        entry = table.entries[ek]
        for m in missing_refs:
            replace_str = "MISSING_" + str(m)
            if entry[column] == m:
                entry[column] = replace_str



"""
finds issues based off of input data
args    0   the root data_pack directory
args    1   evanKey directory
args    2   directory of the export for testing
args    3   directory of output export
"""
def main(args):
    SEPARATE_LOGS = True
    VERBOSE = False
    if len(args) != 4:
        sys.stderr.write("Error: Usage is python detect_all_issues.py dataPackDirectory evanKeyDirectory modDirectory outputDirectory\n")
        return -1
    LOG = sys.stdout
    root_dir = args[0]
    evanKeyDir = os.path.join(args[1],"db")
    devnull = open(os.devnull,"w")

    input_directory = args[2]
    outputDir = os.path.join(args[3],"db")

    # the dict of all tables in the root directory
    baseDirTables = load_directory_Tables(root_dir)

    # dict of all tables in the test directory
    input_dirTables = load_directory_Tables(input_directory)

    # dict of folder names to a list of schema nodes
    folder_to_nodes_dict = schema_scan(baseDirTables, evanKeyDir, devnull)

    base_folders_to_columndata = dict()
    mod_folders_to_columndata = dict()
    # collect column data for each table
    for folder in baseDirTables.keys():
        try:
            table = baseDirTables[folder]["data__"]
            col_data = get_column_data(table)
            base_folders_to_columndata[folder] = col_data
        except:
            pass
        try:
            tables = input_dirTables[folder]
            mod_folders_to_columndata[folder] = dict()
            for t in tables.keys():
                table = tables[t]
                if table != None:
                    col_data = get_column_data(table)
                    for c in col_data.keys():
                        try:
                            mod_folders_to_columndata[folder][c] |= col_data[c]
                        except KeyError:
                            mod_folders_to_columndata[folder][c] = col_data[c]
        except KeyError:
            pass


    #print mod_folders_to_columndata
    """
    Right now this just finds all missing references in the mod pack, for all ref. columns that were processed with evankey.
        It wouldn't detect an edit to a voice actor for example, as that isn't included in evanKey.
    It also detects issues that might not crash the game at all.
        This also won't detect if the mod contains data_pack, deletes an entry, and something else references it.
    Detects broken columns (and do something about it)
        Marks references as missing and write the tables out somewhere
    """
    # process each folder to find out
    for folder in mod_folders_to_columndata.keys():
        LOG_STRING = ""

        cont = True
        try:
            nodes = folder_to_nodes_dict[folder]
        except KeyError:
            LOG_STRING += ("WARNING: No nodes found for folder " + folder + "\n")
            nodes = []
        try:
            data__ = baseDirTables[folder]["data__"]
        except KeyError:
            LOG_STRING += ("Failed to find data__ file for folder " + folder + "\n")
            cont = False
        # if data__ isn't found, we don't run
        if cont:
            try:
                column_data = base_folders_to_columndata[folder]
            except:
                LOG_STRING += ("Column data unavailable for data_pack folder " + folder +"\n")
                cont = False
        if cont:
            mod_tables = input_dirTables[folder]
            mod_column_data = mod_folders_to_columndata[folder]
            issues_in_folder = False
            FOLDER_STRING = ("Processing folder: \'" + folder + "\' {\n")
            # for each mod table in this folder
            for m_table in mod_tables.keys():
                curr_STRING = ""
                curr_STRING += ("\tProcessing mod table: \'" + folder + "/" + m_table + "\' {\n")
                table = mod_tables[m_table]
                ISSUES_FOUND = False

                # if the table has different columns compared to the data_pack version
                if table.columns != data__.columns:
                    curr_STRING += ("\t\tWARNING: This table has broken columns! This will be resolved in the new export\n")
                    ISSUES_FOUND = True
                    tc = set(table.columns)
                    dc = set(data__.columns)
                    tc_and_dc = tc & dc
                    tc_not_dc = tc - dc
                    dc_not_tc = dc - tc
                    default_col_data = dict() # col --> some default data

                    for old_c in tc_not_dc:
                        curr_STRING += ("\t\t\tRemoving old column: \'" + old_c + "\'. This data will not exist in new table export.\n")
                    for new_c in dc_not_tc:

                        curr_STRING += ("\t\t\tAdding new column: \'" + new_c + "\' with default value \'")

                        for ek in data__.entries.keys():
                            d_val = data__.entries[ek][new_c]
                            default_col_data[new_c] = d_val
                            curr_STRING += (str(d_val) + "\'\n")
                            break

                    table.columns = data__.columns # reset the columns

                    for ek in table.entries.keys():
                        entry = table.entries[ek]
                        for new_c in dc_not_tc:
                            entry[new_c] = default_col_data[new_c]


                node_cols = set()
                # get a list of every node column to reduce the amount of columns to check for soft matching
                for node in nodes:
                    node_cols |= {node.column}

                table_mod_node_coldata = get_column_data(table)
                # do a soft scan in case if any table doesn't have a node to represent its link
                for column in table.columns:
                    # skip any that will be matched later
                    if column not in node_cols:
                        table_data = table_mod_node_coldata[column]
                        base_data = column_data[column]

                        mod_shared_refs = table_data & base_data # the column data shared by the mod and the base data_pack
                        mod_unique_refs = table_data - base_data # mod refs that don't exist in the data pack for that folder
                        still_bad = set()
                        for ref in mod_unique_refs:
                            num = is_number(ref)
                            if num:
                                pass
                            else:
                                still_bad |= {ref}

                        if len(still_bad) > 0:
                            ISSUES_FOUND = True
                            curr_STRING += ("\t\tWARNING some soft match references in column \'" + column + "\' are not found in data.pack: {\n")
                            for s in still_bad:
                                curr_STRING += ("\t\t\t- \'" + s + "\'\n")
                            #replace_missing_refs(table, column, still_bad)
                            #curr_STRING += ("\t\tSoft misses will be replaced with ...MISSING strings in the export files. {\n")
                            curr_STRING += ("\t\t}\n")


                # For each node link, check the table's references
                no_nodes = True
                for node in nodes:
                    column = node.column
                    base_node_data = column_data[column]
                    #mod_node_data = mod_column_data[column]
                    table_node_data = table_mod_node_coldata[column]


                    # do a soft scan, assume

                    if node.type == "ROOT":
                        pass # skip this, if its root then it is only looked up by others, not doing the lookup
                    else:
                        for lnk_node in node.direct_links:
                            if lnk_node.type == "ROOT":
                                no_nodes = False
                                curr_STRING += ("\t\tProcessing table reference: \'" + folder +"/"+column + "\' --> \'" + lnk_node.folder + "/" + lnk_node.column + "\'{\n")
                                base_lnk_node_data = base_folders_to_columndata[lnk_node.folder][lnk_node.column]
                                try:
                                    mod_lnk_node_data = mod_folders_to_columndata[lnk_node.folder][lnk_node.column]
                                except KeyError:
                                    mod_lnk_node_data = set()

                                mod_or_base_lnk_node_data = mod_lnk_node_data | base_lnk_node_data | base_node_data

                                mod_ref_to_base = table_node_data & base_lnk_node_data
                                mod_ref_to_mod = table_node_data & mod_lnk_node_data

                                missing_mod_refs = table_node_data - mod_or_base_lnk_node_data
                                errors = len(missing_mod_refs)

                                # IGNORE THE CASE WHERE THE MISSING REF IS THE EMPTY STRING
                                if errors == 1:
                                    for m in missing_mod_refs:
                                        if m == '':
                                            errors = 0
                                if VERBOSE:
                                    curr_STRING += ("\t\t\tMOD REFS TO BASE (" + str(len(mod_ref_to_base)) + ") {\n")
                                    curr_STRING += print_log_set(mod_ref_to_base,"\t\t\t\t")
                                    curr_STRING += ("\t\t\t}\n")
                                    curr_STRING += ("\t\t\tMOD REFS TO MOD (" + str(len(mod_ref_to_mod)) + "){\n")
                                    curr_STRING += print_log_set(mod_ref_to_mod,"\t\t\t\t")
                                    curr_STRING += ("\t\t\t}\n")
                                if VERBOSE or errors > 0:
                                    curr_STRING += ("\t\t\tMOD MISSING REFS (" + str(errors) + "){\n")
                                    if errors > 0:
                                        ISSUES_FOUND = True
                                        curr_STRING += ("\t\t\t\t" + "WARNING: This mod table contains references to " + str(lnk_node) + " that are not found in either data.pack or the mod.pack\n")
                                        curr_STRING += print_log_set(missing_mod_refs,"\t\t\t\t\t")
                                        curr_STRING += ("\t\t\t\tMissing refs will be replaced with \'MISSING_...\' in the table export.\n")
                                    curr_STRING += ("\t\t\t}\n")
                                    replace_missing_refs(table, column, missing_mod_refs)
                                else:
                                    curr_STRING += ("\t\t\tNo issues detected.\n")
                                curr_STRING += ("\t\t}\n")

                if no_nodes:
                    curr_STRING += ("\t\tNo references needed to be processed\n")

                if ISSUES_FOUND == True:
                    issues_in_folder = True
                    curr_STRING += ("\t\tPrinting this table to the export directory.\n")
                    table.fileName = table.fileName + "_SCANNED"
                    table.print_to_file(os.path.join(outputDir,folder))
                else:
                    curr_STRING += ("\t\tNot printing this table to the export directory.\n")
                curr_STRING += ("\t}\n")

                if VERBOSE or ISSUES_FOUND:
                    FOLDER_STRING += curr_STRING

            FOLDER_STRING += ("}\n")
            FOLDER_STRING += ("-"*100 + "\n")
            if issues_in_folder or VERBOSE:
                LOG_STRING += FOLDER_STRING

                path = os.path.join(outputDir,folder)
                try:
                    os.makedirs(path)
                except:
                    pass
                lower_log = open(os.path.join(path,"log.json"),"w")
                lower_log.write(FOLDER_STRING)
        LOG.write(LOG_STRING)

    #pass



if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
















# EOF
