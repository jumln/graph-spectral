import numpy as np

def degrees(adj_matrix):
    """ returns a list of degrees of the graph in order """
    return np.sum(adj_matrix, axis=1)

def degree_matrix(adj_matrix):
    """ returns the degree matrix of the graph """
    return np.diag(degrees(adj_matrix))

def adjacency_matrix(edges):
   """ returns the adjacency matrix of the graph """
   n = len(np.unique(list(edges)))
   adj_matrix = np.zeros((n, n))
   for v1, v2 in edges:
       adj_matrix[v1, v2] = 1
       adj_matrix[v2, v1] = 1
   return adj_matrix  

def laplacian_matrix(edges):
    """ returns laplacian matrix of the graph """
    adj_m = adjacency_matrix(edges)
    return degree_matrix(adj_m) - adj_m
    
def normalized_laplacian(edges):
    """ Return the normalized laplacian matrix of the graph as presented in  
        https://en.wikipedia.org/wiki/Laplacian_matrix#Laplacian_matrix_for_simple_graphs
    """
    n = len(np.unique(list(edges)))
    identity_matrix = np.identity(n)
    adj_m = adjacency_matrix(edges)

    sqrt_degs = 1 / np.sqrt(degrees(adj_m))
    sqrt_degs_matrix = np.diag(sqrt_degs)

    norm_lap = identity_matrix - np.dot(np.dot(sqrt_degs_matrix, adj_m), sqrt_degs_matrix)
    return norm_lap