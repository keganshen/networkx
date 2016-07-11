#coding=utf-8
import csv
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
DG = nx.DiGraph()

reader=csv.reader(file('C:/nx/networkx/test.csv','rb'))

for row in reader:
        if reader.line_num ==1:
                continue
        #for i in range(len(row)):
                #print row[i]
        G.add_edge(row[0].decode('utf-8'),row[1].decode('utf-8'))
        #print len(row)
        #new_item = tuple(row)
        #G.add_edge(*new_item)


weight_g = sorted(G.degree().values())       #返回G中节点权重，并按排序输出结果
for each_node in G.nodes():
        if nx.degree(G)[each_node] >= weight_g[-1]:                           #找到邻居数大于设定值的节点i
                #print G.neighbors(each_item)

                for each_one in G.neighbors(each_node):
                        DG.add_edge(each_one,each_node)           #生成与i直接连接的图

print nx.max_clique(G)
#g = nx.compose(G,DG)    #返会合并公共的node???
pos = nx.spring_layout(G)
nx.draw_networkx(DG,pos,node_size=1000,font_size=8)
nx.freeze(G)
plt.show()
