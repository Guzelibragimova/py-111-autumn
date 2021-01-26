from typing import Hashable, List
import networkx as nx

from collections import deque
import matplotlib.pyplot as plt

def draw_graph(g: nx.Graph):
    nx.draw(g, with_labels=True)
    plt.savefig('graph.png')

def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    # visited = {node: False for node in g.nodes} #как словарь посещенных вершин джи нодес содержит все вершины что я их не посещала
    # d = deque()
    #
    # d.append(start_node)
    # visited[start_node] = True
    # path = []
    #
    # while d:
    #     current_node = d.popleft() #снимаем с очереди новы элеимент
    #     path.append(current_node) # добавляем в путь
    #     for neib in g[current_node]:
    #         if not visited[neib]: # по ключу обращаемся к вершине графу
    #             d.append(neib)
    #             visited[neib] = True
    #
    #
    # return path

    visited = []
    queue1 = deque([start_node])
    visited.append(start_node)
    while queue1:
        vertex = queue1.popleft()
        for neighbour in g[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue1.append(neighbour)
    return visited


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])

    print(graph.nodes)
    print(graph['A'])
    print(list(graph.neighbors('A')))
    draw_graph(graph)