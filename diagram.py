#coding=utf-8
import csv

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
DG = nx.DiGraph()

reader=csv.reader(file('sing.csv','rb'))

for row in reader:
        if reader.line_num ==1:
                continue
        #for i in range(len(row)):
                #print row[i]
        G.add_edge(row[0].decode('utf-8'),row[1].decode('utf-8'))
        #print len(row)
        #new_item = tuple(row)
        #G.add_edge(*new_item)

# 关于图形的方法：
nx.density(G)     #返回图形的密度
nx.degree_histogram(G) #返回列表中每个值的频率
nx.info(G)      #返回图形的摘要信息 ：节点数，边数，平均度 etc..
P=nx.create_empty_copy(G)  #返回 移除边的 图形G的 副本
nx.is_directed(DG)       #返回图形是否有向

#关于点的方法
nx.nodes(G)     #以列表的形式返回所有节点
nx.number_of_nodes(G)    #返回节点数




weight_g = sorted(G.degree().values())       #返回G中节点权重，并按排序输出结果
for each_item in G.nodes():
        if nx.degree(G)[each_item] >= weight_g[-1]:                           #找到邻居数大于设定值的节点i

                #print G.neighbors(each_item)

                for each_one in G.neighbors(each_item):
                        DG.add_edge(each_one,each_item)           #生成与i直接连接的图

#g = nx.compose(G,DG)    #返会合并公共的node???
pos = nx.spring_layout(G)
nx.draw_networkx(DG,pos,node_size=1000,font_size=8)
plt.show()
