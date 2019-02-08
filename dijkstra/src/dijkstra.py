#!/usr/bin/python3
# coding: utf-8

'''
 Name: Michael Young
 Email: michaelyangbo@outlook.com
 Date: 2019/2/8
 Ref.:  https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
'''
import networkx as nx
import matplotlib.pylab as plt


def draw_pic(graph, color_map):
    # store the edge has been add to G
    edge = []
    width=[]
    G = nx.Graph()
    # store the edge need to be color red
    target_edges = []

    # add node
    for node in graph:
        G.add_node(node)

    # pick the edge need to color red into target_edge
    for index, node in enumerate(shortest_path_pic):
        if index < len(shortest_path_pic) - 1:
            target_edges.append([node, shortest_path_pic[index + 1]])
            target_edges.append([shortest_path_pic[index + 1], node])

    for outerNode in graph.items():

        for innerNode in outerNode[1].items():

            if [innerNode[0], outerNode[0]] not in edge:
                edge.append([outerNode[0], innerNode[0]])
                G.add_edge(outerNode[0], innerNode[0], length=innerNode[1])
                width.append(innerNode[1]/150)
                edge_color_map.append('black')
                for target_edge in target_edges:
                    if [outerNode[0], innerNode[0]] == target_edge:
                        edge_color_map.pop()
                        edge_color_map.append('red')
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, edge_color=edge_color_map,width=width)

    plt.show()


def dijkstra(graph, src, dest, visited=[], distances={}, predecessors={}):
    global shortest_path_pic
    if src not in graph:
        raise TypeError('the root of the shortest path tree cannot be found in the graph')
    if dest not in graph:
        raise TypeError('the target of the shortest path cannot be found in the graph')
    # ending condition
    if src == dest:
        # build the shortest path and display it
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
            shortest_path_pic = path
        print('shortest path: ' + str(path) + " cost=" + str(distances[dest]))
    else:
        # if it is the initial run, initializes the cost
        if not visited:
            distances[src] = 0
        # visit the neighbors
        for neighbor in graph[src]:
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijkstra with src='x'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, dest, visited, distances, predecessors)


if __name__ == "__main__":
    # store shortest path
    shortest_path_pic = []
    # store color
    edge_color_map = []
    graph = {'a': {'b': 100, 'c': 200},
             'b': {'a': 100, 'c': 300, 'd': 500},
             'c': {'a': 200, 'b': 300, 'e': 600},
             'd': {'b': 500, 'e': 400, 'f': 200},
             'e': {'c': 1000, 'd': 400, 'f': 100},
             'f': {'d': 200, 'e': 100}}
    dijkstra(graph, 'a', 'f')
    draw_pic(graph, edge_color_map)
