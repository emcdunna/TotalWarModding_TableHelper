

import table_module
import sys

buildunits_file = open("building_units.txt",'r')
keyset = set()
for line in buildunits_file:
    lst = table_module.parse_line_to_list(line,"\t")
    key = lst[3]
    if key in keyset:
        print "Issue with line: " + lst[3]
    else:
        keyset |= {key}
