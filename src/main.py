import sys
from graph import Graph
from partition import spectral_partition
from utils import rename_vertices

def output_clusters(clusters, file_name):
    # Writes the output clustering to a file 
    with open(file_name, 'a') as f:
        f.write('\n'.join('%s %s' % (i, j) for i, j in enumerate(clusters)))
    
if __name__ == "__main__":
    # Takes 3 arguments input file, output file and amount of cluster.
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    k = sys.argv[3]
    graph = Graph()
    with open(input_path) as f:
        for line in f:
            v1, v2 = line.split()
            v1 = int(v1)
            v2 = int(v2)
            edge = (v1, v2)
            graph.add_edge(edge)
    
    partition = spectral_partition(graph, k)
    output_clusters(partition, output_path)