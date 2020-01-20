# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:59:51 2020

@author: Dao
Obtain a tagset of brown corpus and put it in a tagset file
"""

from nltk.corpus import brown
brown_words = brown.tagged_words()
tags = []
for el in brown_words :
    tag = el[1]
    if not (tag in tags) :
        tags.append(tag)

file = open("tagset",'w', encoding='utf8')
for tag in tags :
    file.write(tag)
    file.write(" ")

file.close()