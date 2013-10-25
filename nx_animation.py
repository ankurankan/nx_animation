import networkx as nx
import matplotlib.pyplot as plt
import copy


def compare(li1, li2):
    for i, j in zip(li1, li2):
        if i != j:
            return False
    return True


def set_node_position(G, node=None, position=None):
    '''
    Moves node to position

    Parameters
    ----------
    G        : Graph whose nodes are to be moved
    node     : The node to move if not specified moves all the nodes to the
               corresponding position in position
    position : The new position of the node. If node specified should be in
               form (x,y) or [x,y]. If node not specified should be in form
               [(x1,y1), (x2,y2), (x3,y3)]. It must have new position for
               each node in the graph.

    Example
    -------
    set_node_position(G, node=1, position=[0.5, 0.5])
    set_node_position(G, node=1, position=(0.5, 0.5))
    #Considering graph G has 3 nodes
    set_node_position(G, position=[(0.1,0.1), (0.2, 0.2), (0.3, 0.3)]
    '''
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
            if compare(edge.vertices[0], prev_position):
                edge.vertices[0] = position
            elif compare(edge.vertices[1], prev_position):
                edge.vertices[1] = position

        # move label
        label = axes.get_children()[node_index + 2]
        label.set_position([x,y])

    plt.draw()