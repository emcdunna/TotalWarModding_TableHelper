from table_module import *
import copy



"""
creates new units in tables automatically with minimal input by copy pasting similar entries
args    0   the root data_pack directory
args    1   evanKey directory
args    2   output directory for the result tables to be written to
args    3   units file storing unit data in a special tsv format
"""
def main(args):
    LOG = sys.stdout
    root_dir = args[0]
    evanKeyDir = os.path.join(args[1],"db")
    outputDir = os.path.join(args[2],"db")

    units_file = open(args[3],'r')

    # the dict of all tables in the root directory
    baseDirTables = load_directory_Tables(root_dir)
    modDirTables = copy.deepcopy(baseDirTables)

    # dict of folder names to a list of schema nodes
    folder_to_nodes_dict = schema_scan(modDirTables, evanKeyDir, LOG)

    LOG.write("STARTING CREATE_UNITS MAIN PROCESS\n")
    sys.stderr.flush()

    # for every necessary root folder

    # END LOOP
    print_unique_tables(baseDirTables, modDirTables, LOG, outputDir)


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))


















# EOF
