# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 10:27:23 2020

@author: shivi
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import operator

def preprocess_data_for_graphs():
    
    df = pd.read_csv("final_dataset.csv")
    
    dc_exports={}  #add A to dict +value    Bar
    dc_imports={}   # '
    dc_dp={}        #  1 or 0 count         Pie 
    dc_war={}       # 1 or 0 count          Pie
    dc_border={}    #  dict of each key count    Pie  of 4
    dc_cases=set()    #   .add A and B to set       Pie of 0 or 1 
    dc_treaties ={} # count of 1 or 0            Pie
    dc_rc ={}       # count of key value          Pie of count 
    
    df = df.replace('NA', np.nan)
    df = df.replace(np.nan,0)
    
    
    print(df.columns)
    for index, row in df.iterrows(): 
            
        A = row['Source'].lower().strip().replace(' ','-')
        B = row['Target'].lower().strip().replace(' ','-')
        
        exports = row['Export']
        imports = row['Import']
        dp = row['Diplomatic']
        war = row['War']
        border = row['Border']
        int_cases = row['International Cases']
        treaties = row['Treaties']
        exc = row['Exchange Rate']
        rc = row['Religion_conflicts']
        
        if A in dc_exports.keys():
            dc_exports[A]+= exports
        else:
            dc_exports[A]=exports
        
        if A in dc_imports.keys():
            dc_imports[A]+= imports
        else:
            dc_imports[A]=imports
            
        
        if war in dc_war.keys():
            dc_war[war] +=1
        else:
            dc_war[war]=1
            
        
        if border in dc_border.keys():
            dc_border[border]+=1
        else:
            dc_border[border]=1
        
        if int_cases==1:
            dc_cases.add(A)
            dc_cases.add(B)
        
        if treaties in dc_treaties.keys():
            dc_treaties[treaties]+=1
        else:
            dc_treaties[treaties]=1
        
        if rc in dc_rc.keys():
            dc_rc[rc]+=1
        else:
            dc_rc[rc]=1
        
        
        if A in dc_dp.keys():
            if dp==1:
                dc_dp[A]+=1
        else:
            if dp==1:
                dc_dp[A]=1
            
    top_10_export  = dict(sorted(dc_exports.items(), key=operator.itemgetter(1), reverse=True)[:10])
    top_10_import  = dict(sorted(dc_imports.items(), key=operator.itemgetter(1), reverse=True)[:10])
    
    low_10_export = dict(sorted(dc_exports.items(), key=operator.itemgetter(1) )[:20])
    low_10_import = dict(sorted(dc_imports.items(), key=operator.itemgetter(1))[:20])
    
    top10_diplomatic =dict(sorted(dc_dp.items(), key=operator.itemgetter(1) , reverse=True)[:10])
    low10_diplomatic=dict(sorted(dc_dp.items(), key=operator.itemgetter(1) )[:20])
    
    print(dc_exports) #add A to dict +value    Bar
    print(dc_imports)  # '
    print(dc_dp)        #  1 or 0 count         Pie 
    print(dc_war)   # 1 or 0 count          Pie
    print(dc_border)   #  dict of each key count    Pie  of 4
    print(dc_cases)   #   .add A and B to set       Pie of 0 or 1 
    print("Lenght is "+str(len(dc_cases)))
    print(dc_treaties) # count of 1 or 0            Pie
    print(dc_rc)
    print(top_10_export)
    print(top_10_import)
    print(low_10_export)
    print(low_10_import)
    print(top10_diplomatic)
    print(low10_diplomatic)
    


"""
Preprocessed Data 

Exp={'afghanistan': 1319854770.0, 'albania': 2824592136.0, 'algeria': 30258138343.0, 'andorra': 127306786.0, 'angola': 41536517586.0, 'antigua-barbuda': 46170740.0, 'argentina': 63610423500.0, 'armenia': 2606718674.0, 'australia': 250536034030.0, 'austria': 163136814993.0, 'azerbaijan': 18778474781.0, 'bahamas': 174908828780.0, 'bahrain': 7277680904.0, 'bangladesh': 30713151402.0, 'barbados': 327955409.0, 'belarus': 31173140400.0, 'belgium': 433508510240.0, 'belize': 250557608.0, 'benin': 856113873.0, 'bhutan': 83613438530.0, 'bolivia': 9053809973.0, 'bosnia-herzegovina': 6475587637.0, 'botswana': 5777984997.0, 'brazil': 220848746060.0, 'brunei': 6879143204.0, 'bulgaria': 31460706807.0, 'burkina-faso': 3303722149.0, 'burundi': 172223452.0, 'cambodia': 12253790383.0, 'cameroon': 6532680074.0, 'canada': 441514864450.0, 'cape-verde': 90008061.0, 'central-african-republic': 44518266580.0, 'chad': 1572978860.0, 'chile': 67430245960.0, 'china': 2125260446530.0, 'colombia': 38407545670.0, 'comoros': 52080243.0, 'congo': 10860954480.0, 'costa-rica': 11957830130.0, 'croatia': 16705924958.0, 'cuba': 1112205153.0, 'cyprus': 2917673277.0, 'czechia': 219035125530.0, 'denmark': 126715312530.0, 'djibouti': 83051081740.0, 'dominica': 8932392890.0, 'dominican-republic': 8687143897.0, 'east-timor': 32121632.0, 'ecuador': 22230020374.0, 'egypt': 29913117578.0, 'el-salvador': 5648454104.0, 'equatorial-guinea': 6067088270.0, 'eritrea': 662943725710.0, 'estonia': 16481961717.0, 'eswatini': 0.0, 'ethiopia': 2272369563.0, 'fiji': 815727020.0, 'finland': 68369827677.0, 'france': 538593990710.0, 'gabon': 5507582723.0, 'gambia': 27726822.0, 'georgia': 3795148322.0, 'germany': 1408443429090.0, 'ghana': 16560485630.0, 'greece': 36370200386.0, 'grenada': 31170450.0, 'guatemala': 10407324048.0, 'guinea': 62018620379.0, 'guinea-bissau': 45486509890.0, 'guyana': 1485828037.0, 'haiti': 1243552640.0, 'honduras': 2448184576.0, 'hungary': 116384626412.0, 'iceland': 5092017723.0, 'india': 306006265450.0, 'indonesia': 160335297440.0, 'iran': 45662320746.0, 'iraq': 115647780.0, 'ireland': 165420380851.0, 'israel': 53509352000.0, 'italy': 507529632700.0, 'ivory-coast': 12549953012.0, 'jamaica': 1567998146.0, 'japan': 626167092990.0, 'jordan': 7291241090.0, 'kazakhstan': 57602021554.0, 'kenya': 5892297569.0, 'kiribati': 5235661240.0, 'kosovo': 0.0, 'kuwait': 6437480469.0, 'kyrgyzstan': 1986790944.0, 'laos': 5748188557.0, 'latvia': 14135474715.0, 'lebanon': 2893259265.0, 'lesotho': 661780217.0, 'liberia': 1359735890.0, 'libya': 27951584630.0, 'liechtenstein': 0.0, 'lithuania': 32512422773.0, 'luxembourg': 14501907588.0, 'macedonia': 7105338862.0, 'madagascar': 2576501082.0, 'malawi': 911997155.0, 'malaysia': 212369306400.0, 'maldives': 144166968480.0, 'mali': 3023706360.0, 'malta': 3205722710.0, 'marshall-islands': 7821986950.0, 'mauritania': 2724639780.0, 'mauritius': 1833377621.0, 'mexico': 430865364301.0, 'micronesia': 14203364140.0, 'moldova': 2621838830.0, 'monaco': 0.0, 'mongolia': 7601332941.0, 'montenegro': 408433015.0, 'morocco': 28623340899.0, 'mozambique': 5080888890.0, 'myanmar': 17621404832.0, 'namibia': 5806013245.0, 'nauru': 2795989590.0, 'nepal': 737997358.0, 'netherlands': 542806941410.0, 'new-zealand': 36771697941.0, 'nicaragua': 4996303838.0, 'niger': 931340801.0, 'nigeria': 61978016330.0, 'north-korea': 619752810.0, 'norway': 103183711262.0, 'oman': 14236914128.0, 'pakistan': 23556806334.0, 'palau': 7990694960.0, 'palestine': 1157302030.0, 'panama': 5782905280.0, 'papua-new-guinea': 4419333930.0, 'paraguay': 8982872621.0, 'peru': 45501985632.0, 'philippines': 58608559591.0, 'poland': 235193815700.0, 'portugal': 64591579039.0, 'qatar': 69944474230.0, 'republic-congo': 7859562929.0, 'romania': 74487743247.0, 'russia': 415634522675.0, 'rwanda': 1183560720.0, 'saint-lucia': 99208753.0, 'samoa': 26676360.0, 'san-marino': 716480713530.0, 'sao-tome-principe': 3793080.0, 'saudi-arabia': 61881838294.0, 'senegal': 3976064061.0, 'serbia': 18954088790.0, 'seychelles': 757017478.0, 'sierra-leone': 41445037040.0, 'singapore': 327773568840.0, 'slovakia': 79832462050.0, 'slovenia': 36559743000.0, 'solomon-islands': 550600346.0, 'somalia': 94919016300.0, 'south-africa': 80122127077.0, 'south-korea': 491322154170.0, 'south-sudan': 1851568950.0, 'spain': 310292630730.0, 'sri-lanka': 11400722266.0, 'st-kitts-nevis': 32210800.0, 'st-vincent-grenadines': 38905441.0, 'sudan': 3614916605.0, 'suriname': 901246914.0, 'sweden': 153210601030.0, 'switzerland': 299205232623.0, 'syria': 11056274712.0, 'taiwan': 844141600000.0, 'tajikistan': 241920679630.0, 'tanzania': 3589393297.0, 'thailand': 217740684160.0, 'togo': 1001943299.0, 'tonga': 12428869.0, 'trinidad-tobago': 10540012805.0, 'tunisia': 13861360578.0, 'turkey': 163520339501.0, 'turkmenistan': 9366939490.0, 'tuvalu': 1312206590.0, 'uganda': 3029391422.0, 'ukraine': 46108721727.0, 'united-arab-emirates': 166660334081.0, 'united-kingdom': 441579829250.0, 'united-states': 1565773285610.0, 'uruguay': 6658238390.0, 'uzbekistan': 8402613467.0, 'vanuatu': 65856751.0, 'vatican-city-state': 0.0, 'venezuela': 2131805530.0, 'vietnam': 230129708188.0, 'yemen': 354351745.0, 'zambia': 6958172632.0, 'zimbabwe': 3532997390.0}
Imp={'afghanistan': 106873818910.0, 'albania': 5849502073.0, 'algeria': 46777882556.0, 'andorra': 1586365786.0, 'angola': 15938314400.0, 'antigua-barbuda': 541859459.0, 'argentina': 48007462704.0, 'armenia': 4992172214.0, 'australia': 212611321600.0, 'austria': 165076823152.0, 'azerbaijan': 13574823029.0, 'bahamas': 781403174754.0, 'bahrain': 20371416864.0, 'bangladesh': 43686003991.0, 'barbados': 1577852967.0, 'belarus': 37658023500.0, 'belgium': 419103199129.0, 'belize': 952380605.0, 'benin': 2889649117.0, 'bhutan': 724596875149.0, 'bolivia': 9961952526.0, 'bosnia-herzegovina': 10908551529.0, 'botswana': 5847693907.0, 'brazil': 167055418759.0, 'brunei': 4962111313.0, 'bulgaria': 35919553202.0, 'burkina-faso': 4359757976.0, 'burundi': 778093070.0, 'cambodia': 16105871740.0, 'cameroon': 10357034476.0, 'canada': 444271142913.0, 'cape-verde': 786149989.0, 'central-african-republic': 688341937612.0, 'chad': 170279857370.0, 'chile': 67149257360.0, 'china': 1795200005840.0, 'colombia': 50866899692.0, 'comoros': 208286528.0, 'congo': 25433176740.0, 'costa-rica': 15227043320.0, 'croatia': 27168870991.0, 'cuba': 6369277756.0, 'cyprus': 8950506214.0, 'czechia': 201344202600.0, 'denmark': 113521287987.0, 'djibouti': 717034011596.0, 'dominica': 646802416012.0, 'dominican-republic': 18903514064.0, 'east-timor': 525347166.0, 'ecuador': 19935499810.0, 'egypt': 77606945261.0, 'el-salvador': 11549882092.0, 'equatorial-guinea': 242085057650.0, 'eritrea': 45727166822.0, 'estonia': 17264497088.0, 'eswatini': 0.0, 'ethiopia': 15639168529.0, 'fiji': 2649355422.0, 'finland': 69859249962.0, 'france': 611371341200.0, 'gabon': 2484788794.0, 'gambia': 493658044.0, 'georgia': 9351797194.0, 'germany': 1137769203420.0, 'ghana': 10284364845.0, 'greece': 59765247568.0, 'grenada': 280322761.0, 'guatemala': 18564101262.0, 'guinea': 2950107578.0, 'guinea-bissau': 728571270454.0, 'guyana': 3976088975.0, 'haiti': 109971065100.0, 'honduras': 8704964615.0, 'hungary': 109848253990.0, 'iceland': 6416638432.0, 'india': 456784494602.0, 'indonesia': 163463452978.0, 'iran': 51165611036.0, 'iraq': 31821140860.0, 'ireland': 92582931751.0, 'israel': 70453305000.0, 'italy': 461287311770.0, 'ivory-coast': 10270658917.0, 'jamaica': 6237263452.0, 'japan': 689724083860.0, 'jordan': 18768137155.0, 'kazakhstan': 38059146682.0, 'kenya': 17104623716.0, 'kiribati': 686722309895.0, 'kosovo': 0.0, 'kuwait': 35480079738.0, 'kyrgyzstan': 4951325855.0, 'laos': 5745093317.0, 'latvia': 17420688640.0, 'lebanon': 19750488725.0, 'lesotho': 1941307292.0, 'liberia': 43516361930.0, 'libya': 448811018310.0, 'liechtenstein': 0.0, 'lithuania': 34660223002.0, 'luxembourg': 21241199947.0, 'macedonia': 9280505864.0, 'madagascar': 3507163523.0, 'malawi': 2871937542.0, 'malaysia': 187257677755.0, 'maldives': 742479586303.0, 'mali': 38100739270.0, 'malta': 8031243700.0, 'marshall-islands': 741361083812.0, 'mauritania': 8377036010.0, 'mauritius': 5462728542.0, 'mexico': 440955456736.0, 'micronesia': 752184809572.0, 'moldova': 5640303071.0, 'monaco': 0.0, 'mongolia': 6096534319.0, 'montenegro': 2947095333.0, 'morocco': 50346212187.0, 'mozambique': 6662016478.0, 'myanmar': 18428673569.0, 'namibia': 7527742254.0, 'nauru': 697388865726.0, 'nepal': 9789266079.0, 'netherlands': 490765342780.0, 'new-zealand': 41308793331.0, 'nicaragua': 6506337962.0, 'niger': 1860238941.0, 'nigeria': 42525034528.0, 'north-korea': 400106214440.0, 'norway': 84376567540.0, 'oman': 25136003313.0, 'pakistan': 48720952639.0, 'palau': 682216425206.0, 'palestine': 6485307790.0, 'panama': 420386630480.0, 'papua-new-guinea': 8125385812.0, 'paraguay': 13181517862.0, 'peru': 41890413534.0, 'philippines': 108410169356.0, 'poland': 235124196133.0, 'portugal': 88215981400.0, 'qatar': 27980907369.0, 'republic-congo': 4548418537.0, 'romania': 93426778413.0, 'russia': 237977922803.0, 'rwanda': 3171676303.0, 'saint-lucia': 612199533.0, 'samoa': 368833048.0, 'san-marino': 56988857726.0, 'sao-tome-principe': 149790634.0, 'saudi-arabia': 132942783673.0, 'senegal': 8465456324.0, 'serbia': 25848871222.0, 'seychelles': 1318816380.0, 'sierra-leone': 689690109748.0, 'singapore': 322444191151.0, 'slovakia': 72545933449.0, 'slovenia': 36697576128.0, 'solomon-islands': 542166499.0, 'somalia': 749493986995.0, 'south-africa': 83908668259.0, 'south-korea': 481901434231.0, 'south-sudan': 5674932514050.0, 'spain': 348607569298.0, 'sri-lanka': 20358374956.0, 'st-kitts-nevis': 303129269.0, 'st-vincent-grenadines': 332982055.0, 'sudan': 10394998707.0, 'suriname': 1440700530.0, 'sweden': 154139403265.0, 'switzerland': 268124363159.0, 'syria': 17143710668.0, 'taiwan': 599788.0, 'tajikistan': 231592344471.0, 'tanzania': 8414757869.0, 'thailand': 203155911583.0, 'togo': 1859894490.0, 'tonga': 214140080.0, 'trinidad-tobago': 6430679953.0, 'tunisia': 20651932258.0, 'turkey': 206176343338.0, 'turkmenistan': 370058247940.0, 'tuvalu': 714064719814.0, 'uganda': 6689930086.0, 'ukraine': 55663630848.0, 'united-arab-emirates': 238490844329.0, 'united-kingdom': 660555422910.0, 'united-states': 2494572258780.0, 'uruguay': 8005298915.0, 'uzbekistan': 21592045681.0, 'vanuatu': 271604931.0, 'vatican-city-state': 0.0, 'venezuela': 43958512722.0, 'vietnam': 220552520329.0, 'yemen': 4451173572.0, 'zambia': 7126426542.0, 'zimbabwe': 4667618525.0}
diplo={'afghanistan': 81, 'albania': 64, 'algeria': 115, 'andorra': 51, 'angola': 83, 'antigua-barbuda': 29, 'argentina': 85, 'armenia': 101, 'australia': 87, 'austria': 93, 'azerbaijan': 123, 'bahrain': 61, 'bangladesh': 110, 'barbados': 51, 'belarus': 82, 'belgium': 104, 'belize': 29, 'benin': 71, 'bhutan': 53, 'bolivia': 38, 'bosnia-herzegovina': 66, 'botswana': 70, 'brazil': 185, 'brunei': 87, 'bulgaria': 90, 'burkina-faso': 75, 'burundi': 67, 'cambodia': 61, 'cameroon': 71, 'canada': 128, 'cape-verde': 178, 'central-african-republic': 63, 'chad': 66, 'chile': 79, 'china': 193, 'colombia': 65, 'comoros': 61, 'congo': 77, 'costa-rica': 53, 'croatia': 77, 'cuba': 126, 'cyprus': 100, 'denmark': 125, 'djibouti': 67, 'dominica': 27, 'dominican-republic': 56, 'east-timor': 62, 'ecuador': 44, 'egypt': 147, 'el-salvador': 51, 'equatorial-guinea': 69, 'eritrea': 75, 'estonia': 57, 'eswatini': 63, 'ethiopia': 87, 'fiji': 24, 'finland': 94, 'france': 165, 'gabon': 68, 'georgia': 107, 'germany': 186, 'ghana': 86, 'greece': 99, 'grenada': 29, 'guatemala': 54, 'guinea': 75, 'guinea-bissau': 66, 'guyana': 42, 'haiti': 48, 'honduras': 42, 'hungary': 98, 'iceland': 61, 'india': 184, 'indonesia': 189, 'iran': 144, 'iraq': 169, 'ireland': 84, 'israel': 140, 'italy': 129, 'ivory-coast': 78, 'jamaica': 36, 'japan': 162, 'jordan': 175, 'kazakhstan': 100, 'kenya': 106, 'kiribati': 18, 'kosovo': 89, 'kuwait': 174, 'kyrgyzstan': 60, 'laos': 186, 'latvia': 58, 'lebanon': 93, 'lesotho': 67, 'liberia': 66, 'libya': 119, 'liechtenstein': 50, 'lithuania': 60, 'luxembourg': 63, 'macedonia': 59, 'madagascar': 69, 'malawi': 61, 'malaysia': 173, 'mali': 71, 'malta': 65, 'marshall-islands': 20, 'mauritania': 75, 'mauritius': 65, 'mexico': 132, 'moldova': 55, 'monaco': 49, 'mongolia': 68, 'montenegro': 57, 'morocco': 115, 'mozambique': 70, 'myanmar': 66, 'namibia': 76, 'nauru': 20, 'nepal': 61, 'netherlands': 117, 'new-zealand': 72, 'nicaragua': 52, 'niger': 66, 'nigeria': 106, 'north-korea': 105, 'norway': 101, 'oman': 70, 'pakistan': 100, 'palau': 84, 'palestine': 120, 'panama': 67, 'papua-new-guinea': 26, 'paraguay': 42, 'peru': 65, 'poland': 100, 'portugal': 115, 'qatar': 113, 'republic-congo': 65, 'romania': 105, 'russia': 188, 'rwanda': 69, 'saint-lucia': 28, 'samoa': 18, 'san-marino': 52, 'sao-tome-principe': 63, 'saudi-arabia': 178, 'senegal': 83, 'serbia': 179, 'seychelles': 66, 'sierra-leone': 63, 'singapore': 74, 'slovakia': 116, 'slovenia': 62, 'solomon-islands': 154, 'somalia': 79, 'south-africa': 118, 'south-korea': 128, 'south-sudan': 67, 'spain': 187, 'sri-lanka': 80, 'st-kitts-nevis': 28, 'st-vincent-grenadines': 28, 'sudan': 96, 'suriname': 22, 'sweden': 112, 'switzerland': 119, 'syria': 85, 'taiwan': 168, 'tajikistan': 58, 'tanzania': 75, 'thailand': 175, 'togo': 185, 'tonga': 24, 'trinidad-tobago': 44, 'tunisia': 101, 'turkey': 187, 'turkmenistan': 60, 'tuvalu': 26, 'uganda': 70, 'ukraine': 184, 'united-kingdom': 168, 'united-states': 189, 'uruguay': 66, 'uzbekistan': 63, 'vanuatu': 19, 'vatican-city-state': 145, 'venezuela': 96, 'vietnam': 174, 'yemen': 77, 'zambia': 71, 'zimbabwe': 75}
dc_cases={'thailand', 'india', 'bulgaria', 'qatar', 'niger', 'saudi-arabia', 'colombia', 'macedonia', 'netherlands', 'senegal', 'ecuador', 'canada', 'ethiopia', 'belgium', 'greece', 'liechtenstein', 'turkey', 'paraguay', 'guatemala', 'serbia', 'cambodia', 'malta', 'rwanda', 'guinea-bissau', 'congo', 'italy', 'indonesia', 'mali', 'bolivia', 'united-states', 'finland', 'slovakia', 'australia', 'sweden', 'israel', 'bahrain', 'burundi', 'namibia', 'romania', 'albania', 'argentina', 'france', 'peru', 'burkina-faso', 'uruguay', 'brazil', 'dominica', 'spain', 'benin', 'united-arab-emirates', 'switzerland', 'bosnia-herzegovina', 'cameroon', 'iran', 'germany', 'chad', 'marshall-islands', 'mexico', 'ukraine', 'croatia', 'denmark', 'malaysia', 'chile', 'tunisia', 'liberia', 'south-africa', 'russia', 'nauru', 'new-zealand', 'botswana', 'singapore', 'iceland', 'pakistan', 'nigeria', 'el-salvador', 'nicaragua', 'libya', 'east-timor', 'georgia', 'ireland', 'portugal', 'lebanon', 'egypt', 'honduras', 'hungary', 'norway', 'djibouti', 'united-kingdom', 'montenegro', 'japan'}



Use lower for charts & graphs 
countires_have_past_war = {0.0: 35074, 1.0: 3538}
border = {0: 37444, -1: 20, 2: 998, 1: 150}
dc_cases=Lenght is 90
counties_having_treaties ={0: 38064, 1: 548}
count_of_religion_conflict = {0: 8671, 1: 21421, 2: 7965, 3: 541, 4: 14}
top10_export={'china': 2125260446530.0, 'united-states': 1565773285610.0, 'germany': 1408443429090.0, 'taiwan': 844141600000.0, 'san-marino': 716480713530.0, 'eritrea': 662943725710.0, 'japan': 626167092990.0, 'netherlands': 542806941410.0, 'france': 538593990710.0, 'italy': 507529632700.0}
top10_import={'south-sudan': 5674932514050.0, 'united-states': 2494572258780.0, 'china': 1795200005840.0, 'germany': 1137769203420.0, 'bahamas': 781403174754.0, 'micronesia': 752184809572.0, 'somalia': 749493986995.0, 'maldives': 742479586303.0, 'marshall-islands': 741361083812.0, 'guinea-bissau': 728571270454.0}
low10_export={'eswatini': 0.0, 'kosovo': 0.0, 'liechtenstein': 0.0, 'monaco': 0.0, 'vatican-city-state': 0.0, 'sao-tome-principe': 3793080.0, 'tonga': 12428869.0, 'samoa': 26676360.0, 'gambia': 27726822.0, 'grenada': 31170450.0, 'east-timor': 32121632.0, 'st-kitts-nevis': 32210800.0, 'st-vincent-grenadines': 38905441.0, 'antigua-barbuda': 46170740.0, 'comoros': 52080243.0, 'vanuatu': 65856751.0, 'cape-verde': 90008061.0, 'saint-lucia': 99208753.0, 'iraq': 115647780.0, 'andorra': 127306786.0}
low10_import={'eswatini': 0.0, 'kosovo': 0.0, 'liechtenstein': 0.0, 'monaco': 0.0, 'vatican-city-state': 0.0, 'taiwan': 599788.0, 'sao-tome-principe': 149790634.0, 'comoros': 208286528.0, 'tonga': 214140080.0, 'vanuatu': 271604931.0, 'grenada': 280322761.0, 'st-kitts-nevis': 303129269.0, 'st-vincent-grenadines': 332982055.0, 'samoa': 368833048.0, 'gambia': 493658044.0, 'east-timor': 525347166.0, 'antigua-barbuda': 541859459.0, 'solomon-islands': 542166499.0, 'saint-lucia': 612199533.0, 'burundi': 778093070.0}
top10_diplomatic = {'china': 193, 'indonesia': 189, 'united-states': 189, 'russia': 188, 'spain': 187, 'turkey': 187, 'germany': 186, 'laos': 186, 'brazil': 185, 'togo': 185}
low20_diplomatic = {'kiribati': 18, 'samoa': 18, 'vanuatu': 19, 'marshall-islands': 20, 'nauru': 20, 'suriname': 22, 'fiji': 24, 'tonga': 24, 'papua-new-guinea': 26, 'tuvalu': 26, 'dominica': 27, 'saint-lucia': 28, 'st-kitts-nevis': 28, 'st-vincent-grenadines': 28, 'antigua-barbuda': 29, 'belize': 29, 'grenada': 29, 'jamaica': 36, 'bolivia': 38, 'guyana': 42}

"""


def plot_war(countires_have_past_war):
    
    
    labels = [ 'Fought atleast one war','Nation that fought no war ']
    sizes = [ countires_have_past_war[1.0],countires_have_past_war[0.0]]
    
    
    colors = [ 'yellowgreen','lightskyblue', 'lightcoral', 'gold']
    patches, texts ,autotexts = plt.pie(sizes, colors=colors, shadow=True, startangle=90,autopct='%1.2f%%',explode=(0,0.1))
    plt.legend(patches, labels, loc="lower right")
    plt.axis('equal')
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.6, top=0.8)
    plt.tight_layout(pad=2)
    plt.title("Distribution of Nations for war fought since 1950s" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
    
    plt.savefig('pie_war.pdf',figsize=(20,20))
    #plt.show()

    
def plot_border(border):
    
    labels = ['closed border','Movement using Visa', 'Free movement for certain groups', 'Free movement']
    sizes = [ border[-1],border[0],border[2],border[1]]
    
    colors = [ 'yellowgreen','lightskyblue', 'lightcoral', 'gold']
    patches, texts ,autotexts = plt.pie(sizes, colors=colors, shadow=True, pctdistance =0.2,startangle=270,autopct='%1.2f%%',explode=(0.2,0,0,0))
    plt.legend(patches, labels, loc="upper right")
    plt.axis('equal')
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.6, top=0.8)
   # plt.tight_layout(pad=2)
    plt.title("Distribution of different type of borders across pairs of nation" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
    
    plt.savefig('pie_border.pdf',figsize=(20,20))

def plot_treaties(counties_having_treaties):
    
    labels = ['Have Signed atleast one peace treaty','No peace treaty signed']
    sizes = [ counties_having_treaties[1],counties_having_treaties[0]]
    
    colors = ['lightskyblue' ,'gold','lightskyblue', 'lightcoral', 'gold']
    patches, texts ,autotexts = plt.pie(sizes, colors=colors, shadow=True, startangle=45,autopct='%1.2f%%',explode=(0.1,0))
    plt.legend(patches, labels, loc="lower right")
    plt.axis('equal')
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.6, top=0.8)
    plt.tight_layout(pad=2)
    plt.title("Distribution of Peace Treaties signed-unsigned nation" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
    
    plt.savefig('pie_treaties.pdf',figsize=(20,20))

    
def plot_cases(dc_cases):
    
    x1 = len(dc_cases)
    
    x2= 197- x1
    
    labels = ['Have International Cases','Dont have international cases']
    sizes = [ x1,x2]
    
    colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'lightcoral', 'gold']
    patches, texts ,autotexts = plt.pie(sizes, colors=colors, shadow=True, startangle=270,autopct='%1.2f%%',explode=(0.1,0))
    plt.legend(patches, labels, loc="lower left")
    plt.axis('equal')
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.6, top=0.8)
    plt.tight_layout(pad=2)
    plt.title("Distribution of International Court Cases" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
    
    plt.savefig('pie_cases.pdf',figsize=(20,20))

def plot_rel_conflict(count_of_religion_conflict):
    
    
    labels = ['No conflicting group with other nation','1 conflicting group','2 conflicting group','3 conflicting group','4 conflicting group']
    sizes = [ count_of_religion_conflict[0],count_of_religion_conflict[1],count_of_religion_conflict[2],count_of_religion_conflict[3],count_of_religion_conflict[4]]
    
    colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'red', 'gold']
    patches, texts ,autotexts = plt.pie(sizes, colors=colors, shadow=True, startangle=270,autopct='%1.2f%%',explode=(0.,0.,0.,0.0,0))
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.6, top=0.8)
    plt.tight_layout(pad=2)
    plt.title("Distribution of Count of conflicting group among nations" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
    
    plt.savefig('pie_conflict.pdf',figsize=(20,20))

def plot_border_bar(border):
    
    height = [ border[-1], border[2], border[1]]
    bars = ( 'Closed Border', 'Open Border', 'Uncategorized Understanding')
    y_pos = np.arange(len(bars))
    barrs=plt.bar(y_pos, height)
    colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'red', 'gold']
    color_dict={}
    j=0
    for i in range(0,len(barrs)):
        
        barrs[i].set_color(colors[j])
        color_dict[bars[i]] = colors[i]
        j=(j+1)% (len(colors))
           
    plt.xticks(y_pos, bars,rotation=15)
    for bar in barrs:
        yval = bar.get_height()
        plt.text(bar.get_x(),yval+1,yval)
    
    labels = bars
    color_dict['All other Visa Required'] ="orange"
    handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in labels]
    plt.legend(handles, labels,bbox_to_anchor=(.90, 1.0), loc='upper left',prop={'size':7})
    plt.tight_layout(pad=2)
    plt.xlabel('Type of border');
    plt.ylabel('Count of nation pairs');

    plt.title("Distribution of various types of border among nations (excluding VISA)" , fontdict={'fontsize': 10,
     'fontweight' :1,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
   
    plt.savefig('bar_border.pdf',figsize=(50,50))
    #plt.show()

def plot_rel_conflict_bar(count_of_religion_conflict):
    
    height = [count_of_religion_conflict[0], count_of_religion_conflict[1], count_of_religion_conflict[2], count_of_religion_conflict[3], count_of_religion_conflict[4]]
    bars = ('0', '1', '2','3' ,'4')
    y_pos = np.arange(len(bars))
    barrs=plt.bar(y_pos, height)
    colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'red', 'gold']
    color_dict={}
    j=0
    for i in range(0,len(barrs)):
        
        barrs[i].set_color(colors[j])
        color_dict[bars[i]] = colors[i]
        j=(j+1)% (len(colors))
           
    plt.xticks(y_pos, bars,rotation=0)
    for bar in barrs:
        yval = bar.get_height()
        plt.text(bar.get_x(),yval+1,yval)
    
    labels = bars
    handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in labels]
    plt.legend(handles, labels,title="Count",bbox_to_anchor=(1.05, 1.0), loc='upper left',prop={'size':7})
    plt.tight_layout(pad=2)
    plt.xlabel('Count of religious conflicting group within nation');
    plt.ylabel('No of nations having the count');

    plt.title("Distribution of conflict groups count with other nations" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
   
    plt.savefig('bar_rel_conflict.pdf',figsize=(25,25))
    #plt.show()

def plot_export_top(top10_export):
    
    bars=[i+1 for i in range(0,len(top10_export.keys()))]#list(top10_export.keys())
    height = list(top10_export.values())
    for each in range(0,len(height)):
        height[each]= round(height[each]/10**12,2)
    
    #height = [count_of_religion_conflict[0], count_of_religion_conflict[1], count_of_religion_conflict[2], count_of_religion_conflict[3], count_of_religion_conflict[4]]
   # bars = ('0', '1', '2','3' ,'4')
    y_pos = np.arange(len(bars))
    barrs=plt.bar(y_pos, height)
    colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'red', 'gold','darkorange','royalblue','lime','blueviolet','teal']
    color_dict={}
    j=0
    for i in range(0,len(barrs)):
        
        barrs[i].set_color(colors[j])
        color_dict[bars[i]] = colors[i]
        j=(j+1)% (len(colors))
           
    plt.xticks(y_pos, bars,rotation=00)
    for bar in barrs:
        yval = bar.get_height()
        plt.text(bar.get_x(),yval+0.01,yval)
    
    labels = list(top10_export.keys())
    handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in bars]
    plt.legend(handles, labels,title="Nations")
    plt.legend(handles, labels,bbox_to_anchor=(1.05, 1.0), loc='upper left',prop={'size':7})
    plt.tight_layout(pad=2)
    plt.xlabel('Rank');
    plt.ylabel('Amount in USD dollars');


    plt.title("Top 10 most Exporting nations (in Trillions)" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
   
    plt.savefig('bar_top_export.pdf',figsize=(50,50))
    #plt.show()

def plot_import_top(top10_import):
    
    bars=[i+1 for i in range(0,len(top10_import.keys()))]#list(top10_export.keys())
    height = list(top10_import.values())
    for each in range(0,len(height)):
        height[each]= round(height[each]/10**12,2)
    
    #height = [count_of_religion_conflict[0], count_of_religion_conflict[1], count_of_religion_conflict[2], count_of_religion_conflict[3], count_of_religion_conflict[4]]
   # bars = ('0', '1', '2','3' ,'4')
    y_pos = np.arange(len(bars))
    barrs=plt.bar(y_pos, height)
    colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'red', 'gold','darkorange','royalblue','lime','blueviolet','teal']
    color_dict={}
    j=0
    for i in range(0,len(barrs)):
        
        barrs[i].set_color(colors[j])
        color_dict[bars[i]] = colors[i]
        j=(j+1)% (len(colors))
           
    plt.xticks(y_pos, bars,rotation=00)
    for bar in barrs:
        yval = bar.get_height()
        plt.text(bar.get_x(),yval+0.1,yval)
    
    labels = list(top10_import.keys())
    handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in bars]
    plt.legend(handles, labels,title="Nations")
    plt.legend(handles, labels,bbox_to_anchor=(1.05, 1.0), loc='upper left',prop={'size':7})
    plt.tight_layout(pad=2)
    plt.xlabel('Rank');
    plt.ylabel('Amount in USD dollars');

    plt.title("Top 10 most Importing nations (in Million)" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
   
    plt.savefig('bar_top_import.pdf',figsize=(50,50))
    #plt.show()
    

def plot_import_low(low10_import):
    
    bars=[i+1 for i in range(0,len(low10_import.keys()))]#list(top10_export.keys())
    height = list(low10_import.values())
    for each in range(0,len(height)):
        height[each]= round(height[each]/10**5,1)
    
    #height = [count_of_religion_conflict[0], count_of_religion_conflict[1], count_of_religion_conflict[2], count_of_religion_conflict[3], count_of_religion_conflict[4]]
   # bars = ('0', '1', '2','3' ,'4')
    y_pos = np.arange(len(bars))
    barrs=plt.bar(y_pos, height)
    colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'red', 'gold','darkorange','royalblue','lime','blueviolet','teal']
    color_dict={}
    j=0
    for i in range(0,len(barrs)):
        
        barrs[i].set_color(colors[j])
        color_dict[bars[i]] = colors[i]
        j=(j+1)% (len(colors))
           
    plt.xticks(y_pos, bars,rotation=00)
    for bar in barrs:
        yval = bar.get_height()
        plt.text(bar.get_x(),yval+20,yval,fontsize=5.5)
    
    labels = list(low10_import.keys())
    handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in bars]
    plt.legend(handles, labels,title="Nations")
    plt.legend(handles, labels,bbox_to_anchor=(1.05, 1.0), loc='upper left',prop={'size':7})
    plt.tight_layout(pad=2)
    plt.xlabel('Rank');
    plt.ylabel('Amount in USD dollars');

    plt.title("Lowest 10 Importing nations (in Lakhs)" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
   
    plt.savefig('bar_low_import.pdf',figsize=(50,50))
    #plt.show()


def plot_export_low(low10_export):
    
    bars=[i+1 for i in range(0,len(low10_export.keys()))]#list(top10_export.keys())
    height = list(low10_export.values())
    for each in range(0,len(height)):
        height[each]= round(height[each]/10**6,2)
    
    #height = [count_of_religion_conflict[0], count_of_religion_conflict[1], count_of_religion_conflict[2], count_of_religion_conflict[3], count_of_religion_conflict[4]]
   # bars = ('0', '1', '2','3' ,'4')
    y_pos = np.arange(len(bars))
    barrs=plt.bar(y_pos, height)
    colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'red', 'gold','darkorange','royalblue','lime','blueviolet','teal']
    color_dict={}
    j=0
    for i in range(0,len(barrs)):
        
        barrs[i].set_color(colors[j])
        color_dict[bars[i]] = colors[i]
        j=(j+1)% (len(colors))
           
    plt.xticks(y_pos, bars,rotation=00)
    for bar in barrs:
        yval = bar.get_height()
        plt.text(bar.get_x(),yval+1.2,yval,fontsize=7)
    
    labels = list(low10_export.keys())
    handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in bars]
    plt.legend(handles, labels,title="Nations")
    plt.legend(handles, labels,bbox_to_anchor=(1.05, 1.0), loc='upper left',prop={'size':7})
    plt.tight_layout(pad=2)
    plt.xlabel('Rank');
    plt.ylabel('Amount in USD dollars');



    plt.title("Lowest 10 Exporting nations (in Trillions)" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
   
    plt.savefig('bar_low_export.pdf',figsize=(50,50))
    #plt.show()

def plot_diplo_low(low10_diplomatic):
    
    bars=[i+1 for i in range(0,len(low10_diplomatic.keys()))]#list(top10_export.keys())
    height = list(low10_diplomatic.values())
    
    #height = [count_of_religion_conflict[0], count_of_religion_conflict[1], count_of_religion_conflict[2], count_of_religion_conflict[3], count_of_religion_conflict[4]]
   # bars = ('0', '1', '2','3' ,'4')
    y_pos = np.arange(len(bars))
    barrs=plt.bar(y_pos, height)
    colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'red', 'gold','darkorange','royalblue','lime','blueviolet','teal']
    color_dict={}
    j=0
    for i in range(0,len(barrs)):
        
        barrs[i].set_color(colors[j])
        color_dict[bars[i]] = colors[i]
        j=(j+1)% (len(colors))
           
    plt.xticks(y_pos, bars,rotation=00)
    for bar in barrs:
        yval = bar.get_height()
        plt.text(bar.get_x(),yval+0.3,yval,fontsize=7)
    
    labels = list(low10_diplomatic.keys())
    handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in bars]
    plt.legend(handles, labels,title="Nations")
    plt.legend(handles, labels,bbox_to_anchor=(1.05, 1.0), loc='upper left',prop={'size':7})
    plt.tight_layout(pad=2)
    plt.xlabel('Rank');
    plt.ylabel('Count of diplomatic relations');


    plt.title("10 nations having lowest diplomatic relations" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
   
    plt.savefig('bar_low_diplo.pdf',figsize=(50,50))
    #plt.show()


def plot_diplo_top(top10_diplomatic):
    
    bars=[i+1 for i in range(0,len(top10_diplomatic.keys()))]#list(top10_export.keys())
    height = list(top10_diplomatic.values())
    
    #height = [count_of_religion_conflict[0], count_of_religion_conflict[1], count_of_religion_conflict[2], count_of_religion_conflict[3], count_of_religion_conflict[4]]
   # bars = ('0', '1', '2','3' ,'4')
    y_pos = np.arange(len(bars))
    barrs=plt.bar(y_pos, height)
    colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'red', 'gold','darkorange','royalblue','lime','blueviolet','teal']
    color_dict={}
    j=0
    for i in range(0,len(barrs)):
        
        barrs[i].set_color(colors[j])
        color_dict[bars[i]] = colors[i]
        j=(j+1)% (len(colors))
           
    plt.xticks(y_pos, bars,rotation=00)
    for bar in barrs:
        yval = bar.get_height()
        plt.text(bar.get_x(),yval+0.3,yval,fontsize=7)
    
    labels = list(top10_diplomatic.keys())
    handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in bars]
    plt.legend(handles, labels,title="Nations")
    plt.legend(handles, labels,bbox_to_anchor=(1.05, 1.0), loc='upper left',prop={'size':7})
    plt.tight_layout(pad=2)
    plt.xlabel('Rank');
    plt.ylabel('Count of diplomatic relations');


    plt.title("Nations with highest diplomatic relations" , fontdict={'fontsize': 12,
     'fontweight' :3,
     'verticalalignment': 'baseline',
     'horizontalalignment': 'center'} )
   
    plt.savefig('bar_top_diplo.pdf',figsize=(50,50))
    #plt.show()
    
countires_have_past_war = {0.0: 35074, 1.0: 3538}

border = {0: 37444, -1: 20, 2: 998, 1: 150}
dc_cases={'thailand', 'india', 'bulgaria', 'qatar', 'niger', 'saudi-arabia', 'colombia', 'macedonia', 'netherlands', 'senegal', 'ecuador', 'canada', 'ethiopia', 'belgium', 'greece', 'liechtenstein', 'turkey', 'paraguay', 'guatemala', 'serbia', 'cambodia', 'malta', 'rwanda', 'guinea-bissau', 'congo', 'italy', 'indonesia', 'mali', 'bolivia', 'united-states', 'finland', 'slovakia', 'australia', 'sweden', 'israel', 'bahrain', 'burundi', 'namibia', 'romania', 'albania', 'argentina', 'france', 'peru', 'burkina-faso', 'uruguay', 'brazil', 'dominica', 'spain', 'benin', 'united-arab-emirates', 'switzerland', 'bosnia-herzegovina', 'cameroon', 'iran', 'germany', 'chad', 'marshall-islands', 'mexico', 'ukraine', 'croatia', 'denmark', 'malaysia', 'chile', 'tunisia', 'liberia', 'south-africa', 'russia', 'nauru', 'new-zealand', 'botswana', 'singapore', 'iceland', 'pakistan', 'nigeria', 'el-salvador', 'nicaragua', 'libya', 'east-timor', 'georgia', 'ireland', 'portugal', 'lebanon', 'egypt', 'honduras', 'hungary', 'norway', 'djibouti', 'united-kingdom', 'montenegro', 'japan'}


dc_cases_len=len(dc_cases) #have 
counties_having_treaties ={0: 38064, 1: 548}
count_of_religion_conflict = {0: 8671, 1: 21421, 2: 7965, 3: 541, 4: 14}
top10_export={'china': 2125260446530.0, 'united-states': 1565773285610.0, 'germany': 1408443429090.0, 'taiwan': 844141600000.0, 'san-marino': 716480713530.0, 'eritrea': 662943725710.0, 'japan': 626167092990.0, 'netherlands': 542806941410.0, 'france': 538593990710.0, 'italy': 507529632700.0}
top10_import={'south-sudan': 5674932514050.0, 'united-states': 2494572258780.0, 'china': 1795200005840.0, 'germany': 1137769203420.0, 'bahamas': 781403174754.0, 'micronesia': 752184809572.0, 'somalia': 749493986995.0, 'maldives': 742479586303.0, 'marshall-islands': 741361083812.0, 'guinea-bissau': 728571270454.0}
low10_export={ 'sao-tome-principe': 3793080.0, 'tonga': 12428869.0, 'samoa': 26676360.0, 'gambia': 27726822.0, 'grenada': 31170450.0, 'east-timor': 32121632.0, 'st-kitts-nevis': 32210800.0, 'st-vincent-grenadines': 38905441.0, 'antigua-barbuda': 46170740.0, 'comoros': 52080243.0}
low10_import={ 'taiwan': 599788.0, 'sao-tome-principe': 149790634.0, 'comoros': 208286528.0, 'tonga': 214140080.0, 'vanuatu': 271604931.0, 'grenada': 280322761.0, 'st-kitts-nevis': 303129269.0, 'st-vincent-grenadines': 332982055.0, 'samoa': 368833048.0, 'gambia': 493658044.0}
top10_diplomatic = {'china': 193, 'indonesia': 189, 'united-states': 189, 'russia': 188, 'spain': 187, 'turkey': 187, 'germany': 186, 'laos': 186, 'brazil': 185, 'togo': 185}
low10_diplomatic = {'kiribati': 18, 'samoa': 18, 'vanuatu': 19, 'marshall-islands': 20, 'nauru': 20, 'suriname': 22, 'fiji': 24, 'tonga': 24, 'papua-new-guinea': 26, 'tuvalu': 26}
#plot_export_top(top10_export)
plot_import_top(top10_import)
#plot_export_low(low10_export)
#plot_import_low(low10_import)
#plot_diplo_low(low10_diplomatic)
#plot_diplo_top(top10_diplomatic)

#plot_rel_conflict_bar(count_of_religion_conflict)
#plot_rel_conflict(count_of_religion_conflict)  
#plot_treaties(counties_having_treaties)
#plot_cases(dc_cases)
#plot_war(countires_have_past_war)
#plot_border(border)  CHnage to bar 
#plot_border_bar(border)
"""
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))
barrs=plt.bar(y_pos, height)
colors = ['lightcoral' ,'yellowgreen','lightskyblue', 'red', 'gold']
color_dict={}
j=0
for i in range(0,len(barrs)):
    
    barrs[i].set_color(colors[j])
    color_dict[bars[i]] = colors[i]
    j=(j+1)% (len(colors))
       
plt.xticks(y_pos, bars)
for bar in barrs:
    yval = bar.get_height()
    plt.text(bar.get_x(),yval+1,yval)

labels = bars
handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in labels]
plt.legend(handles, labels)
plt.savefig('bar.pdf',figsize=(20,20))
#plt.show()
"""
