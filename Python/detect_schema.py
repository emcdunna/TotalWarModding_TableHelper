from table_module import *

import sys
import os
"""
Loads every table in this directory.
returns a dict of folder name mapped to a list of tables loaded there.
"""
def load_directory_Tables(directory):
    db = os.path.join(directory, "db")
    folders = os.listdir(db)

    dir_tables = {}
    for f in folders:
        path = os.path.join(db,f)
        f_tables = load_folder_Tables(path)
        dir_tables[f] = f_tables
        #print str(f) + "\t" + str(f_tables)

    return dir_tables


"""
returns a dict of column -> set(all possible values)
"""
def get_column_data(table):
    data = {}
    for c in table.columns:
        data[c] = set()

        for ek in table.entries.keys():
            val = table.entries[ek][c]
            data[c] |= {val}
    return data

"""
evaluates two column data sets to determine if they contain the same kind of data (assumedly)
"""
def eval_column_data(col_set_1, col_set_2):
    col_set_1 -= {""}
    col_set_2 -= {""}
    # only check one out of the entire set!
    for d in col_set_1:
        if( is_number(d) == True):
            return "NUMBER_1",0
        elif (is_bool(d)):
            return "BOOL_1",0
        else:
            break
    # only check one out of the entire set!
    for d in col_set_2:
        if( is_number(d) == True):
            return "NUMBER_2",0
        elif (is_bool(d)):
            return "BOOL_2",0
        else:
            break

    shared = col_set_1 & col_set_2
    if ( len(shared) == 0):
        return "DIFFERENT", 0
    elif (len(shared) == len(col_set_1) ): #(col_set_1 == col_set):
        return "SAME", 1
    else:
        d_1not2 = col_set_1 - col_set_2
        d_2not1 = col_set_2 - col_set_1
        if ( len(d_1not2) == 0) and (len(shared) > 0):
            return "SUBSET_1->2", float(len(shared)) / len(col_set_1 | col_set_2)
        elif ( len(d_2not1) == 0) and (len(shared) > 0):
            return "SUBSET_2->1", float(len(shared)) / len(col_set_1 | col_set_2)
        else:
            return "OVERLAP", float(len(shared)) / len(col_set_1 | col_set_2)
    return "ERROR", 0

def is_bool(word):
    if (word.lower() == "false") or (word.lower() == "true"):
        return True
    else:
        return False


unit_dir = "REBASING_MODS/Lorehammer_units2"
dirTables = load_directory_Tables(root_dir)
unit_dirTables = load_directory_Tables(unit_dir)

folder_to_ColumnData = {}
i = 0
folder_set = set(unit_dirTables.keys())

for folder in folder_set:
    #if folder in unit_dirTables.keys():
    tables = dirTables[folder]
    try:
        t = tables["data__"]
        coldata = get_column_data(t)
        folder_to_ColumnData[folder] = coldata
        i += len(coldata)
    except:
        sys.stderr.write("WARNING: Error found for folder " + folder + "\n")

for folder in folder_set:
    tmp_set = folder_set - {folder}
    colData = folder_to_ColumnData[folder]

    for col_1 in colData.keys(): # col data is a dict of column name to set of all values it has
        values_1 = colData[col_1]
        fnd_same = False
        for o_folder in tmp_set: # for every other folder

            o_colData = folder_to_ColumnData[o_folder]


            for col_2 in o_colData.keys():
                values_2 = o_colData[col_2]

                result, overlap_percent = eval_column_data(values_1,values_2)
                if result == "NUMBER_1":
                    fnd_same = True
                elif result == "NUMBER_2":
                    pass
                elif result == "DIFFERENT":
                    pass
                elif result == "BOOL_1":
                    fnd_same = True
                elif result == "BOOL_2":
                    pass
                else:
                    fnd_same = True
                    print folder + "[" + col_1 + "] --> " + o_folder + "[" + col_2 + "]\t" + result  + " " + str(overlap_percent)
        if fnd_same == False:
            pass
            #print "Never found SAME for " + folder + "[" + col_1 + "]"
        sys.stdout.flush()


# TODO: pick only the best matches, based on size of overlaps

# TODO: Organize these somehow and return it



































# EOF
