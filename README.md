# Spectral partitioning for graphs

### Spectral partitioning 
Partitioning using graphs spectral properties (eigenvectors and eigenvalues). 
https://en.wikipedia.org/wiki/Graph_partition#Spectral_partitioning_and_spectral_bisection

### How to use
pip install -r requirements.txt 
python main.py input_file output_file cluster_amount

### About the input and output files
Input file should consist of edges. Each edge should be on its own row. 
The vertex IDs should range from 0 to amount of vertices - 1. 
On each row of the output file there will be a vertex ID followed by its cluster ID. 
 
Test file gotten from http://networkrepository.com/
