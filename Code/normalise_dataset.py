# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:42:00 2020

@author: shivi
"""


import numpy as np
import csv
import pandas  as pd
from numpy import linalg as LNG 

df = pd.read_csv("final_dataset.csv")

#print(df.head())

np_export = df['Export'].to_numpy()

df = df.replace('NA', np.nan)
df = df.replace(np.nan,0)


df['Export']= (df['Export'].to_numpy())/max(df['Export'].to_numpy())
df['Import']= (df['Import'].to_numpy())/max(df['Import'].to_numpy())

print(df.columns)

df['Border'] = (df['Border'].to_numpy()/max(df['Border'].to_numpy()))
df['Religion_conflicts'] = (df['Religion_conflicts'].to_numpy()/max(df['Religion_conflicts'].to_numpy()))


df['Exchange Rate'] = df['Exchange Rate'].apply(lambda x: 1 if x>1 else -1)


df = df.assign(Score = lambda x: (  (5*x['Export']) +(5*x['Import']) -(3.0*x['War']) +(2*x['Border']) +(0.8*x['Diplomatic']) -(0.5*x['International Cases']) +(0.125*x['Treaties']) +(0.5*x['Exchange Rate']) -(2*x['Religion_conflicts'])                   
                                  
                                  )) 
  


x= df['Score'].to_numpy()
p=0
n=0
for each in x:
    if each>0 :
        p+=1
    else:
        n+=1
        
df.to_csv('score.csv')


dc={
    }

for index, row in df.iterrows(): 
        
    A = row['Source'].lower().strip().replace(' ','-')
    B = row['Target'].lower().strip().replace(' ','-')
    
    dc[(A,B)] = row['Score']
    
print(len(dc.keys()))

def add_row(row): 
    with open(r'sign_score_dataset_test.csv', 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
    f.close();

    


list_of_all_countries_trading_economics = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'antigua-barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'bosnia-herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina-Faso', 'Burundi', 'Cape-Verde', 'Cambodia', 'Cameroon', 'Canada', 'central-african-republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'congo','republic-congo', 'Costa-Rica', 'Ivory-Coast', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'dominican-republic', 'Ecuador', 'Egypt', 'El-Salvador', 'Equatorial-Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta','Marshall-Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New-Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North-Korea', 'macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua-New-Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'st-kitts-nevis', 'Saint-Lucia', 'st-vincent-grenadines', 'Samoa', 'San-Marino', 'sao-tome-principe', 'Saudi-Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra-Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon-Islands', 'Somalia', 'South-Africa', 'South-Korea', 'South-Sudan', 'Spain', 'Sri-Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'East-Timor', 'Togo', 'Tonga', 'Trinidad-Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United-Arab-Emirates', 'United-Kingdom', 'United-States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'vatican-city-state', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']



for i in range(0,len(list_of_all_countries_trading_economics)):
    print(i)
    for j in  range(i+1,len(list_of_all_countries_trading_economics)):
        
        if i!=j:
            
            A= list_of_all_countries_trading_economics[i].lower().strip().replace(' ','-')
            B= list_of_all_countries_trading_economics[j].lower().strip().replace(' ','-')
            
            temp=[]
            temp.append(list_of_all_countries_trading_economics[i])
            temp.append(list_of_all_countries_trading_economics[j])
            final_score=dc[(A,B)] + dc[(B,A)] 
            temp.append( final_score)
            
            if(final_score>0):
                temp.append('+')
            else:
                temp.append('-')
            
            add_row(temp)
            print(temp)
            
        
 
     


"""


dc={}
for index, row in df.iterrows(): 
        #print (row["Source"], row["Target"]) 
        A = row['Exchange Rate']
        
        dc[A]=A
        
print(dc)

for index, row in df.iterrows(): 
        #print (row["Source"], row["Target"]) 
        A = row["Source"].lower()
        B = row["Target"].lower()
        
        
        
        
lng = max(np_export)
print(1/lng)

print(min(df['Export']))
#print(df['Export'])
np_export = df['Export'].to_numpy()
x = np.sort(-np_export)
print(-x[:10])
print(np.min(np_export[np.nonzero(np_export)]))


x = np.sort(np_export)
print(x[:100])
print(np.max(np_export[np.nonzero(np_export)]))

""" 