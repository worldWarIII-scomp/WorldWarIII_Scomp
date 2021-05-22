per##############################unstable to stable#######################
import networkx as nx
import random
import itertools
import matplotlib.pyplot as plt

#Returns the list of triangles in graph G            
def get_tri_list(G):
    #Your Code goes here
    nodes=G.nodes()
    tris_list=[list(x) for x in itertools.combinations(nodes,3)]
    
    return tris_list

#Returns all signs of triangles

def get_signs_of_tris(tris_list, G):
    all_signs=[]
    for i in range(len(tris_list)):
        temp=[]
        temp.append(G[tris_list[i][0]][tris_list[i][1]]['weight'])
        temp.append(G[tris_list[i][1]][tris_list[i][2]]['weight'])
        temp.append(G[tris_list[i][2]][tris_list[i][0]]['weight'])
        all_signs.append(temp)
    
    return all_signs

#Returns number of unstable triangles
def count_unstable(all_signs):
    # Your Code goes here
    num_unstable=0
    for i,j,k in all_signs:
        #print(i,j,k)
        if i<0 and j<0 and k<0:
            num_unstable+=1
        elif (i>=0 and j>=0 and k<0) or (i>=0 and j<0 and k>=0) or (i<0 and j>=0 and k>=0):
            num_unstable+=1
    
    return num_unstable

def move_a_tri_to_stable(G, tris_list, all_signs):
    found_unstable=False
    case=0
    while(found_unstable==False):
        index=random.randint(0,len(tris_list)-1)
        i,j,k=all_signs[index]
        if i<0 and j<0 and k<0: #(all_signs[i].count('+')==2 or all_signs[i].count('+')==0):
            found_unstable=True
            case=1
        elif (i>=0 and j>=0 and k<0) or (i>=0 and j<0 and k>=0) or (i<0 and j>=0 and k>=0):
            found_unstable=True
            case=2
        else:
            continue
    i=G[tris_list[index][0]][tris_list[index][1]]['weight']
    j=G[tris_list[index][1]][tris_list[index][2]]['weight']
    k=G[tris_list[index][2]][tris_list[index][0]]['weight']
    to_change=0
    if(abs(j)>abs(i)):
        to_change=1
        if(abs(k)>abs(j)):
            to_change=2
    elif(abs(k)>abs(i)):
        to_change=2
         
    if case==2:   
        if G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['sign']=='+':
            G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['sign']='-'
            i=G[tris_list[index][(to_change+1)%3]][tris_list[index][(to_change+2)%3]]['weight']
            j=G[tris_list[index][(((to_change+1)%3)+1)%3]][tris_list[index][(((to_change+2)%3)+1)%3]]['weight']
            if(i>j):
                weight=i+abs(j)-G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['weight']
                weight=-weight
                G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['weight']=weight
                
        elif G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['sign']=='-':
            G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['sign']='+'
            weight=abs(G[tris_list[index][(to_change+1)%3]][tris_list[index][(to_change+2)%3]]['weight']) + abs(G[tris_list[index][(((to_change+1)%3)+1)%3]][tris_list[index][(((to_change+2)%3)+1)%3]]['weight'])
            G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['weight']=weight
    
    elif case==1:
        G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['sign']='+'
        weight=abs(G[tris_list[index][(to_change+1)%3]][tris_list[index][(to_change+2)%3]]['weight']) + abs(G[tris_list[index][(((to_change+1)%3)+1)%3]][tris_list[index][(((to_change+2)%3)+1)%3]]['weight'])
        G[tris_list[index][to_change]][tris_list[index][(to_change+1)%3]]['weight']=weight
        
    return G

print('Reading graph!!')
G=nx.read_gml('initial_graph.gml')   
print('Reading graph done')                 
# Get list of triangles
tris_list=get_tri_list(G)

#Get the sign details of all the triangles
all_signs = get_signs_of_tris(tris_list, G)

#Get the number of unstable triangles
num_unstable = count_unstable(all_signs)
print('Number of stable traingle out of ', len(tris_list), ' are ', len(tris_list)-num_unstable)
print('Number of unstable traingle out of ', len(tris_list), ' are ', num_unstable)


num_unstable_prev=num_unstable
stopping_flag=0
round_no=0
while(num_unstable>10000 and stopping_flag<20):
    num_unstable_prev=num_unstable
    G=move_a_tri_to_stable(G, tris_list, all_signs)
    all_signs = get_signs_of_tris(tris_list, G)
    num_unstable = count_unstable(all_signs)
    round_no+=1
    print(round_no,'Number of unstable traingle out of ', len(tris_list), ' are ', num_unstable)
    if(num_unstable_prev==num_unstable):
        stopping_flag+=1
    else:
        stopping_flag=0
    nx.write_gml(G, "graph_after_stablizing.gml")
    
print("################EXPORT DONE##########################")