import pandas as pd

# load 'Questions for Jesus -.7 currie.csv' into dataframe
df = pd.read_csv('Questions for Jesus - Curie_generic.csv')
model="curie_generic"
#df = pd.read_csv('Questions for Jesus - djTemp0.7.csv')
#model="djTemp0.7"
""" df is a dataframe with columns 'category' 'Questions' 'Answer 1' 'Answer 2' 'Answer 3'
create a long dataframe with columns 'category' 'Questions' 'Answer'
""" 
temp=0.7
df=df.reset_index()
df_long = pd.DataFrame(columns=['_ddqual_Question','_ddqual_Answer','Model','Temp','Category'])
for idx, i in df.iterrows():
    df_long = df_long.append({'_ddqual_Question':i['Questions'],'_ddqual_Answer':i['Answer 1'].replace('\n',' ').replace('"','').replace('\r',''),'Model':model,'Temp':temp,'Category':i['category']}, ignore_index=True)
    df_long = df_long.append({'_ddqual_Question':i['Questions'],'_ddqual_Answer':i['Answer 2'].replace('\n',' ').replace('"','').replace('\r',''),'Model':model,'Temp':temp,'Category':i['category']}, ignore_index=True)
    df_long = df_long.append({'_ddqual_Question':i['Questions'],'_ddqual_Answer':i['Answer 3'].replace('\n',' ').replace('"','').replace('\r',''),'Model':model,'Temp':temp,'Category':i['category']}, ignore_index=True)
#delete first column of df_long
#df_long.drop(df_long.columns[0], axis=1, inplace=True)
print(df_long.head())
# save dataframe to csv file
#df_long.to_csv('Questions_for_Jesus_digJ07_long.csv',index=False)
df_long.to_csv('Questions_for_Jesus_curie_gen_long.csv',index=False)
print("done")
