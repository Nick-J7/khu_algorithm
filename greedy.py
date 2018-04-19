import numpy as np

V = ['a', 'b', 'c', 'd', 'e', 'f']
E = [
    ('a', 'b', 2), ('a', 'c', 3),
    ('b', 'c', 4), ('b', 'd', 1), ('b', 'e', 7),
    ('c', 'd', 3), ('c', 'e', 1),
    ('d', 'e', 2), ('d', 'f', 5),
    ('e', 'f', 4)
    ]

W = np.array(
    [[np.inf, 2, 3, np.inf, np.inf, np.inf],
     [2, np.inf, 4, 1, 7, np.inf],
     [3, 4, np.inf, 3, 1, np.inf],
     [np.inf, 1, 3, np.inf, 2, 5],
     [np.inf, 7, 1, 3, np.inf, 4],
     [np.inf, np.inf, np.inf, 5, 4, np.inf]])

def my_prim():
    """Spanning tree search algorithm.
    There are two groups. one is composed of passed vertices and the other is composed of not passed.
    1. Select the nearest vertex which belongs to not passed group.
    2. Check if the selected edge is suitable to current tree.
    3. Check if the tree which is added with selected vertex and edge is optimal.
    :return: None
    """
    n = len(V)

    min_cost = 0
    total_group = set(V)
    pass_group = set(['a'])
    no_pass_group = total_group - pass_group
    spanning_tree_edge_list = []

    for i in range(n-1):
        connected_node_list = []
        min_next_node = None
        min_edge = None
        min_dist = 987654321
        for vertex in pass_group:
            for edge in E:
                if edge[0] == vertex and edge[1] in no_pass_group:
                    connected_node_list.append(edge)
                    if min_dist > edge[2]:
                        min_next_node = edge[1]
                        min_edge = edge
                        min_dist = edge[2]
                elif edge[1] == vertex and edge[0] in no_pass_group:
                    connected_node_list.append(edge)
                    if min_dist > edge[2]:
                        min_next_node = edge[0]
                        min_edge = edge
                        min_dist = edge[2]
        if min_next_node is not None:
            pass_group.add(min_next_node)
            no_pass_group.remove(min_next_node)
            min_cost += min_dist
            spanning_tree_edge_list.append(min_edge)

    print(min_cost)
    print(spanning_tree_edge_list)


def prim():
    n = 6
    F = set()
    min_cost = 0
    nearest = np.zeros(n, dtype=np.int32)
    distance = np.zeros(n, dtype=np.float32)

    # Start node = 0
    for i in range(1, n):
        nearest[i] = 0
        distance[i] = W[0][i]

    # Add (n-1) edge
    for i in range(n-1):
        # Find minimum distance
        min_dist = np.inf
        near_node = None
        for j in range(1, n):
            if 0 <= distance[j] < min_dist:
                min_dist = distance[j]
                near_node = j

        F.add((nearest[near_node], near_node))
        min_cost += min_dist
        distance[near_node] = -1
        for j in range(1, n):
            if W[j][near_node] < distance[j]:
                distance[j] = W[j][near_node]
                nearest[j] = near_node

    print(F)
    print(min_cost)


if __name__ == '__main__':
    my_prim() # slow
    prim()



