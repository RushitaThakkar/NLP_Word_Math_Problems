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
f = open('sample1.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
   
# Closing file 
f.close() 

my_file = open("noise_dataset.txt", "r")
content = my_file.read()
noise_content_list = content.split("\n")
my_file.close()



ans = []
for d1 in data:
    dictionary = {}
    random_sentence = random.choice(noise_content_list)
    dictionary = d1
    temp_question_list = dictionary['Problem'].split('.')
    temp_question_list.insert(randint(1,len(temp_question_list)),random_sentence)
    dictionary['Problem'] = '.'.join(sentence for sentence in temp_question_list)
    ans.append(dictionary)
    

with open('Sample_data_generated.json', 'w') as fp:
    json.dump(ans, fp)
    


    
    