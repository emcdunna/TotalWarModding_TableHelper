from table_module import *
import sys
import os
import itertools
import datetime


"""
This is a script to evaluate a table and detect the column(s) that act as the key for that table.
Keys are unique identifiers that allow tables to be overwritten.
In PFM, the "key" (or keys) is the column highlighted in yellow and moved to the left (by default)
We need to know which column is the key in order to evaluate differences.
"""

"""
detects if a column of data is composed only of unique identifiers
"""
def detect_uniqueness(column):
    already_checked = set()
    for c in column:
        if c in already_checked:
            return False
        already_checked |= {c}
    return True

"""
detects if a column of data is composed only of unique identifiers
"""
def detect_uniqueness_group(column1,column2):
    already_checked = set()
    for ind in range(len(column1)):
        c = column1[ind] + "_WITH_" + column2[ind]
        if c in already_checked:
            return False
        already_checked |= {c}
    return True


"""
table_list will hold a list of lists, where list_of_lists[row][column] denotes an individual value
in the table.
The reason why we don't usually evaluate tables this way is that it is much more difficult to index
entries and evaluate differences.
"""
def eval_table_list(table_list):
    folder = table_list[0][0]
    columns = table_list[2]
    data = table_list[3:]

    column_indices = dict() # dict to point to which column number a column will have
    column_data = [] # column data will be a list of tuples with (column name, [row1 data, row2 data,...])
    num_keys = 0
    key = None
    ki = 0
    keyIndex = None
    warning= ""
    for c in columns:
        column_indices[c] = ki
        if "key" in c.lower():
            num_keys +=1
            keyIndex = ki
        ki += 1
        column_data.append( (c,[]) )

    for dlist in data:
        j = 0
        for col in dlist:
            column_data[j][1].append(col) # append a column data entry to the corresponding list
            j+=1

    # if one and only one column name contains "key", assume its the key column
    if num_keys == 1:
        res = detect_uniqueness(column_data[keyIndex][1])
        if(res == True):
            key = column_data[keyIndex][0]
            return [key], warning
        else:
            warning = "# \'key\' column is not unique"
            #sys.stderr.write("WARNING: " + str(folder) + " has a \'key\' column but it is not unique.\n")

    key = None
    unique_columns = []
    for coldata in column_data:
        res = detect_uniqueness(coldata[1])
        if res == True:
            unique_columns.append(coldata[0])
    if len(unique_columns) == 0:
        warning = "# has no unique columns, will check column groups instead"
        #sys.stderr.write("WARNING: " + str(folder) + " has no unique columns!\n")
        itools = itertools.combinations(columns,2)
        col_groups = list(itools) # a list of tuples, like [(A,B),(B,C),(C,A)] if unique columns had [A,B,C]
        #print "col_groups " + str(col_groups)
        unique_column_groups = []
        for cg in col_groups:
            ci_1 = column_indices[cg[0]] # column index of the first column in the tuple
            ci_2 = column_indices[cg[1]] # same, for the second column
            result = detect_uniqueness_group(column_data[ci_1][1], column_data[ci_2][1])
            if result == True:
                for c in cg:
                    unique_column_groups.append(c)
            #print str(cg) + " " + str(result)
        if len(unique_column_groups) >= 1:
            return unique_column_groups, warning
        else:
            return [None], "# has no unique columns or column groups!"
    elif len(unique_columns) == 1:
        key = unique_columns[0]
        return [key], warning
    else:
        #sys.stderr.write("WARNING: " + str(folder) + " has too many unique columns!\n")
        warning = "# Too many unique columns, will use them all"
        return unique_columns, warning


"""
Given a file, load it into a list of lists where [row][column] would access one item
"""
def load_table_list(table_file):
    table_list = []

    for line in table_file:
        if "\t" in line:
            sep = "\t"
        else:
            sep = ","
        lst = parse_line_to_list(line,sep)
        table_list.append(lst)
    return table_list

# TODO make this work with multiple input files
def find_key(file_path):
    table_file = open(file_path,'r')

    table_list = load_table_list(table_file)
    result = eval_table_list(table_list)
    return result


"""
Open the folder directory, and for each folder, evaluate the table files.

For this evaluation, we will not sort the table into a dict of dicts. Instead, we will
evaluate it a simple list of lists, looking for uniqueness.
"""
def main(args):
    sys.stderr.write("WARNING: Only run this on an export of the DB directory for CA's data.pack, not a directory exported by a mod.\n------\n")
    output_file = open("Python/warhammer2_table_config_NEW.py",'w')
    if len(args) != 1:
        sys.stderr.write("Error: Invalid number of arguments. \n")
        sys.stderr.write("Usage: python find_keys.py <baseDirectory>\n")
        sys.stderr.write("Directory structure should be \'db/main_units_tables/data__.tsv\' for example/\n")
    else:

        table_dir = os.path.join(args[0], "db")

        db_folders = os.listdir(table_dir)
        output_file.write( "# UPDATED AT: " + str(datetime.datetime.now()) + "\n")
        output_file.write( "keyDict = {" + "\n")
        for folder in db_folders:
            folder_files = os.listdir(os.path.join(table_dir,folder))
            pick_file = None

            # now this will run once for every file in the table.
            for f in folder_files:
                if ".tsv" == f[-4:]:
                    if pick_file != None:
                        sys.stderr.write("!!! WARNING: Ignoring older TSV file " + str(pick_file) + " for " + folder + "\n")
                    pick_file = f
                    file_path = os.path.join(table_dir,folder,pick_file)
                    file_key, warning = find_key(file_path)

            if pick_file == None:
                sys.stderr.write("WARNING: No tsv files found in folder " + str(folder) + "\n")
                file_key = [None]
                warning = "# NO TSV FILES FOUND IN FOLDER"
            output_file.write( "\"" + folder + "\": "  + str(file_key) + ", " + str(warning) + "\n")

        output_file.write("}\n#END OF FILE\n")


if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))














#EOF
