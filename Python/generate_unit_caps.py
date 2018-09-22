

from table_module import *

import os
import sys

def get_building_level(word):
    if "_1" in word:
        return 1
    elif "_2" in word:
        return 2
    elif "_3" in word:
        return 3
    elif "_4" in word:
        return 4
    elif "_5" in word:
        return 5
    else:
        return -1


"""
args    0   input file holding tsv data about which units to generate caps for
args    1   output directory
args    2   data_pack directory

STEPS:
1) Make cap of the unit 0 in main units
2) Make a new effect in effects_tables
3) Link effect to unit_cap in effects_bonus_value_ids_unit_sets_tables
4) Create a new unit set (for each individual unit or group of units) in unit_sets_tables
5) Link unit sets to units in unit_set_to_unit_junctions_tables
6) Link effect to buildings in building_effets_junction_tables
"""
def main(args):

    if len(args) != 3:
        sys.stderr.write("ERROR: Usage is python generate_unit_caps.py inputFile outputDirectory dataPackDirectory")
        sys.stderr.write("Input file format: unit_group <tab> unit\n")
        return -1
    inputfile = open(args[0],'r')  # unit group \t unit
    outputDir = os.path.join(args[1],"db")
    dataPack = args[2]
    try:
        buildingUnitsAllowed_file = open("Exports/lh_overhaul_2_14_2018/db/building_units_allowed_tables/evan.tsv",'r')
    except:
        sys.stderr.write("Warning: using default building units allowed table from data_pack.tsv\n")
        buildingUnitsAllowed_file = open(os.path.join(dataPack,"db","building_units_allowed_tables","data__.tsv"),'r')

    LOG = sys.stdout
    baseDirTables = load_directory_Tables(dataPack)

    effectTable = copy.deepcopy(baseDirTables["effects_tables"]["data__"])
    effectBonusTable = copy.deepcopy(baseDirTables["effect_bonus_value_ids_unit_sets_tables"]["data__"])
    buldingEffectsTable = copy.deepcopy(baseDirTables["building_effects_junction_tables"]["data__"])
    unitSetsTable = copy.deepcopy(baseDirTables["unit_sets_tables"]["data__"])
    unitSetToUnitsTable = copy.deepcopy(baseDirTables["unit_set_to_unit_junctions_tables"]["data__"])

    base_buildingUnitsAllowedTable = file_loader(buildingUnitsAllowed_file)

    unitsets_to_units = dict()
    unitset_to_effect = dict()

    for line in inputfile:
        lst = parse_line_to_list(line,"\t")
        unitset = lst[0]
        unit = lst[1]
        try:
            unitsets_to_units[unitset].append(unit)
        except:
            unitsets_to_units[unitset] = [unit]
        effect = "unit_cap_" + unitset
        unitset_to_effect[unitset] = effect

    unitsToBuildings = dict()
    # link units to buildings allowing them
    for ek in base_buildingUnitsAllowedTable.entries.keys():
        entry = base_buildingUnitsAllowedTable.entries[ek]
        building = entry["building"]
        unit = entry["unit"]
        try:
            unitsToBuildings[unit] |= {building}
        except:
            unitsToBuildings[unit] = {building}

    ind = 0
    for unitset in unitsets_to_units.keys():
        ind += 1
        units = unitsets_to_units[unitset]
        effect = unitset_to_effect[unitset]
        building_units = set()

        # effects
        effect_entry = {"effect":effect,"icon":"army.png","priority":str(500 + ind),"icon_negative":"army.png","category":"campaign","is_positive_value_good":"True"}
        effectTable.add_entry(effect_entry)

        # effect bonus value ids unit_sets
        effectBonusValue_entry = {"bonus_value_id":"unit_cap","effect":effect,"unit_set":unitset}
        effectBonusTable.add_entry(effectBonusValue_entry)

        # unit sets
        unitSet_entry = {"unknown0":unitset,"unknown1":"False","unknown2":"-1","unknown3":"-1"}
        unitSetsTable.add_entry(unitSet_entry)

        # unit set to units table
        for unit in units:
            unitSet_to_unit_entry = {"exclude":"False","unit_caste":"","unit_category":"","unit_class":"","unit_record":unit,"unit_set":unitset}
            unitSetToUnitsTable.add_entry(unitSet_to_unit_entry)
            try:
                building_units |= unitsToBuildings[unit]
            except KeyError:
                LOG.write("WARNING: No buildings found for unit: " + unit + "\n")


        # building effects
        for building in building_units:
            bl = get_building_level(building)
            val = bl * 2
            building_to_effect_entry = {"building":building,"effect":effect,"effect_scope":"building_to_faction_own","value":str(val),"value_damaged":str(val),"value_ruined":"0"}
            buldingEffectsTable.add_entry(building_to_effect_entry)

    effectTable.fileName= "unit_caps"
    effectBonusTable.fileName= "unit_caps"
    buldingEffectsTable.fileName= "unit_caps"
    unitSetsTable.fileName= "unit_caps"
    unitSetToUnitsTable.fileName= "unit_caps"

    effectTable.print_to_file(outputDir + "/" + effectTable.name)
    effectBonusTable.print_to_file(outputDir + "/" + effectBonusTable.name)
    buldingEffectsTable.print_to_file(outputDir + "/" + buldingEffectsTable.name)
    unitSetsTable.print_to_file(outputDir + "/" + unitSetsTable.name)
    unitSetToUnitsTable.print_to_file(outputDir + "/" + unitSetToUnitsTable.name)







if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))



















# EOF
