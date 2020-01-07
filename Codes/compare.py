
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:23:39 2019

@author: Dao
@arg1 fich1 : file to look
@arg2 fich2 : file to look
Give differences between tags from fich1 and fich2, 
first print gives the count tags from fich1 that do not correspond to fich2 and secondly do the opposite
fich1 and fich2 form :
word\ttag
...
"""


import sys

fich1 = sys.argv[1]
fich2 = sys.argv[2]

tab1 = []
tab2 = []

fichier1 = open(fich1,'r', encoding='utf8')
fichier2 = open(fich2,'r', encoding='utf8')
texte1 = fichier1.read()
texte2 = fichier2.read()
fichier1.close()
fichier2.close()

for ligne in texte1.split("\n") :
    ens = ligne.split("\t")
    if len(ens)>1 :
        tab1.append(ens[1])

for ligne in texte2.split("\n") :
    ens = ligne.split("\t")
    if len(ens)>1 :
        tab2.append(ens[1])

total = 0

dico1 = dict()
dico2 = dict()
for i in range(0,len(tab1)) :
    a = tab1[i]
    b = tab2[i]
    if a!=b :
        total = total + 1
        if a in dico1 :
            dico1[a]=dico1[a]+1
        else :
            dico1[a]=1
        if b in dico2 :
            dico2[b]=dico2[b]+1
        else :
            dico2[b]=1
    
    

sorted(dico1.items(), key=lambda t: t[0])
sorted(dico2.items(), key=lambda t: t[0])

print("not good in file 1 (should not been)")  
for cle, valeur in dico1.items():
    print(cle)
    print(valeur)
    
print("not good in file 2 (should not been)") 
for cle, valeur in dico2.items():
    print(cle)
    print(valeur) 
        
"""
result = open(vers,'w', encoding='utf8')
for text in tab :
    result.write(text)
    result.write("\n")
result.close()
"""
print(total)