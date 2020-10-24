# -*- coding: utf-8 -*-
"""
@author: kalp
"""
import re
import copy
from googletrans import Translator
#from nltk.translate.bleu_score import sentence_bleu
import json

with open('MathQA/test.json') as json_file:
    test_data=json.load(json_file)
    
with open('MathQA/train.json') as json_file:
    train_data=json.load(json_file)
    
with open('new_data.json') as json_file:
    new_data=json.load(json_file)


def return_ans_value(options,correct_option):
    if correct_option == None:
        return "None"
    list = options.split(',')
    for l in list:
        if correct_option in l:
            return re.sub('[A-Za-z%$]','',l.split(')')[1].strip().replace(" ", ""))
    return "None"


def change_question_format(ans):
    temp_ans = []
    i = 0
    for item in ans:
        temp_dict = {}
        temp_dict["ID"]= i 
        temp_dict["Passage"]= ""
        temp_dict["Question"] = item['Problem'] 
        temp_dict["Equation"] =  item["annotated_formula"]
        temp_dict["Answer"] =  return_ans_value(item['options'],item['correct'])
        temp_dict["Reasoning Type"] = "" 
        temp_dict["Type"] = "kp_back_translation"
        temp_ans.append(temp_dict)
        i += 1
    return temp_ans

formatted_data=change_question_format(new_data)


with open('generated_data_kalp.jsonl', 'w') as outfile:
    for entry in formatted_data:
        json.dump(entry, outfile)
        outfile.write('\n')