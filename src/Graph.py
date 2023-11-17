# this implementation is inspired by this tutorial:
#https://www.bogotobogo.com/python/python_graph_data_structures.php#:~:text=A%20graph%20can%20be%20represented,%2Cv%20%5Cin%20V%24.


class Vertex:
    #Constructors
    def __init__(self,node):
        self.__id = node
        self.__adjacent = {} #dictionary
    
    #Overloaded methods
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent]) + "\n"

    #Public methods
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    #Getters and setters
    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    def get_connections(self):
        return self.adjacent.keys()  


class Graph:
    #Constructors
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    #Overloaded methods
    def __iter__(self):
        return iter(self.vert_dict.values())
    
    def __str__(self):
        new_str = ""
        for vert in self.vert_dict:
            print(vert)
            new_str += str(vert) 
        return new_str

    #Public methods
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    #Getters and setters
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def get_vertices(self):
        return self.vert_dict.keys()
