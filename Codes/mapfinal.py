# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:23:39 2019

@author: Dao
@arg1 nom : file to look
@arg2 vers : file to write
mapping of the Brown Corpus's tags to our tags
nom and vers form :
word\ttag
...

"""


import sys

nom = sys.argv[1]
vers = sys.argv[2]
tab = []
mapping = {
        "at":"art.", #ok
        "jj-tl":"adj.", #ok
        "vbd":"pret.",
        "nr":"s.", #ok
        "nn":"s.", #ok
        "in" :"prep. | conj.",
        "jj":"adj.",
        "``":"SENT", #ok
        "''":"SENT", #ok
        "cs":"conj.",
        "dti":"adj.",
        "." :"SENT", #ok
        ",":"SENT", #ok
        "hvd":"pret. part.pass.",
        "vbz":"tp", #ok
        "cc":"conj.", #ok
        "cc-tl":"conj.", #ok
        "in-tl":"prep. | conj.",
        "vbn":"part.pass.",
        "ben":"part. | pret.",
        "bem":"v.",
        "to":"prep.",
        "vb":"v.",
        "rb":"adv.", #ok
        "dt":"art.",
        "pps":"pron.",
        "dod" :"pret.",
        "ap"  :"adj.",
        "hv" : "v.",
        "dts" :"adj.",
        "vbg" :"part.", #ok
        "ppo" :"pron.",
        "ql"  :"adv.", #ok
        "abx":"adv.", #ok
        "nn-hl":"s.", #ok
        "vbn-hl":"part.pass.",
        "md":  "part.pass.",
        "be" : "v.",
        "vbg-tl":"part.", #ok
        "bez":"tp", #ok
        "nn$-tl":"s.", #ok
        "hvz":"tp", #ok
        "abn":"adv.", #ok
        "pn":"pron.",
        "ppss":"pron.",
        "pp$":"pron.poss.", #ok
        "do":"v.",
        "nn$":"s.", #ok
        "wps":"pron.",
        "ex":"adv.", #ok
        "vb-hl":"v.",
        ":":"SENT", #ok
        "(":"SENT", #ok
        ")":"SENT", #ok
        "'":"SENT", #ok
        "rp":"particle.", #ok
        "--":"SENT", #ok
        "bed":"pret.",
        "od":"CD",
        "beg":"prep. | conj. | s.",
        "at-hl":"art.",
        "vbg-hl":"part.", #ok
        "at-tl":"art.",
        "ppl":"pron.",
        "doz":"tp", #ok
        "nr$":"s.", #ok
        "dod*":"pret.",
        "bedz*":"pret.",
        ",-hl":"SENT", #ok
        "SENT":"SENT", #ok
         "SENT-hl":"SENT", #ok
        "ppss+bem":"pron. v.",
        "ppss+ber":"pron. v.",
        "md*":"v.",
        "(-hl*":"SENT", #ok
        ")-hl":"SENT",  #ok
        "md-hl":"v.",
        "vbz-hl":"tp", #ok
        "in-hl":"prep.",
        "np-tl":"NP", #ok
        "nn-tl":"NP", #ok
        "np$":"NP", #ok
        "nns":"s.", #ok
        "np-tl":"NP", #ok
        "nn-tl":"NP", #ok
        "np":"NP", #ok
        "np$":"NP", #ok
        "rbr":"adv.", #ok
        "wdt":"pron.",
        "bedz":"pret.",
        "ber":"v.",
        "jjt":"adj.",
        "wrb":"adv.", #ok
        "cd":"CD", #ok
        "jjr":"adj.",
        "nns-hl":"s.", #ok
        "*":"adv.", #ok
        "nns-tl":"s.", #ok
        "nps":"s.", #ok
        "jjs":"adj.",
        "np-hl":"NP", #ok
        "nns$":"s.", #ok
        "np$":"NP", #ok
        "cd-tl":"CD", #ok
        "rbt":"adv.",
        #fichier cp28
        "ppss+md":"pron. pret.",
        "pps+md":"pron. pret.",
        "dt+md":"art. pret.",
        "qlp":"adv.", #ok
        "hvg":"v.",
        "hvn":"part.pass.",
        "pp$$":"pron.poss.", #ok
        "pps+hvd":"pron. pret.",
        "hvd*":"pret.",
        "pps+bez":"pron. sp.",
        "bed*":"pret.",
        "ppls":"pron. pers.",
        "uh":"interj.",
        #fichier cp29
        "ppss+hv":"pron.pers. v.",
        "bez*":"sp.",
        "abl":"adv.",
        "wp$":"pron.",
        "nps-tl":"s.", #ok
        "nps$":"s.", #ok
        "do*":"v.",
        "doz*":"tp", #ok
        "ex+bez":"adv. tp",
        "vb+ppo":"v. pron.",
        #fichier cr01
        "ber*":"v.",
        "np$-tl":"NP", #ok
        "np$-hl":"NP", #ok
        "jj-hl":"adj.",
        "dt-hl":"art.",
        "fw-nns":"s.", #ok Par defaut, fw = foreign word
        #fichier cr02
        "rb+bez":"adv. tp",
        "wpo":"pron.",
        "wps-tl":"pron.",
        "do-tl":"v.",
        #fichier cr03
        "dt-tl":"art.",
        "fw-nn":"s.", #ok
        "fw-*":"s.", #ok Par defautl, fw = foreign word
        "fw-jj":"adj.",
        #fichier cr04
        "pn$":"pron.",
        "wps+md":"pron. pert.",
        "nn+hvz":"s. tp",
        "nn+bez":"s. tp",
        "md+to":"pret. prep.",
        "dt+bez":"art. tp.",
        "ex+md":"adj. pret.",
        #fichier cr05
        "wdt+bez":" tp",
        "dtx":"conj.",
        "wps+bez":"pron. tp",
        "pps+hvz":"pron. tp",
        #fichier cr06
        "jjt-tl":"adj.",
        "jj-nc":"adj.",
        "hvz*":"tp", #ok
        "fw-rb":"adv.", #ok
        "fw-np":"NP", #ok
        "fw-vb":"v.",
        "fw-vbg":"part.", #ok
        "fw-bez":"tp", #ok
        #fichier cr07
        "np+bez":"NP tp",
        "rb$":"adv.", #ok
        #fichier cr08
        "fw-in":"prep.",
        "fw-at-tl":"art.",
        "fw-in+at-tl":"prep. art.",
        "nn-nc":"s.", #ok
        "fw-vb-nc":"v.",
        "fw-nn-nc":"s.", #ok
        "vbn-tl":"pret.",
        "pp$-tl":"pron.",
        "fw-vbn":"pret.",
        "fw-nns-tl":"s.", #ok
        #totest
        "fw-in+nn":"prep. s.",
        "fw-nn-tl":"s.",
        "fw-uh-tl":"interj.",
        "fw-pp$-tl":"pron.pers."
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
