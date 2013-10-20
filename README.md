nx_animation
============

Animation Module for NetworkX using Matplotlib

Example:
```python
import networkx as nx
import random
import matplotlib.animation as animation
import nx_animation
import matplotlib.pyplot as plt

# Graph Initialization
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1,2), (2,3), (2,5), (1,5), (2,5)])
nx.draw(G)

# animation function for having node labelled 1 to move to random positions
# If you are moving nodes it's labels and the corresponding edges will also 
# move to their new positions

def animate_one(i):
    nx_animation.set_position(G, node=1, position=(random.uniform(0,1), random.uniform(0,1)))

# calling Matplotlib's FuncAnimation
anim = animation.FuncAnimation(plt.gcf(), animate)

# animation function for having each node take random positions
def animate1_two(i):
    nx_animation.set_position(G, position=[[random.uniform(0,1) for i in range(2)]
                                        for j in range(5)])

anim = animation.FuncAnimation(plt.gcf(), animate)

colors_list = ['r', 'b', 'g', 'm']

# animation function for taking random colors. If only single color is specified
# all the nodes will have that color

TODO: add another function for changing only one node
def animate_three(i):
    nx.animation.set_color(G, new_colors=[random.choice(colors_list) for i in range(5)])

anim = animation.FuncAnimation(plt.gcf(), animate)
```
All other properties can be changed in matplotlib's `PathCollection` and 
`LineCollection` objects can also be edited.
