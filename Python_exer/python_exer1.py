
"""The BFS is levelwise that means we will search level by level
at each step we can search for what is connected to this node and then
put the neighbours of that node inside a queue that will be a storage of
nodes, when we take out each node that means we have searched for it.
"""


from collections import deque
def BFS(graph, target):

    first_node = graph[0]
    nodes = deque([first_node])
    visited = set()

    while nodes:
        curr_node = nodes.pop()
        if curr_node == target:
            return
        if curr_node in visited:
            continue

        visited.add(curr_node)

        for neighbour in graph[curr_node]:
            nodes.append(neighbour)








