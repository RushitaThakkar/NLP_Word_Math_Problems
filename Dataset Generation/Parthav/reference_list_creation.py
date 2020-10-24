#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:04:09 2020

@author: parthavpatel
"""

from itertools import chain
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')

list_items = []
#item_list = ['candy','cake','cookie','pizza','sandwich']
item_list = ['have','had','contains']
#item_list = ['gave','sell']
for item in item_list:
    synonyms = wordnet.synsets(item)
    lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    for lemma in lemmas:
        list_items.append(lemma)
        print(lemma)
        
        

with open("objects.txt", "w") as f:
    for item in list_items:
        f.write("%s\n" % item)



with open("contains_synonyms.txt", "w") as f:
    for item in list_items:
        f.write("%s\n" % item)



with open('sell_synonyms.txt', 'w') as f:
    for item in list_items:
        f.write("%s\n" % item)
