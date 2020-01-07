
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:23:39 2019

@author: Dao
@arg1 nom : file to look
@arg2 vers : file to write
Count tags occurence
"""


import sys

nom = sys.argv[1]
vers = sys.argv[2]

tab = []

fichier = open(nom,'r', encoding='utf8')
texte = fichier.read()
for ligne in texte.split("\n") :
    ens = ligne.split("\t")
    if len(ens)>1 :
        tab.append(ens[1])

fichier.close()

dico = dict()
for tag in tab :
    if tag in dico :
        dico[tag]=dico[tag]+1
    else :
        dico[tag]=1

sorted(dico.items(), key=lambda t: t[0])

for cle, valeur in dico.items():
    print(cle)
    print(valeur)
        
"""
result = open(vers,'w', encoding='utf8')
for text in tab :
    result.write(text)
    result.write("\n")
result.close()
"""
