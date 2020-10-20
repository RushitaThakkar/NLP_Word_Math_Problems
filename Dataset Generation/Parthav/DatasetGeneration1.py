#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:26:55 2020

@author: parthavpatel
"""

import json 
import random
from random import randint
  
# Opening JSON file 
f = open('train.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  

  
# Closing file 
f.close() 

l = []
for d in data:
    temp_l = d['Problem'].split('.')
    for t in temp_l:
        if '?' in t or t.strip().isdigit() or t.isspace() or len(t)==0:
            temp_l.remove(t)
    l = l + temp_l


# Opening JSON file 
f = open('test.json',) 
  
# returns JSON object as  
# a dictionary 
data1 = json.load(f) 
    
# Closing file 
f.close() 

ans = []
for d1 in data1:
    flat_list = l
    dictionary = {}
    random_sentence = random.choice(temp_l)
    dictionary = d1
    temp_question_list = dictionary['Problem'].split('.')
    temp_question_list.insert(randint(1,len(temp_question_list)),random.choice(flat_list))
    dictionary['Problem'] = '.'.join(sentence for sentence in temp_question_list)
    ans.append(dictionary)
    

str = '      '
print(str.isspace())
    
    