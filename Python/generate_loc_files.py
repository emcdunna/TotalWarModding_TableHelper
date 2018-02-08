from table_module import *
import sys
import os

input_file = open("effects_strings.txt","r")
for line in input_file:
    lst = parse_line_to_list(line, "\t")
    effect = lst[0]
    word = lst[1]

    print "\"effects_description_" + effect + "\"\t\"Capacity: %\+n " + word + "\"\t\"True\""
