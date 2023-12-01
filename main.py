import numpy as np
import time
from src.LinearProblem import LinearProblem
from src.Graph import Node,Graph
from src.PlotGraph import drawTree

'''
            What's next??

1)  Not sure the program works where no admissible basis 
    can be found. Implement Phase I simplex

2)  The algo does not manage the case of an illimitate 
    problem. Add limitation clause in the j = argmin section

3)  Test the script for performance in terms of execution 
    time and memomary management, I bet there's still a lot 
    of room for improvement. Develop an actual benchmark, 
    not the one currently implemented

4)  Adapt the optimum outcome to the actual scope, wether a 
    maximization or minimization
    
5)  Implement other methods to solve a linear programming 
    problem. 

6)  Define graphs and related problems (connectivity, mininum cost tree,
    covarage et cetera) and algorithms to solve them

7)  Develop smart way to visualize graphs 

8)  Graphical interpretation of linear programming problems, only in 
    two dimensions
'''
def linearProblem():
    A = np.array([[1,2,3,1],
                  [2,1,1,2]])
    b = np.array([3,4])
    c = np.array([-1,-3,-5,-2]) 
    prob = LinearProblem(A,b,c)
    sol = prob.solve("simplex")
    print("Variables in base:", sol[0], "\nCorrispective values:", sol[1])
    print("Optimum:", prob.optimum())
    
    '''#Illimitate Problem example:
    print()
    A = np.array([[2,1,1],
                  [1,1,2]])
    b = np.array([6,2])
    c = np.array([3,1,1]) 
    prob = LinearProblem(A,b,c)
    sol = prob.solve("simplex")
    print("Variables in base:", sol[0], "\nCorrispective values:", sol[1])
    print("Optimum:", prob.optimum())'''

def graphProblem():
    N = ['a','b','c','d','e']
    A = [[1,2],[2,3],[3,4]]
    n1 = Node('s',1)
    n2 = Node('1',1)
    n3 = Node('2',1)
    n4 = Node('3',1)
    n5 = Node('t',1)

    n1.connect(n2,"Forward")
    n1.connect(n3,"Forward")
    n2.connect(n4)
    n2.connect(n3)
    n3.connect(n4)
    n4.connect(n5) 

    graph = Graph()
    graph.addNode(n1)
    graph.addNode(n2)
    graph.addNode(n3)
    graph.addNode(n4)
    graph.addNode(n5)

    drawTree(graph)
    print(graph.findPath(n1,n5))

if __name__=="__main__":
    begin = time.time()
    graphProblem()
    end = time.time()
    delta = 1000*(end-begin)
    #print("time elapsed: ",delta)
