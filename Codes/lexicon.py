# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:15:06 2020

@author: Dao
Obtain a lexicon of brown corpus and put it in a lexicon file
"""

from nltk.corpus import brown
brown_words = brown.tagged_words()
words =  {}
for el in brown_words :
    word = el[0]
    if word in words.keys() :
        tag = el[1]
        tags = words.get(word)
        if not (tag in tags) :
            tags.append(tag)
        words[word] = tags
    else :
        words[word] = [el[1]]

file = open("lexicon",'w', encoding='utf8')
for word,tags in words.items() :
    for tag in tags :
        file.write(word)
        file.write("\t")
        file.write(tag)
        file.write("\t")
    file.write(word)
    file.write("\n")

file.close()