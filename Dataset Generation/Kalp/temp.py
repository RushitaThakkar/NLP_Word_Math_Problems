# -*- coding: utf-8 -*-
"""
@author: kalp
"""

#from googletrans import Translator
#from nltk.translate.bleu_score import sentence_bleu
import json


with open('MathQA/test.json') as json_file:
    test_data=json.load(json_file)
    
with open('MathQA/train.json') as json_file:
    train_data=json.load(json_file)

for i in range(5,10):
    with open('temp.json', 'a') as fp:
        fp.write('kalp')
        fp.write('\n')
