#coding=utf-8

#python diagram -d 1 -r 1 (d:递归次数 r:选取前几名）
import csv
import networkx as nx
import matplotlib.pyplot as plt
import sys
import getopt
from getopt import GetoptError

#getopt
try:
    opts,args = getopt.getopt(sys.argv[1:],'d:r:')
except GetoptError:
    sys.exit()
for key,values in opts:
    if key in ('-d',''):
        deep = int(values)
    if key in ('-r',''):
        rang = int(values)


G = nx.Graph()
DG = nx.Graph()

#参数h决定关联度（递归次数）
def howdeep(selected_nodes,h):
    if h > 0:
        h -= 1
        for each_item in nx.all_neighbors(G,selected_nodes):
            DG.add_edge(each_item,selected_nodes)
            howdeep(each_item,h)
    else:
        pass

reader=csv.reader(file('C:/nx/networkx/sing.csv','rb'))
#构图
for row in reader:
        if reader.line_num ==1:
                continue
        G.add_edge(row[0].decode('utf-8'),row[1].decode('utf-8'))

 #返回G中节点权重，并按排序输出结果
weight_g = sorted(G.degree().values())
for each_node in G.nodes():
         #找到邻居数大于设定值的节点i
        if nx.degree(G)[each_node] >= weight_g[-rang]:
                 #print G.neighbors(each_item)
                 howdeep(each_node,deep)
                 '''
                 #生成与i直接连接的图
                for each_one in G.neighbors(each_node):
                        DG.add_edge(each_one,each_node)
                        for each_neighbor in G.neighbors(each_one):
                                DG.add_edge(each_neighbor,each_one)
'''

pos = nx.spring_layout(G)
nx.draw_networkx(DG,pos,node_size=1000,font_size=8)
nx.freeze(G)
plt.show()
