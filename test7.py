#coding=utf-8
import csv
import networkx as nx
import matplotlib.pyplot as plt
'''
g=nx.Graph()
g.add_edge(u'张三',u'李四')
g.add_edge(u'张三',u'王五')
print g.nodes()
nx.draw_networkx(g)
plt.show()

'''
G=nx.Graph()

reader=csv.reader(file('sing.csv','rb'))
for row in reader:
        if reader.line_num ==1:
                continue
        for i in range(len(row)):
                print row[i]
                print '_____________'
        G.add_edge(row[0].decode('utf-8'),row[1].decode('utf-8'))
        #print len(row)
        #new_item = tuple(row)
        #aaa= '---'.join(new_item).decode('utf-8')
        #G.add_edge(*new_item)

#print nx.degree(G)
pos = nx.spring_layout(G)
nx.draw_networkx(G,pos,node_size=1000)
plt.show()
