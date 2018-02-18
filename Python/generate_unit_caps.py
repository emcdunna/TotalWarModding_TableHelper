

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
args    3   building_units_allowed_file determines which set of unit recruitment buildings gets used

STEPS:
1) Make cap of the unit 0 in main units
2) Make a new effect in effects_tables
3) Link effect to unit_cap in effects_bonus_value_ids_unit_sets_tables
4) Create a new unit set (for each individual unit or group of units) in unit_sets_tables
5) Link unit sets to units in unit_set_to_unit_junctions_tables
6) Link effect to buildings in building_effets_junction_tables
"""
def main(args):

    inputfile = open(args[0],'r')  # unit group \t unit
    outputDir = os.path.join(args[1],"db")
    dataPack = args[2]
    try:
        os.makedirs(os.path.join(args[1],"text"))
    except:
        pass

    unitstrings_loc = open(os.path.join(args[1],"text","effects.loc.tsv"),'w')
    LOG = sys.stdout
    baseDirTables = load_directory_Tables(dataPack)
    try:
        buildingUnitsAllowed_file = open(args[3],'r')
        base_buildingUnitsAllowedTable = file_loader(buildingUnitsAllowed_file)
    except:
        LOG.write("WARNING: Using default building_units_allowed_file\n")
        base_buildingUnitsAllowedTable = baseDirTables["building_units_allowed_tables"]["data__"]

    effectTable = copy.deepcopy(baseDirTables["effects_tables"]["data__"])
    effectBonusTable = copy.deepcopy(baseDirTables["effect_bonus_value_ids_unit_sets_tables"]["data__"])
    buldingEffectsTable = copy.deepcopy(baseDirTables["building_effects_junction_tables"]["data__"])
    unitSetsTable = copy.deepcopy(baseDirTables["unit_sets_tables"]["data__"])
    unitSetToUnitsTable = copy.deepcopy(baseDirTables["unit_set_to_unit_junctions_tables"]["data__"])

    unitsets_to_units = dict()
    unitset_to_effect = dict()
    unitset_to_unitstring = dict()
    for line in inputfile:
        lst = parse_line_to_list(line,"\t")
        unitset = lst[0]
        unit = lst[1]
        try:
            unitstring = lst[2]

        except:
            unitstring = ""


        if unitstring != "":
            unitset_to_unitstring[unitset] = unitstring
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
        try:
            unitstring = unitset_to_unitstring[unitset]
        except:
            unitstring = ""

        # We assume this is an already made unit set and doesnt need unit set entry or an effect
        if unitstring != "":
            unitstrings_loc.write("\"effects_description_" + effect + "\"\t\"Capacity: %\+n " + unitstring + "\"\t\"True\"\n")
            # effects
            effect_entry = {"effect":effect,"icon":"army.png","priority":str(500 + ind),"icon_negative":"army.png","category":"campaign","is_positive_value_good":"True"}
            effectTable.add_entry(effect_entry)

            # effect bonus value ids unit_sets
            effectBonusValue_entry = {"bonus_value_id":"unit_cap","effect":effect,"unit_set":unitset}
            effectBonusTable.add_entry(effectBonusValue_entry)

            # unit sets
            unitSet_entry = {"unknown0":unitset,"unknown1":"False","unknown2":"-1","unknown3":"-1"}
            unitSetsTable.add_entry(unitSet_entry)


        building_units = set()
        # unit set to units table
        for unit in units:
            unitSet_to_unit_entry = {"exclude":"False","unit_caste":"","unit_category":"","unit_class":"","unit_record":unit,"unit_set":unitset}
            unitSetToUnitsTable.add_entry(unitSet_to_unit_entry)
            try:
                building_units |= unitsToBuildings[unit]
            except KeyError:
                LOG.write("WARNING: No buildings found for unit: " + unit + "\n")

        # building effects
        if (unit_string != ""):
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
