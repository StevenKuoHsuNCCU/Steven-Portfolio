import heapq
import pyvis
import random
import math
import fibheap
from matplotlib import pyplot as plt
from pyvis.network import Network
from IPython.core.display import display, HTML


"""************************************************** Create Graph (Default)****************************************************************************************"""

# Create graph

graph = dict()
default_edge_value = 1

# Create node

for i in range(0,1000):
    graph[i] = dict()

# Create edge

for i in range(0,1000):
    if i == 0 :
        graph[i][i+1] = default_edge_value
        graph[i][999] = default_edge_value
    elif i == 999 :
        graph[i][0] = default_edge_value
        graph[i][i-1] = default_edge_value
    else:
        graph[i][i+1] = default_edge_value
        graph[i][i-1] = default_edge_value
    




"""************************************************** Dijkstra Algorithm ****************************************************************************************"""


    

def fibque(fib):
    sorted_queue = list()
    for i in range(fib.num_nodes):
        sorted_queue.append(fibheap.fheappop(fib))
    for i in sorted_queue:
        fibheap.fheappush(fib, i)
    return sorted_queue
    

def dijkstra_fib(graph,node):
    distances={node:float('inf') for node in graph}
    distances[node]=0
    came_from={node:None for node in graph}
    queue = fibheap.makefheap()
    fibheap.fheappush(queue,(0,node))
    queue_list = fibque(queue)
    
    
    while queue_list:
        current_distance,current_node=fibheap.fheappop(queue)
        queue_list.remove((current_distance,current_node))
        # relaxation
        for next_node,weight in graph[current_node].items():
            distance_temp=current_distance+weight
            if distance_temp<distances[next_node]:
                distances[next_node]=distance_temp
                came_from[next_node]=current_node
                fibheap.fheappush(queue,(distance_temp,next_node))
                queue_list.append((distance_temp,next_node))
                
                
    return distances,#came_from


# Compute average shortest path

def compute_shortest_path_fib(your_graph, startpoint):
    shortest_path = 0
    dijk = dijkstra_fib(your_graph,startpoint)
    for i in list(dijk[0]):
        shortest_path = shortest_path + dijk[0][i]
    return shortest_path

def compute_average_shortest_path_fib(your_graph):
    total_shortest_path = list()
    for i in list(your_graph):
        total_shortest_path.append(compute_shortest_path_fib(your_graph,i) )
    average = sum(total_shortest_path)/len(total_shortest_path)
    average = round(average, 3)
    return average



def compute_shortest_path_Zsamples_fib(your_graph, z):
    average_shortest_path = list()
    for i in range(0,z):
        dijk = dijkstra_fib(your_graph,random.choice(list(your_graph)))
        average_shortest_path.append(dijk[0][random.choice(list(dijk[0]))])
    average = sum(average_shortest_path)/len(average_shortest_path)
    average = round(average, 3)
    return average
    
    
print(compute_shortest_path_Zsamples_fib(graph,500))


"""************************************************** Graph Visualization (Default) ****************************************************************************************"""
# Create network
'''

net = Network(bgcolor="#222222",
    font_color="white",
    height="750px",
    width="100%",
    select_menu=True,
    filter_menu=True)

# Create node

net.add_nodes(list(graph))

# Create edge

for i in list(graph):
    for j in list(graph[i]):
        net.add_edges([(i, j, graph[i][j])])
        

net.show_buttons(filter_=['physics'])
net.show('default.html')

'''
"""************************************************** Experiment ****************************************************************************************"""

# Graph

graph_test_1 = graph


## Add the random x edge

shortest_path_list_x = []
shortest_path_list_x.append(compute_shortest_path_Zsamples_fib(graph_test_1,50))


for i in range(0,100):
    ### Count
    print(i)    
    ### Selecting the edge
    edge_start = random.randint(0,999)
    edge_end = random.randint(0,999)
    while edge_end in list(graph_test_1[edge_start]):
        edge_end = random.randint(0,999)
        
    ### Building the edge
    add_edge_value_y = 0.5
    
    graph_test_1[edge_start][edge_end] = add_edge_value_y
    graph_test_1[edge_end][edge_start] = add_edge_value_y
    
    ### Shortest Path
    sample_z = 50
    
    shortest_path_list_x.append(compute_shortest_path_Zsamples_fib(graph_test_1,sample_z))
    
    
x = range(0,101)
y = shortest_path_list_x

plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.plot(x,y)
plt.show()




# Visualization


'''
# Create network

net_test_1 = Network(bgcolor="#222222",
    font_color="white",
    height="750px",
    width="100%",
    select_menu=True,
    filter_menu=True)

# Create node

net_test_1.add_nodes(list(graph_test_1))

# Create edge

for i in list(graph_test_1):
    for j in list(graph_test_1[i]):
        net_test_1.add_edges([(i, j, graph_test_1[i][j])])
        


net_test_1.show_buttons(filter_=['physics'])
net_test_1.show('demo.html')

'''
        

    
















    
