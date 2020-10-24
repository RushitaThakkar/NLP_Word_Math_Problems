# -*- coding: utf-8 -*-
"""
@author: kalp
"""
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


for i in range(500)
score = sentence_bleu(s1, new_text, weights=(0.25, 0.25, 0.25, 0.25))