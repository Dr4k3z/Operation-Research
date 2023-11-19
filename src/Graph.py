# this implementation is inspired by this tutorial:
#https://www.bogotobogo.com/python/python_graph_data_structures.php#:~:text=A%20graph%20can%20be%20represented,%2Cv%20%5Cin%20V%24.


class Vertex:
    #Constructors
    def __init__(self,node):
        self.__id = node
        self.__adjacent = {} #dictionary
    
    #Overloaded methods
    def __str__(self):
        return str(self.__id) + ' adjacent: ' + str([x.__id for x in self.__adjacent]) + "\n"

    #Public methods
    def add_neighbor(self, neighbor, weight=0):
        self.__adjacent[neighbor] = weight

    #Getters and setters
    def get_id(self):
        return self.__id

    def get_weight(self, neighbor):
        return self.__adjacent[neighbor]
    
    def get_connections(self):
        return self.__adjacent.keys()  


'''
class Graph:
    #Constructors
    def __init__(self):
        self.__vert_dict = {}
        self.__num_vertices = 0

    #Overloaded methods
    def __iter__(self):
        return iter(self.vert_dict.values())
    
    def __str__(self):
        new_str = ""
        for vert in self.__vert_dict:
            print(str(vert))
            new_str += str(vert) 
        return new_str

    #Public methods
    def add_vertex(self, node):
        self.num_vertices = self.__num_vertices + 1
        new_vertex = Vertex(node)
        self.__vert_dict[node] = new_vertex
        return new_vertex

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.__vert_dict:
            self.add_vertex(frm)
        if to not in self.__vert_dict:
            self.add_vertex(to)

        self.__vert_dict[frm].add_neighbor(self.__vert_dict[to], cost)
        self.__vert_dict[to].add_neighbor(self.__vert_dict[frm], cost)

    #Getters and setters
    def get_vertex(self, n):
        if n in self.__vert_dict:
            return self.__vert_dict[n]
        else:
            return None

    def get_vertices(self):
        return self.__vert_dict.keys()
'''

class Node:
    #Constructors
    def __init__(self,name,val):
        self.__id = name
        self.value = val
        self.__forwardStar = []
        self.__backwardStar = []

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
        
    #Getters
    def getValue(self,id):
        try:
            return self.__nodes[id].value
        except:
            print("Error! Wrong id")
            return None