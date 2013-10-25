import networkx as nx
import matplotlib.pyplot as plt
import copy


def compare(li1, li2):
    for i, j in zip(li1, li2):
        if i != j:
            return False
    return True


def set_node_position(G, node=None, position=None):
    fig = plt.gcf()
    axes = plt.gca()
    node_index = G.nodes().index(node)
    no_of_nodes = G.number_of_nodes()

    if node:
        # move node
        x, y = position
        nodes_collection = axes.get_children()[no_of_nodes + 2]
        prev_positions = nodes_collection.get_offsets()
        prev_position = copy.deepcopy(prev_positions[node_index])
        prev_positions[node_index] = [x, y]

        # move edge
        edges_collection = axes.get_children()[no_of_nodes + 3]
        for edge in edges_collection.get_paths():
            print(edge.vertices)
            if compare(edge.vertices[0], prev_position):
                edge.vertices[0] = position
            elif compare(edge.vertices[1], prev_position):
                edge.vertices[1] = position

        # move label
        label = axes.get_children()[node_index + 2]
        label.set_position([x,y])

    plt.draw()