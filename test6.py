#coding=utf-8
import csv
import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()

reader=csv.reader(file('sing.csv','rb'))
for row in reader:
        if reader.line_num ==1:
                continue
        for i in range(len(row)):
                print row[i]
        G.add_edge(row[0],row[1])
        #print len(row)
        #new_item = tuple(row)
        #aaa= '---'.join(new_item).decode('utf-8')
        #G.add_edge(*new_item)

#print nx.degree(G)
pos = nx.random_layout(G)
nx.draw(G,pos,node_size=0,font_size=12)
plt.show()
