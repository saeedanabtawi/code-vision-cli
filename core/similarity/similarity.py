from . import jaccard, lcs


def save_opreation(key, xkey, xhash):
    strpair = key + '-' + xkey
    xstrpair = xkey + '-' + key

    xhash[strpair] = True
    xhash[xstrpair] = True

    pass


def similarity(ready_dict, algorithem):
    # save operation in history like  p(a, b) = p(b, a) for non repeating operation
    history = {}

    # 2d array represents edges in a graph
    graph_data = []

    for key, value in ready_dict.items():
        for xkey, xvalue in ready_dict.items():
            # checking history and key => p(a, b) = p(b, a) and  p(a, a) = 1
            if not ((key + '-' + xkey) in history) and (key != xkey):

                # Saving opreation in history
                save_opreation(key, xkey, history)

                if algorithem == "jaccard":
                    sim = jaccard.calculate_sim(value, xvalue)
                elif algorithem == "lcs":
                    sim = lcs.calculate_sim(value, xvalue)
                else:
                    # Raise error "invalid algorithm"
                    # @TODO ImplementedError
                    raise NotImplementedError

                # creating a similarity row (edge)
                row = [key, xkey, sim]

                # add row (edge) to graph
                graph_data.append(row)

    return graph_data
