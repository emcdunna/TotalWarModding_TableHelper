

building_level_to_chain_file = open("building_level_to_chain.txt","r")
building_level_to_effect_file = open("building_level_to_effect.txt","r")


"""
Takes in list of strings, returns a line with strings separated by a "sep" character
"""
def stringify_list(lst):
    sep = "\t"
    line = ""
    j = 0
    for i in lst:
        j+=1
        line += i
        if (j < len(lst)):
            line += sep
    return line

"""
Takes in string line and separator character
returns lst of items
"""
def parse_line_to_list(line):
    lst = []
    word = ""
    sep = "\t"
    for i in line:
        if (i == sep) | (i == "\n") | (i == "\r"):
            lst.append(word)
            word = ""
        else:
            word += i
    if word != "":
        lst.append(word)
    return lst

bl_to_chains = dict()
bl_to_effects = dict()
bleffect_to_value = dict()
bchain_to_effects = dict()
bchaintier_to_bl = dict()
bchain_to_bl = dict()
bl_to_tier = dict()

for line in building_level_to_chain_file:
    lst = parse_line_to_list(line)
    bl_to_chains[lst[0]] = lst[1]
    bl_to_effects[lst[0]] = set()
    bchain_to_effects[lst[1]] = set()
    bl_to_tier[lst[0]] = lst[2]
    bchaintier_to_bl[(lst[1],lst[2])] = lst[0]

bls = bl_to_chains.keys()
chains = bchain_to_effects.keys()
for c in chains:
    bchain_to_bl[c] = set()

for bl in bls:
    chain = bl_to_chains[bl]
    bchain_to_bl[chain] |= {bl}



for line in building_level_to_effect_file:
    lst = parse_line_to_list(line)
    bl_to_effects[lst[0]] |= {lst[1]}
    bleffect_to_value[(lst[0],lst[1])] = lst[2:]

    chain = bl_to_chains[lst[0]]
    bchain_to_effects[chain] |= {lst[1]}

def get_effect_type(effect):
    xp_effect = "effect_agent_recruitment_xp"
    enable_effect = "effect_agent_enable_recruitment"
    cap_effect = "effect_agent_cap_increase"

    if xp_effect in effect:
        return "XP"
    if enable_effect in effect:
        return "ENABLE"
    if cap_effect in effect:
        return "CAP"
    return "OTHER"


new_bl_effects = []
for chain in chains:

    effects = bchain_to_effects[chain]
    builds = bchain_to_bl[chain]

    for e in effects:
        t = get_effect_type(e)
        values = None
        scope = None
        if t == "XP":
            values = [3,6,9,9,9]
            scope = "province_to_province_own"
        elif t == "ENABLE":
            values = [1,1,1,1,1]
            scope = "province_to_province_own"
        elif t == "CAP":
            values = [1,2,3,4,5]
            scope = "faction_to_faction_own_unseen"
        if (values != None) and (scope != None):

            for b in builds:
                tier = int(bl_to_tier[b])
                if tier in range(5):

                    new_lst = [b,e,scope,str(values[tier]),str(values[tier]),"0"]
                    new_bl_effects.append(new_lst)
                else:
                    print "bad tier " + str(tier) + " for " + b + ". Using default 0."

                    new_lst = [b,e,scope,str(values[0]),str(values[0]),"0"]
                    new_bl_effects.append(new_lst)

outputfile = open("agent_building_effects.tsv",'w')

for lst in new_bl_effects:
    outputfile.write(stringify_list(lst) + "\n")




































# EOF
