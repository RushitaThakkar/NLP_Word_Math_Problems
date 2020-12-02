#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:27:04 2020

@author: sharadhi
"""
import json
import string
import random 
import jsonlines

with open('/Users/sharadhi/Documents/Third_semester/NLP/drop_dataset/drop_dataset_train.json') as f:
    
    raw_data = json.load(f)
    
    complete_json_list = {}
    
    count = 0 
    
    for key, value in raw_data.items():
        
        count += 1 
        
        if( count <= 500 ):
    
            passage_data = raw_data[ key ]
          
            data = passage_data['qa_pairs']
            
            json_list = []
            
            #print( len( data ) )
            
            for index in range( 0 , len( data ) ):
            
                #print( index )
                
                question = data[ index ]
                
                problem = question[ 'question' ]
                
                words = problem.split()
                
                num_of_words = len( words )   
                
                num1 = random.randint( 0 , int( num_of_words / 2 ) )
                
                num_list = []
                
                for i in range( 0 , num1 ):
                    
                    num2 = random.randint( 0 , num_of_words - 1 )
                    
                    if num2 not in num_list:
                        
                        num_list.append( num2 )
                
                filtered_num_list = []
                
                for i in range( 0 , len( num_list ) ):
                    
                    if( words[ num_list[ i ] ].isalpha() ):
                        
                        filtered_num_list.append( num_list[ i ] )
                        
                if not filtered_num_list:
                    
                    continue
                    
                reconstructed_question = []
                
                for i in range( 0 , num_of_words ):
                    
                    if( i not in filtered_num_list ):
                        
                        reconstructed_question.append( words[ i ] )
                    
                    else:
                        
                        #print( words[ i ] )
                        
                        qwerty_error = { 'q' : [ 'w', 'a', 's' ] , 'w' : [ 'q', 's', 'e' ] , 'e' : [ 'w', 's', 'd', 'r' ] , 'r' : [ 'e', 'd', 'f', 't' ] , 't' : [ 'r', 'f', 'g', 'y' ] , 'y' : [ 't', 'g', 'h', 'u' ] , 'u' : [ 'y', 'h', 'j', 'i' ] , 'i' : [ 'u', 'j', 'k', 'o' ] , 'o' : [ 'i', 'k', 'l', 'p' ] , 'p' : [ 'o', 'l' ] , 'a' : [ 'q', 's', 'z' ], 's' : [ 'a', 'w', 'd', 'z' ], 'd' : [ 'e', 's', 'f', 'x' ], 'f' : [ 'r', 'd', 'g', 'c' ], 'g' : [ 't', 'f', 'h', 'v' ], 'h' : [ 'y', 'g', 'b', 'j' ], 'j' : [ 'u', 'h', 'k', 'n' ], 'k' : [ 'i', 'j', 'l', 'm' ], 'l' : [ 'k', 'o', 'p' ], 'z' : [ 'a', 's', 'x' ], 'x' : [ 'z', 's', 'd', 'c' ], 'c' : [ 'x', 'd', 'f', 'c' ], 'v' : [ 'c', 'f', 'g', 'b' ], 'b' : [ 'v', 'f', 'g', 'b' ], 'n' : [ 'b', 'h', 'j', 'm' ], 'm' : [ 'n', 'j', 'k', 'l'] }
            
                        num3 = max( 1 , random.randint( 0 , int( len( words[ i ] ) / 4 ) ) )
                        
                        letter_list = []
                        
                        for j in range( 0 , num3 ):
                            
                            num4 = random.randint( 0 , len( words[ i ] ) - 1 )
                            
                            if num4 not in letter_list:
                                
                                letter_list.append( num4 )
                                
                        new_word = ''
                        
                        for j in range( 0 , len( words[ i ] ) ):
                            
                            if j in letter_list:
                                
                                if words[ i ][ j ] not in qwerty_error:
                                    
                                    new_word += ''
                                    
                                else:
                                    
                                    new_word += random.choice( qwerty_error[ words[ i ][ j ] ] )
                                
                            else:
                                
                                new_word += words[ i ][ j ]
            
                        reconstructed_question.append( new_word )
                        
                string_question = ''
                
                for word in reconstructed_question:
                    
                    string_question += word + ' '
                    
                #index = 1
                
                new_qa = {}
                
                new_qa['question'] = string_question
                new_qa['answer'] = question['answer']
                new_qa['query_id'] = question['query_id']
                
                json_list.append( new_qa )
                
            #print( json_list )
            
            passage_data['qa_pairs'] = json_list
            
            complete_json_list[ key ] = passage_data 
            
with jsonlines.open( '/Users/sharadhi/Documents/Third_semester/NLP/drop_dataset/train_output.json' , mode = 'a' ) as writer:
        
   writer.write( complete_json_list )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    