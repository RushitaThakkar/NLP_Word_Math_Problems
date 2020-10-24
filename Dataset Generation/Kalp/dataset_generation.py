# -*- coding: utf-8 -*-
"""
@author: kalp
"""
import copy
from googletrans import Translator
#from nltk.translate.bleu_score import sentence_bleu
import json
import time

def paraphrase(sentance,lang):
    translator = Translator()
    temp_translate=translator.translate(sentance,src='en',dest=lang)
    time.sleep(1)
    eng_translate=translator.translate(temp_translate.text,src=lang,dest='en')
    time.sleep(1)
    return eng_translate.text

'''
s1='How much probability does coin has of getting four heads in a row'
languages=['hi','gu']
translates=[]
for lang in languages:
    temp=paraphrase(s1,lang)
    translates.append(temp)
    print(temp)
'''


#score = sentence_bleu(s1, new_text, weights=(0.25, 0.25, 0.25, 0.25))

####     Trying with different types of Data from MathQA

####     Importing data



with open('MathQA/test.json') as json_file:
    test_data=json.load(json_file)
    
with open('MathQA/train.json') as json_file:
    train_data=json.load(json_file)

new_test=copy.deepcopy(test_data)
new_train=copy.deepcopy(train_data)

general=[]
other=[]
physics=[]
gain=[]
probability=[]
geometry=[]

count=3000
dic={}
for question in train_data:
    if question['category']=="general":
        general.append(question)
    elif question['category']=="gain":
        gain.append(question)
    elif question['category']=="physics":
        physics.append(question)
    elif question['category']=="probability":
        probability.append(question)
    elif question['category']=="geometry":
        geometry.append(question)
    elif question['category']=="other":
        other.append(question)
    count-=1
    if count==0:
        break
        
    
for i in range(1191,3500):
    translator = Translator()
    temp_translate=translator.translate(new_train[i]['Problem'],src='en',dest='de')
    eng_translate=translator.translate(temp_translate.text,src='de',dest='en')
    new_train[i]['Problem']=eng_translate.text
    print(i)
    with open('new_data.json', 'a') as fp:
        json.dump(new_train[i], fp)
        fp.write(',')
        fp.write('\n')
    

new_general=[]
new_geometry=[]
new_gain=[]
new_probability=[]
new_physics=[]
new_other=[]

i=1


for question in general:
    pq=paraphrase(question['Problem'],'de')
    question['Problem']=pq
    new_general.append(question)
    print("general-",i)
    i+=1

with open('general.json', 'w') as fp:
    json.dump(new_general, fp)

for question in geometry:
    pq=paraphrase(question['Problem'],'de')
    question['Problem']=pq
    new_geometry.append(question)
    
with open('geometry.json', 'w') as fp:
    json.dump(new_geometry, fp)

for question in gain:
    pq=paraphrase(question['Problem'],'de')
    question['Problem']=pq
    new_gain.append(question)
    
with open('gain.json', 'w') as fp:
    json.dump(new_gain, fp)
    
for question in probability:
    pq=paraphrase(question['Problem'],'de')
    question['Problem']=pq
    new_probability.append(question)
    
with open('probability.json', 'w') as fp:
    json.dump(new_probability, fp)
    
for question in other:
    pq=paraphrase(question['Problem'],'de')
    question['Problem']=pq
    new_other.append(question)
    
with open('other.json', 'w') as fp:
    json.dump(new_other, fp)