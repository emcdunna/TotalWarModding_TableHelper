from table_module import *

folder = "Buildings_heroes"

effects_file = open(folder + "/enable_effects.txt",'r')
effects_set = set()
effects_dict = {}
for line in effects_file:
     lst = parse_line_to_list(line, "\t")
     effects_dict[lst[0]] = lst[0] + "\t" +lst[1] + "\t" +lst[2] + "\t" +lst[3] + "\t" +lst[4]
     effects_set |= {lst[0]}

buildings_file = open(folder + "/settlements.txt",'r')
buildings_set = set()
for line in buildings_file:
    lst = parse_line_to_list(line, "\t")
    buildings_set |= {lst[0]}

empire = [{'empire','emp','teb','kislev'},set(),set()]
dwarfs = [{'dwf','dwar','runesmith','engineer'},set(),set()]
asrai = [{'wef','wood_el','woodelves'},set(),set()]
asur = [{'hef','high_el','highelves'},set(),set()]
skaven = [{'skaven','skv','hellpit'},set(),set()]
chaos = [{'chs','chaos'},set(),set()]
greens = [{'greenskin','orc','goblin','grn','savage'},set(),set()]
druchii = [{'def','dark_el','darkelves','naggarond'},set(),set()]
vampires = [{'vmp','vampire_count'},set(),set()]
beastmen = [{'bst','beastmen'},set(),set()]
lizardmen = [{'lzd','lizardmen','itza','hexoatl'},set(),set()]
bretonnia = [{'brt','breton'},set(),set()]
norsca = [{'norsca','nor'},set(),set()]
other = [{'other','rogue'},set(),set()]
group = [empire,dwarfs,asrai,asur,skaven,chaos,greens,druchii,vampires,beastmen,lizardmen,bretonnia,norsca,other]

claimed_buildings = set()
claimed_effects = set()
for build in buildings_set:
    for race in group:
        for key in race[0]:
            if key in build:
                race[1] |= {build}
                claimed_buildings |= {build}

for effect in effects_set:
    for race in group:
        for key in race[0]:
            if key in effect:
                race[2] |= {effect}
                claimed_effects |= {effect}

unclaimed_buildings = buildings_set - claimed_buildings
unclaimed_effects = effects_set - claimed_effects

sys.stderr.write("Unclaimed buildings: \n")
for uc in unclaimed_buildings:
    sys.stderr.write(uc +"\n")
sys.stderr.write("Unclaimed effects: \n")
for uc in unclaimed_effects:
    sys.stderr.write(uc +"\n")


for race in group:
    builds = race[1]
    effects = race[2]
    for b in builds:
        for e in effects:
            sys.stdout.write(b + "\t" + effects_dict[e] + "\n")
