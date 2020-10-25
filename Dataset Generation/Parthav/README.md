Insertion of noise sentence to generate synthetic dataset.


1st approach

* I have created a saperate file which consist of sentences which have no relation to the dataset given as source. 
* The source dataset is taken from MathQA dataset and each question is read.
* A random noise sentence from the file is chosen and inserted between sentences of the question.
* Thus in this way a new question is generated without changing the meaning of the sentence.

*Original sentence

{'Problem': 'a shopkeeper sold an article offering a discount of 5 % and earned a profit of 31.1 % . what would have been the percentage of profit earned if no discount had been offered ?',
 'Rationale': '"giving no discount to customer implies selling the product on printed price . suppose the cost price of the article is 100 . then printed price = 100 ã — ( 100 + 31.1 ) / ( 100 â ˆ ’ 5 ) = 138 hence , required % profit = 138 â € “ 100 = 38 % answer a"',
 'options': 'a ) 38 , b ) 27.675 , c ) 30 , d ) data inadequate , e ) none of these',
 'correct': 'a'}
 
 *New sentence generated
 
 {'Passage':''
 'Question': 'a shopkeeper sold an article offering a discount of 5 % and earned a profit of 31.1 % . 1000 after 4 years. what would have been the percentage of profit earned if no discount had been offered ?. on the way back steve drives twice as fast as he did on the way to work ',
 'Equation':''
 'Reasoning Type': '"giving no discount to customer implies selling the product on printed price . suppose the cost price of the article is 100 . then printed price = 100 ã — ( 100 + 31.1 ) / ( 100 â ˆ ’ 5 ) = 138 hence , required % profit = 138 â € “ 100 = 38 % answer a"',
 'Answer': 38,
 'Type': 'PP_Random_noise_insertion'}



2nd approach

* In this approach I am generating a template with certain questions which can help in generating a new dataset from the template by replacing the names and also inserting random noise sentences which are generated from the template.


*Original sentence for template
Template : ["{0} {6} {3} {2}.{0} {7} {1} {4} of the {2}. How many {2} does {0} now have?",
     "{0} {6} {3} {5}. {0} {7} {4} {5} to {1}.How many {5} does {0} now have?",
     ]

* New sentence generated from the template 

{'Passage':'',
'Question': 'Lucio had 10 balloon.Lucio gave Emera 4 of the balloon.{Vaughn had 10 pen}. How many balloon does Lucio now have?',  
'Equation': '10-6=4', 
'Reasoning Type': ,
'Answer': 'C',
'Type': 'PP_Random_noise_insertion'} 
