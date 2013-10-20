import networkx as nx
import matplotlib.pyplot as plt


def set_node_position(G, node=None, position=None):
    fig = plt.gcf()
    axes = plt.gca()
    index = G.nodes().index(node)
    no_of_nodes = G.number_of_nodes()

    if node:
        # move node
        x, y = position
        nodes_collection = axes.get_children()[no_of_nodes + 2]
        prev_positions = nodes_collection.get_offsets()
        prev_position = prev_positions[index]
        prev_positions[index] = [x, y]

        # move edge
        edges_collection = axes.get_children()[no_of_nodes + 3]
        for edge in edges_collection.get_paths():
            if edge.vertices[0] == prev_position:
                edge.vertices[0] = position
            elif edge.vertices[1] == prev_position:
                edge.vertices[1] = position

        label = axes.get_children()[index + 2]
        label.set_position([x,y])

    plt.draw()