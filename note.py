
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

#关于边的方法
nx.edges(G)     #以列表的形式返回所有的边
nx.number_of_edges(G)   #返回边数
nx.non_edges(G)         #以iterator的形式返回所有不存在的边
nx.edges_iter(G)        #以iterator的形式返回所有边
