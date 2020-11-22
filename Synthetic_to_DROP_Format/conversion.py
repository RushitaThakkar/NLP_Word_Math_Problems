# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 23:26:07 2020

@author: kalpp
"""

import json
import os
from os import listdir
from os.path import isfile, join
import random

def is_number(s):
    '''
    function to check if the answer is in number format or string format
    input: string
    output: boolean
    '''
    
    try:
        float(s)
        return True
    except ValueError:
        return False
i = 0    
def conversion_function_to_DROP_dataset():    
    print('start')
    drop={}
    synt_data = []    
    mypath = os.getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in onlyfiles:
        print('processing {}'.format(file))
        if file.endswith('.jsonl'):
            with open(file, 'r', encoding="utf8") as jsonl_content:
                synt_data = [json.loads(jline) for jline in jsonl_content]
    
        elif file.endswith('.json'):
            with open(file) as json_file: 
                dict_data=json.load(json_file)
                synt_data.append(dict_data.copy())
    
        else:
            continue #to abvoid reading python file in the same directory  

        sample_index_list = random.sample(range(0, len(synt_data)), int(len(synt_data)/2))
        for i in sample_index_list:
            data = synt_data[i]
            if data['Answer'] == "":
                print("***")
                continue
            key = data['Type'] + '_{}'.format(str(i))
            drop[key] = {}
            drop[key]['passage'] = ''
            drop[key]['qa_pairs'] = []
            
            qa_pair = {}
            qa_pair['question'] = data['Question']
            qa_pair['answer'] = {}
            qa_pair['answer']['date'] ={"day": "","month": "","year": ""}
            qa_pair['query_id'] = ''
            if is_number(data['Answer']):
                qa_pair['answer']['number'] = data['Answer']
                qa_pair['answer']['spans'] = []
            else:
                qa_pair['answer']['number'] = ''
                qa_pair['answer']['spans'] = [data['Answer']]        
            
            
            drop[key]['qa_pairs'].append(qa_pair)
            drop[key]['wiki_url'] = 'https://en.wikipedia.org'

            
    json_object = json.dumps(drop, indent = 4) 
    
    with open("output/DropFormatData_train.json", "w") as outfile: 
        outfile.write(json_object) 
    
    print('success')
        
if __name__ == '__main__':
    conversion_function_to_DROP_dataset()