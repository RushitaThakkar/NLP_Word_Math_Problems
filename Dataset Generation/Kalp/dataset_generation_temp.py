# -*- coding: utf-8 -*-
"""
@author: kalp
"""
import copy
#from googletrans import Translator
#from nltk.translate.bleu_score import sentence_bleu
import translators as ts
import json
s1='How much probability does coin has of getting four heads in a row'
languages=['hi','gu']
translates=[]

for lang in languages:
    #translator = Translator()
    temp_translate=ts.deepl(s1,to_language='ru',from_language='en')
    eng_translate=ts.deepl(temp_translate,to_language='en',from_language='ru')
    translates.append(eng_translate)

for items in translates:
    print(items.text)

#score = sentence_bleu(s1, new_text, weights=(0.25, 0.25, 0.25, 0.25))

####     Trying with different types of Data from MathQA

####     Importing data

with open('MathQA/test.json') as json_file:
    test_data=json.load(json_file)
    
with open('MathQA/train.json') as json_file:
    train_data=json.load(json_file)

new_test=copy.deepcopy(test_data)
new_train=copy.deepcopy(train_data)
a=0
for question in new_test:
    translator = Translator()
    temp_translate=translator.translate(question['Problem'],src='en',dest='hi')
    eng_translate=translator.translate(temp_translate.text,src='hi',dest='en')
    question['Problem']=eng_translate.text
    print(a)
    a+=1
    
