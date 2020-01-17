 
"""
RSIC Project - Analysis of Protein Networks with NetworkX

Author: Balan
"""

import networkx as nx

i = 0
x = 0
G = nx.Graph()
C = nx.Graph()
#deg_cen_list = list()
#deg_cen_invert = dict()
bet_cen_list = list()
bet_cen_invert = dict()

# Change Path for E. Coli file on a different device
"""
C:/Users/TLC/Desktop/RSIC Project - Dr. Karthik Raman/ecoli.txt             --   TLC computer 6 from recording room
E:ecoli.txt   --  Balan's Laptop
C:/Users/TLC/Desktop/RSIC/ecoli.txt    -- TLC computer 4 from the recording room
"""

# Making the graph
with open('E:ecoli.txt', 'r') as f:
    for line in f.readlines():
        words=line.split()
        if ((int(words[2]))>=700):
            G.add_edge(words[0], words[1], weight = int(words[2]))

# Extracting the largest subgraph
for comp in nx.connected_component_subgraphs(G):
    if comp.number_of_nodes()>i:
        C = comp
        i = comp.number_of_nodes()

# Getting the centrality measures
#deg_cen = nx.degree_centrality(C)
bet_cen = nx.betweenness_centrality(C)

# For inverting the dictionaries
"""
for keys, values in deg_cen.items():
    deg_cen_invert[values] = deg_cen.get(values, [])  
for keys, values in deg_cen.items():
    deg_cen_invert[values].append(keys)

""" 
for keys, values in bet_cen.items():
    bet_cen_invert[values] = bet_cen.get(values, [])
for keys, values in bet_cen.items():    
    bet_cen_invert[values].append(keys)

 
# Extracting highest 10 values of degree centrality
#deg_cen_list = list(deg_cen_invert.keys())
#deg_cen_list.sort()
bet_cen_list = list(bet_cen_invert.keys())
bet_cen_list.sort()

# Receiving average shortest path length
x = nx.average_shortest_path_length(C)
print("Initial average shortest path length", str(x))


# Average shortest path based on betweenness centrality
i = 0
for i in range(1, 11):
    for j in range(len(bet_cen_invert[bet_cen_list[-i]])): 

        #Remove Node
        C.remove_node(bet_cen_invert[bet_cen_list[-i]][j])
        print('Node Removed : ', bet_cen_invert[bet_cen_list[-i]][j])
    
        # Re-Checking Shortest Path length
        try:
            x = nx.average_shortest_path_length(C)
            print('Avg Path Length after removal : ', x)                  
              
            print('\n')
        except nx.NetworkXError:
            print('ERROR')
            pass
    
"""


# Average shortest path based on degree centrality
i = 0
for i in range(1, 11):
    for j in range(len(deg_cen_invert[deg_cen_list[-i]])):
        
        #Remove Node
        C.remove_node(deg_cen_invert[deg_cen_list[-i]][j])
        print('Node Removed : ', deg_cen_invert[deg_cen_list[-i]][j])
        
        # Re-Checking Shortest Path length
        try:
            x = nx.average_shortest_path_length(C)
            print('Avg Path Length after removal : ', x)                  
            print('\n')
        except nx.NetworkXError:
            print('ERROR')
            pass

"""
"""        
Keys for TLC Computer        

!  @  #  $  %  ^  &  *  ()  _  +  {}  | 
"  <>  ?  /  \  .  ,  ;  '  []  =  -  :
"""
