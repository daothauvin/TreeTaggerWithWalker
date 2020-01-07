# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:23:39 2019

@author: Dao
@arg1 nom : file to look
@arg2 vers : file to write
mapping of the Walker's dictionnary's tags to our tags
nom and vers form :
word\ttag
...
"""


import sys

nom = sys.argv[1]
vers = sys.argv[2]
tab = []
mapping = {
        " THE first letter of the alphabet,":"art.", #ok
        "s.":"s.", #ok
        "adv.":"adv.", #ok
        "v. a.":"v.", #ok
        "v. n.":"v.", #ok
        "adj.":"adj.", #ok
        "prep.":"prep.", #ok
        "interj.":"interj.", #not found
        "conj.":"conj.", #ok
        "first person":"v.", #not found
        "art.":"art.", #ok
        "pret.":"pret.", #ok
        "part.":"part.", #ok
        "part. pass.":"part.pass.", #ok
        "irreg. pret.":"pret.", #ok?
        "pret. imperfect.":"pret.", #ok?
        "part. adv.":"part. adv.", #ok : double
        "particle.":"particle.", #ok
        "second person":"sp", #ok
        "thrid person":"tp", #ok
        "pron.":"pron.",#ok
        "oblique case":"pron.", #not_found
        "pron. poss.":"pron.poss.", #ok
        "pron. pers.":"pron.pers.", #ok
        "A negative or privative termination.":"NAN", #ok
        "impersonal. verb.":"v.", #ok?
        "verb imperfect.":"v.", #ok?
        "v. defective.":"v.", #ok?
        "contraction.":"NAN", #ok
        "pron. dem.":"pron.", #ok?
        "pron. rel.":"pron.", #ok
        "conjunct.":"conj.", #ok
        "article.":"art.", #ok
        "pron. reciprocal.":"pron.", #ok?
        "An adverbial form of speech.":"adv.", #ok
        "plural. pret.":"pret.", #ok?
        "v.":"v.", #ok
        "accusative.":"pron.", #not_found
        "genitive.":"pron.", #not_found
        "solemn nominative plural.":"NAN", #ok
        "part. adj.":"part. adj.", #ok : double
        "pret. part. pass.":"pret. part.pass.", #ok double
        "pret. part.":"pret. part.", #ok double
        "verb imperfect":"v.", #ok?
        "adj. adv.":"adj. adv.", #ok : double
        "adj. s.":"adj. s.", #ok : double
        "v. adj. interj.":"s." #not_found
        }

fichier = open(nom,'r', encoding='utf8')
texte = fichier.read()
i = 0
for ligne in texte.split("\n") :
    i = i + 1
    ens = ligne.split("\t")
    tab.append(ens[0])
    tab.append("\t")
    if len(ens)>1 :
        print(i)
        tab.append(mapping[ens[1]])
    tab.append("\n")
fichier.close()

result = open(vers,'w', encoding='utf8')
for text in tab :
    result.write(text)
result.close()
