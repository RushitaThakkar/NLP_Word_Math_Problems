# -*- coding: utf-8 -*-
"""
@author: kalp
"""
import copy
from googletrans import Translator
from nltk.translate.bleu_score import sentence_bleu
import json

with open('MathQA/test.json') as json_file:
    test_data=json.load(json_file)
    
with open('MathQA/train.json') as json_file:
    train_data=json.load(json_file)
    
with open('new_data.json') as json_file:
    new_data=json.load(json_file)
new_data.pop(409)
new_data.pop(408)

bleu_scores=[]
for i in range(len(new_data)):
    score = sentence_bleu(train_data[i]['Problem'], new_data[i]['Problem'], weights=(0.25, 0.25, 0.25, 0.25))
    bleu_scores.append(score)
    
print(sum(bleu_scores)/len(bleu_scores))
