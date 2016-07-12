import networkx as nx


# 关于图形的方法：
nx.density(G)     #返回图形的密度
nx.degree_histogram(G) #返回列表中每个值的频率
nx.info(G)      #返回图形的摘要信息 ：节点数，边数，平均度 etc..
P=nx.create_empty_copy(G)  #返回 移除边的 图形G的 副本
nx.is_directed(DG)       #返回图形是否有向

#关于点的方法
nx.nodes(G)     #以列表的形式返回所有节点
nx.number_of_nodes(G)    #返回节点数
nx.all_neighbors(G,'tank')    #以iterator的形式返回一个节点的所有邻居
nx.non_neighbors(G,'tank')    #以iterator的形式返回一个节点的所有非邻居
nx.common_neighbors(G,'','') #以iterator的形式返回两个节点的公共邻居
nx.nodes_iter(G)              #以iterator的形式返回所有节点
g = nx.compose(G,DG)    #返会合并公共的node???
sorted(G.degree().values())

#关于边的方法
nx.edges(G)     #以列表的形式返回所有的边
nx.number_of_edges(G)   #返回边数
nx.non_edges(G)         #以iterator的形式返回所有不存在的边
nx.edges_iter(G)        #以iterator的形式返回所有边

#关于MultiDiGraph()
G.successors(node)  #返回一个节点的后继
G.predecessor(node) #返回一个节点的前任
G.number_of_edges(node,node)    #返回两个节点间的边数
G.size()    #返回图的边数
G.nodes_with_selfloops()    #以列表形式返回(自己到自己）的节点
G.out_degree()  #返回向外联系的数量；括号中可以填点，返回点的；也可不填，返回所有点的列表