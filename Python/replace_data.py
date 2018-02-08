import sys
import os
from table_module import *

"""
creates new units in tables automatically with minimal input by copy pasting similar entries
args    0   the root data_pack directory
args    1   evanKey directory
args    2   output directory for the result tables to be written to
args    3   replace data file formatted as TSV, where data is stored as -->folder\tcolumn\tbaseVal\treplaceVal
"""
def main(args):
    LOG = sys.stdout
    root_dir = args[0]
    evanKeyDir = os.path.join(args[1],"db")
    outputDir = os.path.join(args[2],"db")
    devnull = open(os.devnull,"w")
    already_done_set = set() # set of ALL combos of folder / column / base val that have already been done

    replaceDataFile = open(args[3],'r')
    replaceData = dict()
    for line in replaceDataFile:
        lst = parse_line_to_list(line,"\t")
        if len(lst) == 5 and lst[3] != "" and lst[4] != "":
            rep_id = (lst[0],lst[1],lst[2],lst[3])

            if rep_id in already_done_set:
                LOG.write("WARNING: Replace parameters " + str(rep_id) + " has already been used! ")
                LOG.write("SKIPPING THIS TO AVOID ERRORS\n")
            else:
                try:
                    replaceData[lst[0]].append(lst[1:])
                except:
                    replaceData[lst[0]] = [lst[1:]]
                already_done_set |= {rep_id}
        else:
            LOG.write("IGNORING REPLACE DATA LINE: " + line)
    if len(replaceData) == 0:
        sys.stderr.write("ERROR: No valid replace data!\n")
        return -1

    # the dict of all tables in the root directory
    baseDirTables = load_directory_Tables(root_dir)

    # dict of folder names to a list of schema nodes
    folder_to_nodes_dict = schema_scan(baseDirTables, evanKeyDir, devnull)

    modDirTables = None
    for keyIndex in replaceData.keys():
        LOG.write("-"*200 + "\n")
        LOG.write("Processing keyIndex " + str(keyIndex) + "\n")
        currDirTables = copy.deepcopy(baseDirTables)
        currData = replaceData[keyIndex]
        replace_data(currData, currDirTables, folder_to_nodes_dict, LOG)

        for folder in currDirTables.keys():
            tables = currDirTables[folder]
            for tk in tables.keys():
                try:
                    table = tables[tk]
                    table.fileName = "data_" + str(keyIndex)
                except:
                    pass
        print_unique_tables(baseDirTables, currDirTables, LOG, outputDir)
        """if modDirTables == None:
            modDirTables = currDirTables
            LOG.write("Set modDirTables at keyIndex " + str(keyIndex) + "\n")
        else:
            currDirTables = unique_dirTables(baseDirTables, currDirTables, LOG)
            modDirTables = merge_dirTables(modDirTables, currDirTables, LOG)
            LOG.write("Merged modDirTables at keyIndex " + str(keyIndex) + "\n")"""



    LOG.write("-"*200 + "\n")

    # END LOOP



if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
