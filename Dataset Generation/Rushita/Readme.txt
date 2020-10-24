NLP Word Math Problems - Generate Word Math Problems manually by inserting words in a Template.
____________________________________________________________________________________________________
There are essentially 8 functions, each generating specific type of questions.
____________________________________________________________________________________________________
Functions with their descriptions
1) function -> signed_expression(args).
 Generates signed expressions based on the arguments and values of the final output of those signed expressions
 example
{
"id": "e5a878885e054f5c994d8a34a90d4ad2", "passage": "", 
"question": "- 1572.4 - 19227.64 - 5894", 
"equation_expression": "- 1572.4 - 19227.64 - 5894", 
"answer": -26694.04, "type": 
"RT_Template_Based_Generation", 
"reasoning_type": "addition subtraction operations"
}
____________________________________________________________________________________________________
2) function -> min_max_avg_expression(args)
Generates questions involving min,max, avg of the arguments given
example
{"id": "b5c4dd6e4b24430ea885b3e93d639368",
 "passage": "", 
"question": "there are 3 people namely Liuka,Weider,Elene their height are 1572.4, 19227.64, 5894 find the mean of height.",
 "equation_expression": "average(1572.4, 19227.64, 5894)", 
"answer": 8898.01, "type": "RT_Template_Based_Generation", 
"reasoning_type": "min max avg operations"}
Scope - Covers questions related to finding min, max, mean/avg of weights, heights and scores for the people involved.
______________________________________________________________________________________________________________________
3) function -> arg_min_max_expression
Generates questions where it ivolves finding argmin, argmax from the given list of numbers
example
{"id": "5ade1888f1404c73bd962cfcf841b121", 
"passage": "", "question": " the count of things is given by green 1572.4, shampoo 19227.64, bag 5894,  which of them has minimum count", 
"equation_expression": "argmax(green 1572.4, shampoo 19227.64, bag 5894)",
 "answer": "shampoo", "reasoning_type": "arg_min_max_expression", "type":
 "RT_Template_Based_Generation", "knowledge": ""}
Also involves questions realted to finding a person with max/min[height, weight, scores]
_______________________________________________________________________________________________________________________
4) function -> rand_percent()
Generates questions related to finding percentage
example
{"id": "44e2195872a64a3e850a469a9f7cc26c", 
"passage": "", "question": "the votes recieved by the participating parties are democratic 66.3%, shiv-sena 19%, republic 14.7% what is the percentage of votes  recieved by republic,democratic", 
"equation_expression": "percent republic, democratic :: democratic 66.3%, shiv-sena 19%, republic 14.7%", 
"answer": 81.0, "type": "RT_Template_Based_Generation", "reasoning_type": "percentage", 
"knowledge": "Sum of all percentage is 100"}
______________________________________________________________________________________________________________________
5) function -> date_min_max()
Generates questions related to find the minimum and maximum of the dates
example
{"id": "dc16b3585cb14592adfe9496ef4e0ec5", "passage": "", "question": "The birthdays of Kaleb,Meade,Piotr are August 22, 0763; 09 July 0763; 24 July 0763 who is older of the two", 
"equation_expression": "last(August 22, 0763; 09 July 0763; 24 July 0763)", 
"answer": "Kaleb", "type": "RT_Template_Based_Generation", "reasoning_type": "max,min of dates", "knowledge": ""}
______________________________________________________________________________________________________________________
6) function -> date_diff()
Generates questions realted to finding the difference in dates involving calculation of number of months, days and years
{"id": "c4a272f65dab483eb79e85100a322be6", 
"passage": "", 
"question": " There are 2 people. Kamilah,Marlow Their birthday are March 03, 0790; April 20, 0790 What is the difference in their age in days", 
"equation_expression": "difference in days(March 03, 0790; April 20, 0790)",
 "answer": 47, "type": "RT_Template_Based_Generation", "reasoning_type": "date difference", "knowledge": ""
}
______________________________________________________________________________________________________________________________
7) functions -> triangle_questions()
Generates questions related to triangles mainly like finding the 3rd angle given the other 2 angles
example
{"id": "5f000adc19af4d3e867b95c3ab09a9bf", "passage": "", 
"question": " The two angles of a triangle are 32 and 15respectively  what is the third angle ", 
"equation_expression": "120 - 32-15", "knowledge": "angles of a trainge sum to 180", "answer": 133, 
"reasoning_type": "geometry", "type": "RT_Template_Based_Generation"
}
______________________________________________________________________________________________________________________________
8) functions -> speed_distance()
Generates questions involving speed calculations based on the distance and time units given in km/m 
and time given in hr/s
{"id": "e24d68502f764cfe987c06d266ddffc0", "passage": "", 
"question": "There is a car covering 63m in 115s Find speed in km/hr",
 "equation_expression": "63/115*3.6", "knowledge": "Speed is distance covered in unit time. 1km = 1000m and 1 hr = 60 sec",
 "answer": "1.972173913043478km/hr", "reasoning_type": "speed-distance-time", "type": "RT_Template_Based_Generation"}

____________________________________________________________________________________________________________________________
References
Code - https://github.com/ag1988/injecting_numeracy
Paper - https://arxiv.org/pdf/2004.04487.pdf
___________________________________________________________________________________________________________________________
Running the code
python generate_synthetic_data.py --num_samples 1e6 --num_dev_samples 1e4 --output_jsonl sytheticData.json

___________________________________________________________________________________________________________________________
Requirements
- - - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ---
pytorch
nltk
json
jsonlines
tqdm
ujson


