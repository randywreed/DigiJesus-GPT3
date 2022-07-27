import openai
import json
import sys
import os
import pandas as pd
import numpy as np
import configparser

# get openai api key from file openai_api_key.ini
config = configparser.ConfigParser()
config.read('openai_api_key.ini')
api_key = config.get('DEFAULT', 'openai_api_key')
openai.api_key = api_key

# load Jesus_sayings_final_v6.pkl into dataframe
df = pd.read_pickle('Jesus_sayings_final_v6.pkl')

#df columns = Version', 'Book', 'Chapter', 'Verse', 'Text'
# select subset of df to extract where Book="Mark" 
books=['Mark','Luke','John','Matthew']
for b in books:
    df_subset = df[df['Book'] == b]
    #df_subset.to_pickle(b+'_Jesus_sayings_final_v6.pkl')
    # save 'Text' column of df-subset to jsonl file
    df_subset['Text'].to_json('Jesus_'+b+'_sayings_final_v6.jsonl', orient='records', lines=True)

