#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 00:19:07 2020

@author: parthavpatel
"""

import json 
import os
import re

def noise_sentence_generation(file_name):  
    data = []
    noise_content_list = []
    for line in open(file_name, 'r'):
        data.append(json.loads(line))
    
    cleaned_data = data_cleaning(data)
    if os.path.isfile('noise_dataset.txt'):
        my_file = open("noise_dataset.txt", "r")
        content = my_file.read()
        noise_content_list = content.split("\n")
        my_file.close()
    
    noise_content_list += cleaned_data

    with open('noise_dataset.txt', 'w') as f:
        for item in noise_content_list:
            f.write("%s\n" % item)

def data_cleaning(data):
    l = []
    for d in data:
        if 'question' in d.keys():
            key_label = 'question'
        else:
            key_label = 'problem'
        temp_l = d[key_label].split('.')
        for t in temp_l:
            t = t.strip()
            if len(t) > 10:
                if re.match(r"[what|What|Find|find]",t):
                    continue
                elif not re.search('[a-zA-Z]', t):
                    continue
                if '?' in t or t.strip().isdigit() or t.isspace() or len(t) < 10:
                    continue
                else:
                    l.append(t)
            else:
                pass
    return l


if __name__ == '__main__':
    #Change the file name to insert new noise sentences in the noise sentence dataset
    file_name = 'input_noise_creation.json'
    noise_sentence_generation(file_name)
    

