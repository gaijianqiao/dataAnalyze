
"""狄克斯特拉算法"""
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

graph = {}

graph['you'] = ["alice","bob","claire"]
graph['start']={}
graph['start']["a"] = 6
graph['start']['b'] =2

print(graph['start'].keys())

graph['a']={}
graph['a']['fin'] = 1
graph['b']={}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin']={}

infinity = float("inf")

print(1/infinity)

costs = {}

costs['a']=6
costs['b']=2
costs['fin'] = infinity

parents={}
parents['a']='start'
parents['b']='start'
parents['fin']=None

processed = []
#未处理节点中找到开销最小的节点
node = find_lowest_cost_node(costs)

while node is not None:
    # 得到到当前节点的开销
    cost = costs[node]
    # 取出需要计算的邻居
    neighbors = graph[node]
    # 改变邻居对应的开销
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if cost[n] >new_cost:
            costs[n]=new_cost
            parents[n] = node
    processed.append(node)
    #重复执行找出没有被处理节点中，最小权重的那个
    node = find_lowest_cost_node(costs)

