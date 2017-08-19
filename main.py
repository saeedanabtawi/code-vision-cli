from Loader import load, filter
from Similarity import similarity
from Result import cluster
import optparse
import time

def main():

    # Command line Usage
    parser = optparse.OptionParser("usage : "+"-i <input dirtory> -o <output dirtory> -a <algorithem> -t <threshold>")
    parser.add_option('-i', dest='in_dir', type='string', help='input dirtory must be in project folder')
    parser.add_option('-o', dest='out_dir', type='string', help='output dictionary must be in porject folder')
    parser.add_option('-a', dest='algorithem', type='string', help='algorithem value "jacard" xor "lcs"')
    parser.add_option('-t', dest='threshold', type='float', help='Threshold value 0.00 - 1.00')
    (options, arg) = parser.parse_args()

    if(options.in_dir is None or options.out_dir is None or options.threshold is None or options.algorithem is None):

        print (parser.usage)
        exit(0)


    in_dir = options.in_dir
    out_dir = options.out_dir
    algorithem = options.algorithem
    threshold = options.threshold

    start = time.time()
    code_dict = load.load_code_from_dir(in_dir)

    if algorithem == "jaccard":
        jaccard_ready_dict = filter.jaccard_filter(code_dict)
        similarity_graph_data = similarity.similarity(jaccard_ready_dict, algorithem)
    elif algorithem == "lcs":
        lcs_ready_dict = filter.lcs_filter(code_dict)
        similarity_graph_data = similarity.similarity(lcs_ready_dict, algorithem)
    else:
        print (parser.usage)
        exit(0)

    #bulid a graph  form keyword Dictionary
    # @TODO "cluster" replaced with "graph", "out_dir" wth "out_file"
    cluster.build_graph(cluster.list_to_graph(similarity_graph_data), threshold, out_dir+"/"+algorithem+"_out_weighted_graph.png")
    #cluster.build_graph(cluster.list_to_graph(similarity_graph_data), threshold, out_dir+"/out_weighted_graph.png")
    end = time.time()
    print(end-start,'s')
    #Draw Graph ,  save image in ouput file
    #Cluster.buildGraph(Graph,threshold,out_dir)

    pass

if __name__ == '__main__':
    main()
