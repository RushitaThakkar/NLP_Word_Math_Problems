#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 00:19:07 2020

@author: parthavpatel
"""

import json 
import random
from random import randint
  
# Opening JSON file 
f = open('sample1.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 

    
# Closing file 
f.close() 
 
# Opening JSON file 
f = open('sample2.json',) 
  
# returns JSON object as  
# a dictionary 
data1 = json.load(f) 

  
# Closing file 
f.close()

data_combined = data + data1 

l = []
for d in data_combined:
    temp_l = d['Problem'].split('.')
    for t in temp_l:
        if '?' in t or t.strip().isdigit() or t.isspace() or len(t)==0 or 'what' in t:
            temp_l.remove(t)
    l = l + temp_l

with open('noise_dataset.txt', 'w') as f:
    for item in l:
        f.write("%s\n" % item)
