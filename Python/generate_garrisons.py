import table_module
import sys

chain_file = open("D:/Lorehammer2/garrisons/chains.txt","r")
chain_to_building_file = open("D:/Lorehammer2/garrisons/chain_to_building_level.tsv","r")
units_races_file = open("D:/Lorehammer2/garrisons/settlement_garrisons.txt","r")
data_garrisons = open("D:/Lorehammer2/Exports/data_pack_12_22_17/db/building_level_armed_citizenry_junctions_tables/data__.tsv","r")

new_data_garrisons = open("D:/Lorehammer2/garrisons/new_data__.tsv",'w')
settlement_file = open("D:/Lorehammer2/garrisons/new_settlement_garrisons.tsv",'w')
num_map = [4,2,3,1,1]

#minor_map = [4,3,3,1,1]

#ignore_buildings = {"altdorf","black_crag","drakenhof","couronne","karaz_a_karak"}
file_header = """building_level_armed_citizenry_junctions_tables
1
building_level	id	unknown3	unit_group
"""

def read_tsv(line):
    word = ""
    lst = []
    for i in line:
        if i == "\t":
            lst.append(word)
            word = ""
        elif i == "\n":
            if len(word)>0:
                lst.append(word)
            return lst
        else:
            word += i
    return lst

chains_to_buildings = dict()
for line in chain_file:
    lst = read_tsv(line)
    chains_to_buildings[lst[0]] = set()

for line in chain_to_building_file:
    lst = read_tsv(line)
    chains_to_buildings[lst[0]] |= {lst[1]}

faction_units = dict()
for line in units_races_file:
    lst = read_tsv(line)
    faction_units[lst[0]] = lst[1:]
settlement_file.write( file_header)
done_buildings = set()
index = 0
for chain in chains_to_buildings.keys():

    # each building in that chain
    for building in chains_to_buildings[chain]:
        # its a settlement or outpost
        if (("settlement" in chain) or ("outpost" in chain) and ( (not "savage" in chain) and (not "rogue" in chain) and not ("_nor_" in chain) and not ("_other_" in chain)) ):
            done = False
            for faction in faction_units.keys():

                s = "_" + faction.lower()
                if (s in building) and ("ruin" not in building) and ("horde" not in building):
                    k = 0
                    # each unit in that faction's list
                    for unit in faction_units[faction]:
                        # more than one of each unit
                        for j in range(num_map[k]):
                            settlement_file.write( building + "\t" + str(index) + "\t0\t" + unit + "\n")
                            index +=1
                        k += 1
                    done = True
                    done_buildings |= {building}
            if done == False:
                faction = "NONE"
                if ("ruin" not in building) and ("horde" not in building):
                    if "_hexoatl_" in building or "_itza_" in building:
                        faction = "LZD"
                    elif "naggarond" in building:
                        faction = "DEF"
                    elif "_lothern_" in building:
                        faction = "HEF"
                    elif "skavenblight" in building or "hellpit" in building:
                        faction = "SKV"
                    else:
                        sys.stderr.write("Failed to identify faction for " + str(building) + "\n")
                        break
                    k = 0
                    # each unit in that faction's list
                    for unit in faction_units[faction]:
                        # more than one of each unit
                        for j in range(num_map[k]):
                            settlement_file.write( building + "\t" + str(index) + "\t0\t" + unit + "\n")
                            index +=1
                        k += 1
                    done = True
                    done_buildings |= {building}

        elif ("defence" in chain) or ("garrison" in chain) or ("wall" in chain):
            done = False
            for faction in faction_units.keys():

                s = "_" + faction.lower()
                if (s in building) and (done == False) and ("ruin" not in building) and ("horde" not in building):
                    k = 0
                    unit = faction_units[faction][0]
                    for k in range(2):
                        settlement_file.write( building + "\t" + str(index) + "\t0\t" + unit + "\n")
                        index +=1
                    k = 0
                    unit = faction_units[faction][2]
                    for k in range(2):
                        settlement_file.write( building + "\t" + str(index) + "\t0\t" + unit + "\n")
                        index +=1


                    done_buildings |= {building}

base_garrisons_table = table_module.file_loader(data_garrisons)

for ek in base_garrisons_table.entries.keys():
    entry = base_garrisons_table.entries[ek]
    if entry["building_level"] in done_buildings:
        #print entry["building_level"]
        del base_garrisons_table.entries[ek]

new_data_garrisons.write(base_garrisons_table.get_fileprint_string())
