#coding=utf-8
import csv
import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()
g.add_edge(u'张三',u'李四')
g.add_edge(u'张三',u'王五')
nx.draw_networkx(g)
plt.show()

'''
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
nx.draw_networkx(G,pos)
plt.show()
'''