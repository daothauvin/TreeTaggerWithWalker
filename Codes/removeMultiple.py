"""
@arg1 bar : input file name
@arg2 foo : output file name
This program opens file bar and merge ligns with same word at the beginning and writes the
contents to foo file.
nom and vers form :
word\ttag
"""

import sys

inf = sys.argv[1]
of = sys.argv[2]
prec = []
prev = 0
word = []
tab = []
outfile = open(of, "w")
infile = open(inf, "r")
texte = infile.read()
for line in texte.split("\n"):
    ens = line.split("\t")
    if ens[0] not in word:  # not a duplicate
        word.append(ens[0])
        prec.append(ens[1:])
        tab.append([line])
    else:
        pos=word.index(ens[0])
        for el in ens[1:]:
            if (el==word[pos] and prev==0) or (el!=word[pos] and el not in prec[pos]):
                tab[pos].append("\t")
                tab[pos].append(el)
            else:
                if el!=word[pos]:
                    prev=1
                else:
                    prev=0
            prec[pos].append(el)
        
for line in tab:
    for word in line:
        outfile.write(word)
    outfile.write("\n")
    
outfile.close()
infile.close()

