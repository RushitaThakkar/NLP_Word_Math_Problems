# -*- coding: utf-8 -*-
"""
@author: kalp
"""

from googletrans import Translator
translator = Translator()
s1='How much probability does coin has of getting four heads in a row'
temp_translate=translator.translate(s1,src='en',dest='hi')
s2=translator.translate(temp_translate.text,src='hi',dest='en')
new_text=s2.text

####     Trying with different types of Data from MathQA

####     Importing and Pre-processing of data
