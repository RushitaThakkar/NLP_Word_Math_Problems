from pycorenlp import StanfordCoreNLP
from POSTree import POSTree
import os
import json
import re
from simpleparse.parser import Parser
import random
import jsonlines

#java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000


path = os.getcwd() + "/AQuA_dataset/"

nlp = StanfordCoreNLP('http://localhost:9000')

def read_data(name):
    dev_data = []
    with open(path+ name + ".json" ,"r") as f:
        for j_obj in f:
            dev_data.append(json.loads(j_obj))
            
    return dev_data
    
    
def get_correct_answer(data):
    option_no = data['correct']
    ind = ord(str.lower(option_no)) - 96
    ans = data['options'][ind-1]
    ans = ans[2:]

    return ans
    

def gen_mask(split_samp, formed_sent_rep):
    split_samp[-1] = formed_sent_rep
    join_samp = '.'.join(split_samp)
    
    grammar = """
    integer := [0-9]+
    <alpha> := -integer+
    all     := (integer/alpha)+
    """
    parser = Parser(grammar, 'all')
    digit_data = parser.parse(join_samp)
    digit_data = digit_data[1]

    if len(digit_data) == 0:
        raise ValueError('Unknown question structure!')
    else:
        start_ind = digit_data[0][1]
        end_ind = digit_data[0][2]

        new_samp = join_samp[:start_ind] + "___" + join_samp[end_ind:]
        ans = join_samp[start_ind:end_ind]

        return new_samp, ans 

    
def json_obj(gen_text,gen_output,data,gen_id):
    new_data = {}
    new_data['ID'] = gen_id
    new_data['Passage'] = ""
    new_data['Question'] = gen_text
    new_data['Equation'] = ""
    new_data['Answer'] = gen_output
    new_data['Reasoning Type'] = ""
    new_data['Type'] = "SR_Masking"
    
    
    return new_data


data = read_data("train")
j_objs = []
gen_id = random.randint(0,100000)
for i in range(6000):
    print(i)
    try:
        sample = data[i]['question']
        ans = get_correct_answer(data[i])
        split_samp = sample.split('.')
        output = nlp.annotate(split_samp[-1], properties={'annotators': 'tokenize,ssplit,pos,depparse,parse','outputFormat': 'json'})
        parsed = output['sentences'][0]['parse']
        
        p_list = parsed.split("\r\n")
        p_str = '"'
        for j in range(len(p_list)):
            p_str = p_str + p_list[j] + '"   "'
    
        
        tree = POSTree(eval(p_str[:len(p_str)-4]))
        formed_sent = tree.adjust_order()
        formed_sent_rep = formed_sent.replace("**blank**", ans)
        formed_sent_rep = str.upper(formed_sent_rep[0]) + formed_sent_rep[1:]
        
        
        new_samp, new_output = gen_mask(split_samp, formed_sent_rep)
        j_objs.append(json_obj(new_samp,new_output,data[i],gen_id))
        gen_id = gen_id + 1
        
    except:
        continue
    

with jsonlines.open('output_masking.jsonl', mode='w') as writer:
    for j in range(len(j_objs)):
        writer.write(j_objs[j])
    


