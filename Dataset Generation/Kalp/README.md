# NLP_Word_Math_Problems
CSE-576-Word Math Problems
Arizona State University

Methods Im working on.
1. Changing Question grammer by translating it to one language and the again translating to English.
  - This method is as simple as it sounds. First you translate a question into some intermediate language and then you translate it back to English language. 
  - I have chosen Intermediate Language as Germany since It is gramatically close to English. Due to underlying algorithm used for Language translation (LSTM/RNN Encoders Decoders) It will output different sentance structure than the original one but it will keep it's meaning same as original one most of the time.
  -I have used GoogleTrans API which is not officialy by Google but it calls to Google Translate API in the backend. 

## Folder Structure   
   
dataset_generation.py: Generates New samples from MathQA data set and saves as JSON file. For MathQA dataset it will also create dataset category wise for each category. \
  Before running: Change the file path in Line 41 to dataset from which new samples needs to be generated \
  Steps to run: Simpally running code from command line or IDE would create new samples.     \
    - Googletrans will block your IP if requested for too many times. I suggest using VPN for running code.   \
    
dataset_conversion.py: This file converts generated JSON files into required Uniform format JSONL file.  \

created_dataset_comparision: This file has script to compare generated samples with original samples. It shows metric for how much they match with original one. \
   

2. Paraphrasing Question manually using NLTK
Not able to Implement full method. Will upload scripts of the progress made so far.
