import networkx as nx
import time
import csv
# Create Graph using networkx
def read_csv_graph(csv_file):
    G = nx.Graph()
    # Open csv file where each line represents an edge "node1;node2;weight\n"
    with open(csv_file, 'r') as f:
        cont = f.read()
        for line in cont.split('\n'):
            if line != '':
                # Read line "edge" and add it to graph
                edge = line.split(';')
                G.add_edge(edge[0], edge[1], weight=float(edge[2]))
    return G


def write_csv_graph(Graph_csv):
    start = time.time()
    with open('./output/graph_out.csv', 'w') as csvfile:
        fieldnames = ['source', 'target', 'weight']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for edge in Graph_csv:
            row = {fieldnames[0]: edge[0], fieldnames[1]: edge[1], fieldnames[2]: edge[2]}
            writer.writerow(row)
    end = time.time()
    print('[+] Writing csv Done in : ' + str(end - start))
