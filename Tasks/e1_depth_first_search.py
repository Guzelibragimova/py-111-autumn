from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """

    # print(g, start_node)
    # return list(g.nodes)
    visited = set()
    if start_node not in visited:
        print(start_node)
        visited.add(start_node)
        for neibh in (g[start_node] - visited):
            dfs(g, neibh)
        return visited

if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
    ])

    print(graph.nodes)
    print(graph['A'])
    print(list(graph.neighbors('A')))


