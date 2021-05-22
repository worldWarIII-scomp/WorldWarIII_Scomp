
import csv
import requests
import pandas  as pd
from bs4 import BeautifulSoup

def get_war(A,B):
    
    URL='https://en.wikipedia.org/wiki/List_of_wars_involving_'+A;
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    html = soup.prettify()
    #print(html)
    B=B.replace('_',' ')
    html = html[:html.find('References')]
    if html.find(B)!=-1 and html.find('Wikipedia does not have an article with this exact name') ==-1:
        return 1
    elif html.find(B)==-1 and html.find('Wikipedia does not have an article with this exact name') ==-1:
        return 0
    else:
        return (-1) #NA

def get_diplomatic_relation_or_embassy(A,B):
    
    URL='https://en.wikipedia.org/wiki/List_of_diplomatic_missions_of_'+A;
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    html = soup.prettify()
    B=B.replace('_',' ')
    #print("B is :" + B+":")
    if html.find(B)!=-1 and html.find('Wikipedia does not have an article with this exact name') ==-1:
        return 1
    elif html.find(B)==-1 and html.find('Wikipedia does not have an article with this exact name') ==-1:
        return 0
    else:
        return (-1)  #NA

def get_imports(A,B,A_index_factor,B_index_factor):
    
    URL = 'https://tradingeconomics.com/'+A+'/imports/'+B
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='ctl00_ContentPlaceHolder1_Comtrade_LabelShortDescription')
    if results is None:
      print("trying again found none for "+A+" "+B)
      return get_imports(A,B,A_index_factor,B_index_factor) #if adv disturb the page
      

    a= results.prettify()
    a=a[68:]
    p= a.split(' ')
    v= p[6+A_index_factor+ B_index_factor][3:]
    mo=p[7+A_index_factor+ B_index_factor]
    if mo=="Million":
        return (float(v)*1000000)
    elif mo=="Billion":
        return (float(v)*1000000000)
    elif mo=="Thousand":
        return (float(v)*1000)
    elif mo=="during":
        return float(v)
    elif p[1]=="Historical":
        return float(0)
    else :
        print(mo +" In Imports , Found new currency units for "+A+" "+B )
        return -1


def get_exports(A,B,A_index_factor,B_index_factor):
    
    URL = 'https://tradingeconomics.com/'+A+'/exports/'+B
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='ctl00_ContentPlaceHolder1_Comtrade_LabelShortDescription')
    if results is None:
      print("trying again found none for "+A+" "+B)
      return get_exports(A,B,A_index_factor,B_index_factor)
      

    a= results.prettify()
    a=a[68:]
    p= a.split(' ')
    v= p[6+A_index_factor+ B_index_factor][3:]
    mo=p[7+A_index_factor+ B_index_factor]
    
    if mo=="Million":
        return (float(v)*1000000)
    elif mo=="Billion":
        return (float(v)*1000000000)
    elif mo=="Thousand":
        return (float(v)*1000)
    elif mo=="during":
        return float(v)
    elif p[1]=="Historical":
        return float(0)
    else :
        print(mo +" In Exports, Found new currency units for "+A+" "+B )
        return -1

def add_row(row): 
    with open(r'data1.csv', 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
    f.close();

    

list_of_all_countries =['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua_and_Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh','Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia_and_Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina_Faso', 'Burundi', 'Cape_Verde', 'Cambodia', 'Cameroon', 'Canada', 'the_Central_African_Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'the_Democratic_Republic_of_the_Congo', 'the_Republic_of_the_Congo', 'Costa_Rica', 'Ivory_Coast', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'the_Dominican_Republic', 'Ecuador', 'Egypt', 'El_Salvador', 'Equatorial_Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'the_Marshall_Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New_Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North_Korea', 'North_Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua_New_Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint_Kitts_and_Nevis', 'Saint_Lucia', 'Saint_Vincent_and_the_Grenadines', 'Samoa', 'San_Marino', 'Sao_Tome_and_Principe', 'Saudi_Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra_Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon_Islands', 'Somalia', 'South_Africa', 'South_Korea', 'South_Sudan', 'Spain', 'Sri_Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'East_Timor', 'Togo', 'Tonga', 'Trinidad_and_Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United_Arab_Emirates', 'United_Kingdom', 'the_United_States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican_City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
list_of_all_countries_trading_economics = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'antigua-barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'bosnia-herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina-Faso', 'Burundi', 'Cape-Verde', 'Cambodia', 'Cameroon', 'Canada', 'central-african-republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'congo','republic-congo', 'Costa_Rica', 'Ivory-Coast', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'dominican-republic', 'Ecuador', 'Egypt', 'El-Salvador', 'Equatorial-Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta','Marshall-Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New-Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North-Korea', 'macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua-New-Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'st-kitts-nevis', 'Saint-Lucia', 'st-vincent-grenadines', 'Samoa', 'San-Marino', 'sao-tome-principe', 'Saudi-Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra-Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon-Islands', 'Somalia', 'South-Africa', 'South-Korea', 'South-Sudan', 'Spain', 'Sri-Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'East-Timor', 'Togo', 'Tonga', 'Trinidad-Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United-Arab-Emirates', 'United-Kingdom', 'United-States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'vatican-city-state', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
list_of_index_adjustment_economics=[0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 4, 0, 1, 3, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0]
list_of_index_adjustment_economics[26]=1
#list_of_all_countries=list_of_all_countries[:5]
#list_of_all_countries_trading_economics=list_of_all_countries_trading_economics[:5]
#list_of_index_adjustment_economics=list_of_index_adjustment_economics[:5]

ans=[]

for i in range(119+5,119+12):
    print(i)
    for j in  range(0,len(list_of_all_countries)):
        
        if i!=j:
            
            temp=[]
    
            x1= get_exports(list_of_all_countries_trading_economics[i],list_of_all_countries_trading_economics[j],list_of_index_adjustment_economics[i],list_of_index_adjustment_economics[j])
            x2= get_imports(list_of_all_countries_trading_economics[i],list_of_all_countries_trading_economics[j],list_of_index_adjustment_economics[i],list_of_index_adjustment_economics[j])    
            x3= get_diplomatic_relation_or_embassy(list_of_all_countries[i],list_of_all_countries[j])
            x4= get_war(list_of_all_countries[i],list_of_all_countries[j])
            
            temp.append(list_of_all_countries_trading_economics[i])
            temp.append(list_of_all_countries_trading_economics[j])
            temp.append(x1)
            temp.append(x2)
            temp.append(x3)
            temp.append(x4)
            print(temp)
            add_row(temp)
            ans.append(temp)
            
print(ans)

