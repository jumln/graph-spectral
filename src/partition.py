import scipy as sp
import numpy as np
from sklearn.cluster import KMeans
from matrix import normalized_laplacian

def spectral_partition(graph, k):
    """ Returns the spectral partitioning of a graph in k clusters """

    # Get the Normalized laplacian of the graph and find its eigenvectors and values
    print("--- Forming normalized laplacian ---")
    n_lap = normalized_laplacian(graph.edges)

    # Get the eigenvectors corresponding to the k smallest eigenvalues
    print("--- Calculating eigenvectors ---")
    _, vec = sp.sparse.linalg.eigsh(n_lap, k=k, which='SM')

    # Normalize each row to norm to 1
    norm_eig_vecs = normalize(vec)

    # Do K-means on the normalized eigenvectors to get k communities
    print("--- Doing K-means ---")
    kmeans = KMeans(n_clusters=k, random_state=300).fit(norm_eig_vecs)

    print("Conductance: ", get_cost(graph.edges, kmeans.labels_))

    return kmeans.labels_   

def normalize(matrix):
    """ Normalizes a matrix to have row norm of 1 """
    l2norm = np.sqrt((matrix * matrix).sum(axis=1))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            matrix[i,j] /= l2norm[i]
    return matrix

def smallest_community(clusters):
    """ Returns the size of the smallest community """
    _, counts = np.unique(clusters, return_counts=True)
    return min(counts)

def get_cost(edges, cluster):
    """ Returns the objective function to minimize """
    sc = smallest_community(cluster)
    n = get_cut_edges(cluster, edges)    
    cost = n / sc
    return cost

def get_cut_edges(cluster, edges):
    """ Returns edges that are cut after the partitioning """
    n = 0
    for edge in edges:
        v1, v2 = edge
        if(cluster[v1] != cluster[v2]):
            n += 1
    return n


