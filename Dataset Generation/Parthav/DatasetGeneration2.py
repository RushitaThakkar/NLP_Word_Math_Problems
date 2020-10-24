# importing libraries 
import random  
from random import randint
import json



# loading list of names from the file created 
nam = open("names.txt", "r")
list_names = nam.readlines()
nam.close()

# loading list of synonyms from the file created
obj = open("contains_synonyms.txt", "r")
list_contains = obj.readlines()
obj.close()

# loading list of synonyms from the file created
obj = open("sell_synonyms.txt", "r")
list_sell = obj.readlines()
obj.close()


# loading list of synonyms from the file created 
obj = open("objects.txt", "r")
list_objects = obj.readlines()
obj.close()




s = ["{0} {6} {3} {2}.{0} {7} {1} {4} of the {2}. How many {2} does {0} now have?",
     "{0} {6} {3} {5}. {0} {7} {4} {5} to {1}.How many {5} does {0} now have?",
     ]

final_list = []
temp_list = []
for t_s in s:
    l = []
    for i in range(500):
        number1 = random.randint(1,1000)
        number2 = random.randint(1,1000) + number1
        #temp_s = "{0} had {3} {2}. {0} gave {1} {4} of the {2}. How many {2} does {0} now have?".format(random.choice(list_names),random.choice(list_names),random.choice(list_objects),number2,number1)
        temp_s = t_s.format(random.choice(list_names),random.choice(list_names),random.choice(list_objects),number2,number1,random.choice(list_objects),random.choice(list_contains),random.choice(list_sell)) 
        d = {}
        d['Passage'] = ''
        d['Question'] = temp_s
        d["Equation"] = "{0}-{1}={2}".format(number2,number1,(number2-number1))
        d['Answer'] = number2 - number1
        d["Reasoning Type"] = ''
        d["Type"] = 'PP_random_question_generation_with_template_and_noise_insertion'
        temp_list.append(temp_s.split('.')[:2])
        l.append(d)
        
    flat_list = []
    for sublist in temp_list:
        for item in sublist:
            flat_list.append(item)

    for item in l:
        #print(item)
        temp_question_list = item['Question'].split('.')
        temp_question_list.insert(randint(1,len(temp_question_list)-1),random.choice(flat_list))
        item['Question'] = '.'.join(sentence for sentence in temp_question_list)
        final_list.append(item)
    
with open('Sample_data_generated_1.jsonl', 'w') as outfile:
    for entry in final_list:
        json.dump(entry, outfile)
        outfile.write('\n')
        
