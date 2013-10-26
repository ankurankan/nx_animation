import matplotlib.pyplot as plt
import copy
import sys


def compare(li1, li2):
    for i, j in zip(li1, li2):
        if i != j:
            return False
    return True


def set_node_position(G, **kwargs):
    """
    Moves node to position

    Parameters
    ----------
    G        : Graph whose nodes are to be moved

    kwargs
    ------
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
    """
    try:
        node = kwargs['node']
    except KeyError:
        node = None
    try:
        position = kwargs['position']
    except KeyError:
        print("position argument required")
        sys.exit(0)

    # TODO: Recursive call the below for each node for it to work when no node is specified

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
        label.set_position([x, y])

    plt.draw()


def set_node_color(G, **kwargs):
    """
    Changes node colors

    Parameters
    ----------
    G     : Graph whose node's color needs to be changed

    kwargs
    ------
    node  : The node whose color needs to be changed. If node not specified
            and only one color is specified changes all the nodes to that
            color. If node not specified and color is a list or tuple of
            colors, each node will be changed to its corresponding color.

    color : Can be a single value of a list of colors.

    The following color abbreviations are supported:
    ==========  ========
    character   color
    ==========  ========
    'b'         blue
    'g'         green
    'r'         red
    'c'         cyan
    'm'         magenta
    'y'         yellow
    'k'         black
    'w'         white
    ==========  ========

    Examples:
    set_node_color(G, node=1, color='b')
    set_node_color(G, node=1, color=['b'])
    set_node_color(G, color=['r', 'b', 'g', 'y', 'm', 'k', 'c'])
    set_node_color(G, color='b')
    set_node_color(G, color=('b'))
    """
    try:
        node = kwargs['node']
    except KeyError:
        node = None
    try:
        color = kwargs['position']
    except KeyError:
        print("color argument required")
        sys.exit(0)

    if (isinstance(color, list) or isinstance(color, tuple)) and \
            len(color) == 1:
        color = color[0]

    colors_dict = {'b': [0.,    0.,    1.,  1.],
                   'g': [0.,    0.5,   0.,  1.],
                   'r': [1.,    0.,    0.,  1.],
                   'c': [0.,    0.75,  0.75,  1.],
                   'm': [0.75,  0.,    0.75,  1.],
                   'y': [0.75,  0.75,  0.,  1.],
                   'k': [0.,    0.,    0.,  1.],
                   'w': [1.,    1.,    1.,  1.]}

    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    nodes_collection = axes.get_children()[no_of_nodes + 2]

    # if node is specified manually changing the facecolor and edgecolor array
    # so that the colors for other nodes are retained
    if node:
        node_index = G.nodes().index(node)
        facecolor_array = nodes_collection.get_facecolor()
        edgecolor_array = nodes_collection.get_edgecolor()
        facecolor_array[node_index] = colors_dict[color]
        edgecolor_array[node_index] = colors_dict[color]

    # if node not specified call the matplotlib's set_color function
    else:
        nodes_collection.set_color(color)

    plt.draw()


def set_node_size(G, **kwargs):
    """
    Change node size

    Parameters
    ----------
    G    : The graph whose nodes are to be resized

    kwargs
    ------
    node : The node whose size is to be changed. If node not specified size
           of all the nodes will be changed.
    size : If size is an int and node specified, that node's size would be
           changed. If size is a list of tuple and no node specified each
           node will be changed to it's corresponding size. If node not
           specified and size is int all the nodes will be changed to that
           value.
    """
    try:
        node = kwargs['node']
    except KeyError:
        node = None
    try:
        size = kwargs['position']
    except KeyError:
        print("size argument required")
        sys.exit(0)

    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    nodes_collection = axes.get_children()[no_of_nodes + 2]

    if node:
        node_index = G.nodes().index(node)
        line_width_arr = nodes_collection.get_linewidths()
        line_width_arr[node_index] = size

    else:
        nodes_collection.set_linewidth(size)

    plt.draw()
