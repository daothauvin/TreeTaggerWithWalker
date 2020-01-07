# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:20:16 2019

@author: Dao
@arg1: name file 1
@arg2: name file 2
@arg3: name result file, contains every lign of file 1 and file 2 two by two separate with \t
"""

nom1 = sys.argv[1]
nom2 = sys.argv[2]
res = sys.argv[3]
part1 = []
part2 = []

fich1 = open(nom1,'r', encoding='utf8')
texte = fich1.read()
part1=texte.split("\n")
fich1.close()

fich2 = open(nom2,'r', encoding='utf8')
texte = fich2.read()
part2=texte.split("\n")
fich2.close()

fich3 = open(res,'w', encoding='utf8')
for i in range(0,len(part1)) :
    fich3.write(part1[i]);
    if i<len(part2) :
        fich3.write("\t"+part2[i])
    fich3.write("\n")
fich3.close()
    

    