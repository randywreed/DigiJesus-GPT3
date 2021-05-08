#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/randywreed/DigiJesus-GPT3/blob/main/digitaljesus_prompt_gpt_neo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:





# In[ ]:


get_ipython().system('pip install transformers')


# In[ ]:


import os
import transformers


# In[ ]:


#if not using gdrive
modelpath="EleutherAI/gpt-neo-1.3B"
tokenpath="EleutherAI/gpt-neo-1.3B"


# In[ ]:


#skip if not using Gdrive 
from google.colab import drive
drive.mount('/content/gdrive')


# In[ ]:


#if using Gdrive (probably requires colab pro get's out of memory error)
modelpath='/content/gdrive/MyDrive/Data Analysis for Humanities/Jesus saying database/gptneomodel/model'
tokenpath='/content/gdrive/MyDrive/Data Analysis for Humanities/Jesus saying database/gptneomodel/tokenizer'


# In[ ]:


# download pretrained model and save to google drive. 
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model.save_pretrained(modelpath)
tokenizer.save_pretrained(tokenpath)


# In[ ]:


from transformers import pipeline
generator=pipeline('text-generation', model="EleutherAI/gpt-neo-1.3B",device=0)


# In[ ]:


from transformers import GPT2Tokenizer
tokenizer=GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B",device=0)


# In[ ]:





# In[ ]:


from transformers import pipeline, GPT2Tokenizer
generator = pipeline('text-generation', model="EleutherAI/gpt-neo-2.7B", device=0)


# In[ ]:


from transformers import GPT2Tokenizer
tokenizer=GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B", device=0)


# In[ ]:


import sys
from io import StringIO
from IPython import get_ipython


class IpyExit(SystemExit):
    """Exit Exception for IPython.

    Exception temporarily redirects stderr to buffer.
    """
    def __init__(self):
        # print("exiting")  # optionally print some message to stdout, too
        # ... or do other stuff before exit
        sys.stderr = StringIO()

    def __del__(self):
        sys.stderr.close()
        sys.stderr = sys.__stderr__  # restore from backup


def ipy_exit():
    raise IpyExit


if get_ipython():    # ...run with IPython
    exit = ipy_exit  # rebind to custom exit
else:
    exit = exit      # just make exit importable


# In[ ]:


import torch

with open("prompt.txt","r+") as promptfile:
    initprompt=promptfile.read()
    newpassflag=True
    while newpassflag:
        newpassage=input('enter new passage: ')
        prompt=initprompt+"\npassage:"+newpassage+"\nquote:"
        print(prompt)
        loopflag=True
        while loopflag:        
            minl=tokenizer(prompt, return_length=True)
            print(f'prompt length={minl.length}')
            passlen=tokenizer(newpassage,return_length=True)
            print(f'new prompt token length {passlen.length}')
            minl=int(input('enter max length: '))
            temparature=float(input('Enter tempreature: '))
            response=generator(prompt, do_sample=True,bs=2 ,max_length=minl, temperature=temparature)
            newresponse=response[0]['generated_text'].split("###")[-2]
            newsayings=newresponse.split('\n')
            print(f'prompt= {newsayings[1]}')
            print(f'quote={newsayings[2]}')
           
            #gc.collect()
            torch.cuda.empty_cache()
            #print(response)
            action=input('type correction, hit return to retry, a to add, x to stop, r to re-enter: ')
            if len(action)>1:
                promptfile.write(action+"\n###\n")
            else:
                if action=="a":
                    #print(response[0])
                    newprompt="\n"+newsayings[1]+"\n"+ newsayings[2]+"\n###"
                    import pdb; pdb.set_trace()
                    promptfile.write(newprompt)
                    loopflag=False
                    getmore=input('enter c to continue or x to exit')
                    if getmore=="x":
                        promptfile.close()
                        exit()
                else:
                    if action=="x":
                        promptfile.close()
                        exit()
                    else:
                        if action=="r":
                            loopflag=False


# In[ ]:


del generator
#gc.collect()
torch.cuda.empty_cache()


# In[ ]:




