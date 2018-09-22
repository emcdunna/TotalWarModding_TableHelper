from table_module import *

land_table = file_loader(open("../DL1/land_units_tables - dl1.tsv",'r'),None)
melee_table = file_loader(open("../DL1/melee_weapons_tables - dl1.tsv",'r'),None)

o_file = open("../melee_weapons.tsv",'w')

for mw in melee_table.entries.keys():

    for lu in land_table.entries.keys():
        lu_entry = land_table.entries[lu]
        l_mw = lu_entry["primary_melee_weapon"]
        if mw == l_mw:
            o_file.write( melee_table.stringify_entry(mw) + "\t" + lu_entry["category"] + "\t" + lu_entry["class"] + "\n")
