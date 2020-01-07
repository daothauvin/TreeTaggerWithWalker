
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:23:39 2019

@author: Dao
@arg1 nom : file to look
@arg2 vers : file to write
@arg3 sep : separator
Write in the file vers the text between <sep> and </sep> lign by lign
Used on Walker's dictionnary
"""


import sys


"""
delete forget's content in phrase
"""
def change(phrase) :
    #forget = ['<emph rend="italic">','</emph>','<xr type="entry">','</xr>','-','[Lat.]']
    forget = ['<emph rend="italic">','</emph>','To ',',']
    #forget = []
    for mot in forget :
        phrase=phrase.replace(mot,"")
    return phrase

nom = sys.argv[1]
vers = sys.argv[2]
sep = sys.argv[3]
tab = []

fichier = open(nom,'r', encoding='utf8')
texte = fichier.read()
for ligne in texte.split("\n") :
    ligne = change(ligne)
    if ("<pos>" not in ligne or "</pos>" not in ligne or "<pos></pos>" in ligne):
        
    
        ens = ligne.split("<"+sep+">")
        if len(ens)>1 :
            mot = ens[1].split("</"+sep+">") 
            if len(mot[0].strip()) != 0:
                tab.append(mot[0])

fichier.close()

result = open(vers,'w', encoding='utf8')
for text in tab :
    result.write(text)
    result.write("\n")
result.close()

