from table_module import *
import sys
import os
import datetime

"""

"""
def main(args):
    if len(args) != 2:
        sys.stderr.write("Error!\nUsage is \'python detect_renamed_columns.py oldBaseDir newBaseDir\'\n")

        return -1
    else:
        LOG = sys.stderr

        oldBaseDir = os.path.join(args[0],"db")
        newBaseDir = os.path.join(args[1],"db")

        detect_renamed_columns(oldBaseDir, newBaseDir, LOG)


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))