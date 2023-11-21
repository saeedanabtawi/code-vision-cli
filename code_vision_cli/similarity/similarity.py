from tqdm import tqdm
import itertools

from . import jaccard, lcs


def save_operation(key, xkey, xhash):
    strpair = key + '-' + xkey
    xstrpair = xkey + '-' + key

    xhash[strpair] = True
    xhash[xstrpair] = True

    pass


def similarity(ready_dict, algorithm):
    # Save operations in history like p(a, b) = p(b, a) for non-repeating operation
    history = {}

    # 2D array represents edges in a graph
    graph_data = []

    # Calculate the total number of iterations for the progress bar
    total_iterations = len(list(itertools.combinations(ready_dict.keys(), 2)))

    # Create a tqdm progress bar with the total number of iterations
    with tqdm(total=total_iterations, desc="[+] Calculating Similarity", unit="comparison") as pbar:
        for key, value in ready_dict.items():
            for xkey, xvalue in ready_dict.items():
                # Checking history and key => p(a, b) = p(b, a) and p(a, a) = 1
                if not ((key + '-' + xkey) in history) and (key != xkey):
                    # Saving operation in history
                    save_operation(key, xkey, history)

                    if algorithm == "jaccard":
                        sim = jaccard.calculate_sim(value, xvalue)
                    elif algorithm == "lcs":
                        sim = lcs.calculate_sim(value, xvalue)
                    else:
                        # Raise error "invalid algorithm"
                        # @TODO NotImplementedError
                        raise NotImplementedError("Invalid algorithm")

                    # Creating a similarity row (edge)
                    row = [key, xkey, sim]

                    # Add row (edge) to graph
                    graph_data.append(row)

                    # Update the progress bar
                    pbar.update(1)

    return graph_data
