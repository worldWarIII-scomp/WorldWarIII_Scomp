def single_append_pos(G,country,first_set,second_set):
    discovered_nodes=[]
    res=[]
    neigh=list(G.neighbors(country))
    pos_max=0
    pos=""
    neg=""
    neg_max=0
    for i in range(len(neigh)):
        discovered_nodes.append(neigh[i])
        if G[country][neigh[i]]['sign']=='+':
            if neigh[i] not in first_set and neigh[i] not in second_set:
                if G[country][neigh[i]]['weight']>pos_max:
                    pos_max=G[country][neigh[i]]['weight']
                    pos=neigh[i]
        elif G[country][neigh[i]]['sign']=='-':
            if neigh[i] not in second_set and neigh[i] not in first_set:
                if G[country][neigh[i]]['weight']<neg_max:
                    neg_max=G[country][neigh[i]]['weight']
                    neg=neigh[i]
    if(pos_max>0):
        first_set.append(pos)
        #print("pos selected=",pos)
    if(neg_max<0):
        second_set.append(neg)
        #print("neg selected=",neg)
    res.append(pos)
    res.append(neg)
    res.append(first_set)
    res.append(second_set)
    res.append(discovered_nodes)
    return(res)

def single_append_neg(G,country,first_set,second_set):
    discovered_nodes=[]
    res=[]
    neigh=list(G.neighbors(country))
    pos_max=0
    pos=""
    neg=""
    neg_max=0
    for i in range(len(neigh)):
        discovered_nodes.append(neigh[i])
        
        if G[country][neigh[i]]['sign']=='+':
            if neigh[i] not in second_set and neigh[i] not in first_set:
                if G[country][neigh[i]]['weight']>pos_max:
                    pos_max=G[country][neigh[i]]['weight']
                    pos=neigh[i]
        elif G[country][neigh[i]]['sign']=='-':
            if neigh[i] not in first_set and neigh[i] not in second_set:
                if G[country][neigh[i]]['weight']<neg_max:
                    neg_max=G[country][neigh[i]]['weight']
                    neg=neigh[i]
    if(pos_max>0):
        second_set.append(pos)
        #print("pos selected in neg=",pos)
    if(neg_max<0):
        first_set.append(neg)
        #print("neg selected in neg=",neg)
    res.append(neg)
    res.append(pos)
    res.append(first_set)
    res.append(second_set)
    res.append(discovered_nodes)
    return(res)

def see_cohilitions(G,country):
    first_set=[]
    second_set=[]
    processed=[]
    to_be_processed_positive=[]
    to_be_processed_negitive=[]
    discovered_nodes=[]
    #nodes=list(G.nodes())
    #country ='Iran'
    first_set.append(country)
    to_be_processed_positive.append(country)
    pos,neg,first_set,second_set,discovered_nodes1=single_append_pos(G,country,first_set,second_set)
    discovered_nodes=list(set(discovered_nodes) | set(discovered_nodes1)) #union
    if(pos):
        to_be_processed_positive.append(pos)
    if(neg):
        to_be_processed_negitive.append(neg)
    processed.append(country)
    #print("processed!!",country)
    to_be_processed_positive.remove(country)
    round_no=0
    while(len(processed)<197):
        round_no+=1
        if(len(to_be_processed_negitive)>0):
            country=to_be_processed_negitive[0]
            pos,neg,first_set,second_set,discovered_nodes1=single_append_neg(G,country,first_set,second_set)
            discovered_nodes=list(set(discovered_nodes) | set(discovered_nodes1)) #union
            if(pos):
                to_be_processed_positive.append(pos)
            if(neg):
                to_be_processed_negitive.append(neg)
            processed.append(country)
            #print("processed!!",country)
            to_be_processed_negitive.remove(country)
        if(len(to_be_processed_positive)>0):
            country=to_be_processed_positive[0]
            pos,neg,first_set,second_set,discovered_nodes1=single_append_pos(G,country,first_set,second_set)
            discovered_nodes=list(set(discovered_nodes) | set(discovered_nodes1)) #union
            if(pos):
                to_be_processed_positive.append(pos)
            if(neg):
                to_be_processed_negitive.append(neg)
            processed.append(country)
            to_be_processed_positive.remove(country)
            #print("processed!!",country)
        
        #print(round_no,len(first_set),len(second_set))
    
    return first_set,second_set

#import pandas as pd
#import numpy as np
#df = pd.read_csv(r'sign_score_dataset_test2.csv')
#print("################IMPORT DONE##########################")
#G=nx.from_pandas_edgelist(df, 'Source', 'Target', edge_attr=True)
G=nx.read_gml('graph_after_stablizing1.gml')
for k in list(G.nodes()):
    L1,L2=see_cohilitions(G,k)
    plus=0
    minus=0
    for i,j in enemy:
        if (i in L1 and j in L2) or (j in L1 and i in L2):
            plus+=1
        else:
            minus+=1
    for i,j in friend:
        if (i in L1 and j in L1) or (j in L2 and i in L2):
            plus+=1
        else:
            minus+=1
    print(k,plus)
    if(plus>26):
        print(L1)
        print(L2)

#print(first_set)
#print(second_set)