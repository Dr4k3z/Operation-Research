# this implementation is inspired by this tutorial:
#https://www.bogotobogo.com/python/python_graph_data_structures.php#:~:text=A%20graph%20can%20be%20represented,%2Cv%20%5Cin%20V%24.

class Node:
    #Constructors
    def __init__(self,name,val):
        self.__id = name
        self.value = val
        self.cost = 0
        self.__forwardStar = []
        self.__backwardStar = []

        self.coordinates = [] #for graphical porpouse

    #Overloaded methods
    def __str__(self):
        return "Node: " + str(self.__id) +\
                "\nPointed by: " + str([bs.__id for bs in self.__backwardStar]) +\
                "\nPoints to: " + str([fs.__id for fs in self.__forwardStar])

    #Public methods
    def connect(self,n,dir="Forward"):
        if dir == "Forward":
            self.__forwardStar.append(n)
        elif dir == "Backward":
            self.__backwardStar.append(n)
    
    #Getters
    def getId(self):
        return self.__id
    
    def getFS(self):
        return self.__forwardStar
    
    def getBS(self):
        return self.__backwardStar
    
class Graph:
    #Constructors
    def __init__(self):
        self.__nodes = {} #dictionary key is node id
        self.__arches = [] #arch is an array of two nodes: tail and head

    #Overloaded methods
    def __str__(self):
        new_str = ""
        for n in self.__nodes:
            new_str += str(n) + " -> "
        
        new_str += "\n"

        for a in self.__arches:
            new_str += str(a[0].getId()) + " connects to " + str(a[1].getId()) + "\n"

        return new_str

    #Public methods
    def addNode(self,n,dir="Forward"):
        self.__nodes[n.getId()] = n

    def addArch(self,arch):
        if arch[0] not in self.__nodes:
            self.addNode(arch[0])
        if arch[1] not in self.__nodes:
            self.addNode(arch[1])

        self.__nodes[arch[0].getId()].connect(arch[1],dir) # One direction
        self.__arches.append(arch)
        

    def findPath(self,s,t):
        # Initialization
        P = {}
        for node in self.__nodes:
            P[node] = 0
        P[s.getId()] = s.getId()
        Q = [s]

        while Q!=[]:
            curr = Q[0]
            del Q[0]
            if curr==t:
                #print(P)
                return P
            
            for node in curr.getFS():
                if P[node.getId()] == 0:
                    P[node.getId()] = curr.getId()
                    Q.append(node)
            if Q==[]:
                return False

    def isConnected(self):
        # returns True if the graph is fully connected
        pass

    def isCyclic(self):
        pass

    def isNegative(self):
        # returns True if the graph has negative costs
        for n in self.__nodes:
            if n.cost < 0:
                return True
        return False

    #Getters
    def getValue(self,id):
        try:
            return self.__nodes[id].value
        except:
            print("Error! Wrong id")
            return None
        
    def getNodes(self):
        return self.__nodes
    
    def getArches(self):
        return self.__arches