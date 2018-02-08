import sys
import os
from table_module import *

"""
finds links based off of input data
args    0   the root data_pack directory
args    1   evanKey directory
args    2   input data file formatted as TSV, where data is stored as -->folder\tcolumn\trootValue
"""
def main(args):
    LOG = sys.stdout
    root_dir = args[0]
    evanKeyDir = os.path.join(args[1],"db")
    devnull = open(os.devnull,"w")

    inputDataFile = open(args[2], "r")
    inputData = []
    for line in inputDataFile:
        lst = parse_line_to_list(line,"\t")
        if len(lst) == 3:
            inputData.append(lst)
        else:
            LOG.write("IGNORING DATA LINE: " + line)
    if len(inputData) == 0:
        sys.stderr.write("ERROR: No valid data links!\n")
        return -1

    # the dict of all tables in the root directory
    dirTables = load_directory_Tables(root_dir)

    # dict of folder names to a list of schema nodes
    folder_to_nodes_dict = schema_scan(dirTables, evanKeyDir, devnull)

    for data in inputData:
        folder = data[0]
        column = data[1]
        value = data[2]
        nodes = folder_to_nodes_dict[folder]

        node = None
        for nd in nodes:
            if nd.column == column:
                node = nd
        if node == None:
            LOG.write("ERROR: Couldn't find node matching \'" + folder + "/"  + column + "\'\n")
        else:
            result = find_data_links(dirTables, node, value, LOG, set())
            


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))
















# EOF
