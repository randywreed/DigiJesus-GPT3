import os
import openai

import configparser

from openai.api_resources import engine
config=configparser.ConfigParser()
config.read('openaigpt3.ini')
API_KEY=config['DEFAULT']['api_key']

openai.api_key=API_KEY

prompt=(
    "extract quote from passage\n"
    "passage:But Jesus answered, Permit it now ; for thus must we do to accomplish all that is right. Then he permitted him.\n"
    "quote:Permit it now; for thus must we do to accomplish all that is right.\n"
    "###\n"
    'passage:But Jesus answered, It is written, Man shall not live by bread alone, but in whatever way God may ordain.\n'
    'quote:It is written, Man shall not live by bread alone, but in whatever way God may ordain.\n'
    '###\n'
    'passage:Jesus said to him, It is written also, Thou shalt not make trial of the LoRD, thy God.\n'
    'quote:It is written also, Thou shalt not make trial of the LoRD, thy God.\n'
    '###\n'
    'passage:FROM that time Jesus began to preach, saying, Reform; for the kingdom of Heaven is at hand.\n'
    'quote:Reform; for the kingdom of Heaven is at hand.\n'
    '###\n'
    'passage:And lo. they brought to him a man with a palsy, lying on a bed. And Jesus, perceiving their faith, said to the paralytic, Take courage, s son | your sins have been forgiven.\n'
    'quote:Take courage, s son | your sins have been forgiven.\n'
    '###\n'
    'passage:And as Jesus was going thence, he saw a man, called Matthew, sitting to receive the cus toms; and said to him, Be my follower. And he arose and went with him.\n'
    'quote:'
)
response=openai.Classification.create(engine='davinci', prompt=prompt)
print(prompt)
with open('prompt.txt',"w") as f:
    f.write(prompt)