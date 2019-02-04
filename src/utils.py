def rename_vertices(input_name, output_name=None):
    # Renames the vertices in input file to start from 0 and to end in |vertices| - 1
    # Writes that to output file
    
    if output_name == None:
        output_name = input_name
    vertices = {}
    edges=[]
    i = 0

    with open(input_name) as f:
        for line in f:
            v1, v2 = line.split()
            v1 = int(v1)
            v2 = int(v2)
            if v1 not in vertices:
                vertices[v1] = i
                i+=1
            if v2 not in vertices:
                vertices[v2] = i
                i+=1
            edges.append((vertices[v1], vertices[v2]))
    
    with open(output_name, 'a') as f:
        f.write('\n'.join('%s %s' % (i, j) for i, j in edges))

