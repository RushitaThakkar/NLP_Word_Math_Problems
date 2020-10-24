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

with open('/Users/sharadhi/Documents/Third_semester/NLP/Project/MathQA/train.json') as f:
    
    data = json.load(f)
    
    json_list = []
    
    for index in range( 0 , len( data ) ):
    
        print( index )
        
        question = data[ index ]
        
        problem = question[ 'Problem' ]
        
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
                
                print( words[ i ] )
                
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
        
        find_str = question[ 'correct' ] + " )"
        
        start_ind = question[ 'options' ].find( find_str )
        
        end_ind = question[ 'options' ][ start_ind + 4 : ].find( ',' )
        
        ans = question[ 'options' ][ start_ind + 4 : start_ind + 4 + end_ind ]
        
        new_question = {}
        
        new_question[ 'ID' ] = index + 1
        
        new_question[ 'Passage' ] = ''
        
        new_question[ 'Question' ] = string_question
        
        new_question[ 'Equation' ] = question[ 'annotated_formula' ]
        
        new_question[ 'Answer' ] = ans
        
        new_question[ 'Reasoning Type' ] = question[ 'Rationale' ]
        
        new_question[ 'Type' ] = 'SJ_QwertyError'
       
        json_list.append( new_question )
    
    with jsonlines.open( '/Users/sharadhi/Documents/Third_semester/NLP/Project/MathQA/output.json' , mode = 'a' ) as writer:
        
        for k in range( 0 , len( json_list ) ):
            
            writer.write( json_list[ k ] )
    
    
    
    
    
    
    
        
        