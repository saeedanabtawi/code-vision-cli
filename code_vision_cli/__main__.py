import argparse
import sys
import time
import os
import logging

from tqdm import tqdm

from code_vision_cli.loader import load, filter
from code_vision_cli.similarity import similarity
from code_vision_cli.result import cluster


def main():
    parser = argparse.ArgumentParser(description='Process code similarity.')
    parser.add_argument('-i', '--in_dir', required=True, help='Input directory must be in the project folder')
    parser.add_argument('-o', '--out_dir', required=True, help='Output directory must be in the project folder')
    parser.add_argument('-a', '--algorithm', choices=['jaccard', 'lcs'], required=True,
                        help='Algorithm to use: "jaccard" or "lcs"')
    parser.add_argument('-t', '--threshold', type=float, required=True, help='Threshold value between 0.00 and 1.00')
    args = parser.parse_args()

    # Check if input directory exists
    if not os.path.exists(args.in_dir):
        logging.error(f"Input directory {args.in_dir} does not exist.")
        return

        # Check if output directory exists, if not, create it
    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)

    # Load and process code
    start = time.time()
    code_dict = load.load_code_from_dir(args.in_dir)

    if args.algorithm == "jaccard":
        filtered_dict = filter.jaccard_filter(code_dict)
    elif args.algorithm == "lcs":
        filtered_dict = filter.lcs_filter(code_dict)
    else:
        logging.error("Invalid algorithm specified.")
        return

    similarity_graph_data = similarity.similarity(filtered_dict, args.algorithm)

    # Build and save the graph
    graph_filename = os.path.join(args.out_dir, f"{args.algorithm}_out_weighted_graph.png")
    # Create a tqdm progress bar with the total number of items
    with tqdm(total=1, desc="[+] Rendering cluster", unit='cluster') as pbar:
        cluster.build_graph(cluster.list_to_graph(similarity_graph_data), args.threshold, graph_filename)
        pbar.update(1)

    end = time.time()
    print(f"[+] Processing completed in {end - start} seconds.")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())
