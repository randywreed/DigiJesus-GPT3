import os
import openai
import configparser

from openai.api_resources import engine
config=configparser.ConfigParser()
config.read('openaigpt3.ini')
API_KEY=config['DEFAULT']['api_key']
openai.api_key=API_KEY
with open("prompt.txt","r+") as promptfile:
    initprompt=promptfile.read()
    newpassflag=True
    while newpassflag:
        newpassage=input('enter new passage: ')
        prompt=initprompt+"\npassage:"+newpassage+"\nquote:"
        print(prompt[-len(newpassage)+15])
        loopflag=True
        while loopflag:

            response = openai.Completion.create(
            engine="ada",
            prompt=prompt,
            temperature=0.7,
            max_tokens=int(len(newpassage)*.80),
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            print(response)
            action=input('type correction, hit return to retry, a to add, x to stop, r to re-enter: ')
            if len(action)>1:
                promptfile.write(action+"\n###\n")
            else:
                if action=="a":
                    newresponse=response.choices[0].text.split("###")
                    promptfile.write("\npassage: "+newpassage+"\nquote:"+ newresponse[0]+"###")
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
