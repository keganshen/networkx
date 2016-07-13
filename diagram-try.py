#coding=utf-8
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv

G = nx.MultiDiGraph()
DG = nx.MultiDiGraph()

def howdeep(selected_nodes,h):
    if h > 0:
        h -= 1
        for each_item in nx.all_neighbors(G,selected_nodes):

            DG.add_edge(each_item,selected_nodes)
            howdeep(each_item,h)
    else:
        pass

reader = csv.reader(file('test.csv','rb'))

for row in reader:
    if reader.line_num == 1 :
        continue
    G.add_edge(row[0],row[1])

weight_g = sorted(G.degree().values())

for each_node in sorted(G.nodes()):
    total = G.out_degree(each_node)+G.in_degree(each_node)
    print '%s: \n 通话总数：%d \n 拨出数: %d' %(each_node,total,G.out_degree(each_node))
    if nx.degree(G)[each_node] >= weight_g[-1]:
        howdeep(each_node,1)



'''
pos = nx.spring_layout(G)
nx.draw_networkx(DG,pos,node_size=1000,font_size=8)
nx.freeze(G)
plt.show()
'''
