import json
import os
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import random
from nltk.translate.bleu_score import sentence_bleu
import pandas as pd
import random
import jsonlines

stop_words = stopwords.words("english") 
 

path = os.getcwd() + "/AQuA_dataset/"


#Function to read the data it can be train, dev or test datatset from AQuA
def read_data(name):
    dev_data = []
    with open(path+ name + ".json" ,"r") as f:
        for j_obj in f:
            dev_data.append(json.loads(j_obj))
            
    return dev_data
    
#This function replaces the original token into its synonyms and different words
def spin_tokens(i):
    word = i
    synonyms = []
    if word in stop_words:
        return word
    if wordnet.synsets(word)==[]:
        return word
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    pos_tag_word = nltk.pos_tag([word])
    pos = []
    for i in synonyms:
        pos.append(nltk.pos_tag([i]))
    final_synonyms = []
    for i in pos:
        if pos_tag_word[0][1] == i[0][1]:
            final_synonyms.append(i[0][0])
    final_synonyms = list(set(final_synonyms))
    
    #print(final_synonyms)
    rm_index = []
    for i in range(len(final_synonyms)):
        if '_' in final_synonyms[i]:
            rm_index.append(i)
            
    rm_index = rm_index[::-1]
    if len(rm_index) != len(final_synonyms):
        for ind in rm_index:
            final_synonyms.pop(ind)
    
    #print('New:', final_synonyms)
    if final_synonyms == []:
        return word
    if word.istitle():
        return random.choice(final_synonyms).title()
    else:
        return random.choice(final_synonyms)
    
#This function transforms the original sentence into a text spinned sentece using spin_tokens function
def text_spinner_helper(para):
    para_split = word_tokenize(para)
    final_text = []
    for i in para_split:
        final_text.append(spin_tokens(i))
    final_text = " ".join(final_text)
    return final_text

#This function calculates the BLEU score for orignal and generated sample to analyze how similar are the sentences
def calc_bleu_score(reference, candidate):
    bleu1 = 0
    bleu2 = 0
    bleu3 = 0
    bleu4 = 0
    
    try:
        reference = reference.split(" ")
        candidate = candidate.split(" ")
        reference = [reference]
        bleu1 = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
        bleu2 = sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0))
        bleu3 = sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0))
        bleu4 = sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25))
        #print('BLEU-1 score: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))
        #print('BLEU-2 score: %f' % sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))
        #print('BLEU-3 score: %f' % sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))
        #print('BLEU-4 score: %f' % sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))
    except:
        print("Error")
        
    return bleu1, bleu2, bleu3, bleu4
    
#This function prepares a json object to be stored in the final result
def json_obj(gen_text,data,gen_id):
    option_no = data['correct']
    ind = ord(str.lower(option_no)) - 96
    ans = data['options'][ind-1]
    ans = ans[2:]
    new_data = {}
    new_data['ID'] = gen_id
    new_data['Passage'] = ""
    new_data['Question'] = gen_text
    new_data['Equation'] = ""
    new_data['Answer'] = ans
    new_data['Reasoning Type'] = data['rationale']
    new_data['Type'] = "SR_Text_Spinner"
    
    gen_id = gen_id + 1
    
    return new_data
    
    
#This function does all the process of text spinning and write the results   
def text_spinner(data):
    j_objs = []
    df = pd.DataFrame(columns=['Original', "Spinned Text", "BLEU1","BLEU2","BLEU3","BLEU4"])
    org_list = []
    spin_list = []
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    gen_id = random.randint(0,100000)
    for i in range(12000):
        print(i)
        sample = data[i]['question']
        spinned_text = text_spinner_helper(sample)
        #print('Original:', sample)
        #print('Spinned:', spinned_text)
        bl1,bl2,bl3,bl4 = calc_bleu_score(sample, spinned_text)
        #print("\n")
        org_list.append(sample)
        j_objs.append(json_obj(spinned_text,data[i],gen_id))
        spin_list.append(spinned_text)
        b1.append(bl1)
        b2.append(bl2)
        b3.append(bl3)
        b4.append(bl4)
        gen_id = gen_id + 1
        
    df['Original'] = org_list
    df['Spinned Text'] = spin_list
    df['BLEU1'] = b1
    df['BLEU2'] = b2
    df['BLEU3'] = b3
    df['BLEU4'] = b4
    df.to_csv("Results.csv")
    
    with jsonlines.open('output.jsonl', mode='w') as writer:
        for j in range(len(j_objs)):
            writer.write(j_objs[j])

    
dev_data = read_data("train")
text_spinner(dev_data)
    

