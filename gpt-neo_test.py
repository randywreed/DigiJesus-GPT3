from transformers import pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
while True:
    geninput=input('enter start: ')
    
    if len(geninput)<2:
        geninput=oldgeninput
    minl=len(geninput)+100
    print(minl)
    out=generator(geninput, do_sample=True, min_length=len(geninput),max_length=minl)
    print (out)
    oldgeninput=geninput