"""
@arg1 bar : input file name
@arg2 foo : output file name
This program opens file bar and removes duplicate lines and writes the
contents to foo file.
"""

import sys

inf = sys.argv[1]
of = sys.argv[2]

lines_seen = set()  # holds lines already seen
outfile = open(of, "w")
infile = open(inf, "r")
print ("The file bar is as follows")
for line in infile:
    print(line)
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print ("The file foo is as follows")
for line in open(of, "r"):
    print (line)
