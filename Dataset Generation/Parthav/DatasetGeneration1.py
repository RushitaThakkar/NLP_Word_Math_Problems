#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:26:55 2020

@author: parthavpatel
"""

import json 
import random
from random import randint
import re
  
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


def return_ans_value(options,correct_option):
    list = options.split(',')
    for l in list:
        if correct_option in l:
            return re.sub('[A-Za-z%$]','',l.split(')')[1].strip().replace(" ", ""))

def change_question_format(ans):
    temp_ans = []
    i = 0
    count = 0
    for item in ans:
        try:
            if re.match("[+,-]*\d+?\.*\d*", item['correct']):
            #if item['correct'].replace('.','',1).isdigit():
                temp_dict = {}
                temp_dict["ID"]= i 
                temp_dict["Passage"]= ""
                temp_dict["Question"] = item['Problem'] 
                temp_dict["Equation"] =  item["annotated_formula"]
                temp_dict["Answer"] =  item['correct']
                temp_dict["Reasoning Type"] = "" 
                temp_dict["Type"] = "PP_Random_noise_insertion"
                temp_ans.append(temp_dict)
                i += 1
        except:
            print(item['correct'])

    print(count)        
    return temp_ans
        
    
    
ans = []
for d1 in data:
    dictionary = {}
    random_sentence = random.choice(noise_content_list)
    dictionary = d1
    temp_question_list = dictionary['Problem'].split('.')
    temp_question_list.insert(randint(1,len(temp_question_list)),random_sentence)
    dictionary['Problem'] = '.'.join(sentence for sentence in temp_question_list)
    dictionary['correct'] = return_ans_value(dictionary['options'],dictionary['correct'])
    ans.append(dictionary)
    
final_list = change_question_format(ans)


with open('Sample_data_generated.json', 'w') as fp:
    json.dump(final_list, fp)
    


    
    