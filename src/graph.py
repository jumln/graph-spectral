class Graph(object):

    def __init__(self):
        self.__graph_dict = {}
        self.edges = set()

    def vertices(self):
        """ Returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def add_edge(self, edge):
        """ Adds an edge (tuple of vertices) to the graph """
        v1, v2 = edge
        if v1 in self.__graph_dict:
            self.__graph_dict[v1].add(v2)
        else:
            self.__graph_dict[v1] = {v2}
        if v2 in self.__graph_dict:
            self.__graph_dict[v2].add(v1)
        else:
            self.__graph_dict[v2] = {v1}
        self.edges.add(edge)