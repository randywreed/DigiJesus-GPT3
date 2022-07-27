import openai
import json
import sys
import os
import pandas as pd
import numpy as np
# import modules necessary for tokenization
from nltk.tokenize import word_tokenize
from transformers import GPT2TokenizerFast

tokenizer=GPT2TokenizerFast.from_pretrained('gpt2')
# load data from Jesus_sayings_final_v6.pkl into dataframe
df = pd.read_pickle('Jesus_sayings_final_v6.pkl')
token_count=0
word_count=0
for idx, i in df.iterrows():
    #print(df.iloc[i]['Text'])
    # print('words=',len(df.iloc[i]['Text'].split()))
    # print('tokens=',len(tokenizer.tokenize(df.iloc[i]['Text'])))
    # print('\n')
    token_count+=len(tokenizer.tokenize(i['Text']))
    word_count+=len(i['Text'].split())
print('token_count=',token_count)
print('word_count=',word_count)
print('openai charge=',(token_count/1000)*0.03)
# count the total number of tokens in the 'Text' column
# df['token_count'] = df['Text'].apply(lambda x: len(tokenizer(x)))
# # sum the number in the 'token_count' column
# token_total=df['token_count'].sum()
# # print the total number of tokens
# print('Total number of tokens:', token_total)
# openai_charge=(token_total/1000)*0.03
# print('OpenAI charge:', openai_charge)