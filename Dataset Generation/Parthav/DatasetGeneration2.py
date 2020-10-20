#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:34:31 2020

@author: parthavpatel
"""

# importing libraries 
import random 
from nltk.corpus import names 
import nltk 
from random import randint
import pandas as pd
  
def gender_features(word): 
    return {'last_letter':word[-1]} 
 
    
nltk.download('names')
# preparing a list of examples and corresponding class labels. 
males = [(name) for name in names.words('male.txt')]
females = [(name) for name in names.words('female.txt')]
objects = ['table', 'choclate', 'balloon', 'pen','marbles']  


dict = {"question": "Quent had 10 pen.Bela gave Kanya 4 of the choclate.Quent gave Sukey 4 of the pen. How many pen does Quent now have?", 
        "options": ["A)5", "B)9", "C)6", "D)8", "E)3"],
        "rationale": "10-6=4", 
        "correct": "C"}
  
s = "{0} had 10 {2}.{0} gave {1} 4 of the {2}. How many {2} does {0} now have?"
temp_s = dict['question']
l = []
temp_list = []
for i in range(100):
    temp_s = "{0} had 10 {2}.{0} gave {1} 4 of the {2}. How many {2} does {0} now have?".format(random.choice(males),random.choice(females),random.choice(objects))
    #print(temp_s)
    d = {}
    d['question'] = temp_s
    d['options'] = dict['options']
    d['rationale'] = dict['rationale']
    d['correct'] = dict['correct']
    temp_list.append(temp_s.split('.')[:2])
    l.append(d)
    
flat_list = []
for sublist in temp_list:
    for item in sublist:
        flat_list.append(item)
        

        

for item in l:
    #print(item)
    temp_question_list = item['question'].split('.')
    temp_question_list.insert(randint(1,len(temp_question_list)),random.choice(flat_list))
    item['question'] = '.'.join(sentence for sentence in temp_question_list)
    print(item)
    
