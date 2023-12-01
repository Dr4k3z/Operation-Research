import numpy as np
import matplotlib.pyplot as plt
from src.Graph import *

def drawNode(node,x,y):
    theta = np.arange(0, 2*np.pi, .05)
    label = str(node)
    plt.plot(x+0.1*np.cos(theta),y+0.1*np.sin(theta),color="black")
    plt.text(x-0.05,y-0.05,label,fontsize=12)

def drawArch(start,end):
    h = [0,0]
    h[0] = end[0]-start[0]
    h[1] = end[1]-start[1]
    plt.arrow(start[0],start[1],h[0],h[1],head_width=0.15, color='black', length_includes_head=True)

def drawTree(graph):
    nodes = graph.getNodes()
    arches = graph.getArches()
    n = len(nodes)
    m = len(arches)

    coordinates = [[0,0],[1,1],[1,-1],[2,1],[2,-1],[3,0]]

    i = 0
    for el in nodes:
        drawNode(el,coordinates[i][0],coordinates[i][1])
        i += 1

    for i in range(n-1):
        drawArch(coordinates[i],coordinates[i+1])

    plt.xlim([-1,4])
    plt.ylim([-4,4])
    plt.show()
