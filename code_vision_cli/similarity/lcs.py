from bisect import bisect_right, bisect_left

# Dynamic programming (longest common sequence)
def dlcs(text1, text2):
    if len(text1) < len(text2):
        temp = text1
        text1 = text2
        text2 = temp

    indices = {}
    for i in range(len(text1)):
        c = text1[i]
        if c not in indices:
            indices[c] = [i]
        else:
            indices[c].append(i)

    seq = []
    for c in text2:
        if c not in indices:
            continue
        # Find smallest index > seq[-1].
        # If it exists, add to seq.
        if not seq:
            seq.append(indices[c][0])
        else:
            idx = bisect_right(indices[c], seq[-1])
            if idx < len(indices[c]) and indices[c][idx] > seq[-1]:
                seq.append(indices[c][idx])

            # For indices < seq[-1], replace in seq.
            for i in range(idx - 1, -1, -1):
                seq[bisect_left(seq, indices[c][i])] = indices[c][i]

        if not indices[c]:
            indices.pop(c)

    return len(seq)

def calculate_sim(text_a, text_b):
    try:
        return (2 * dlcs(text_a, text_b)) / (len(text_a) + len(text_b))
    except Exception as e:
        print('[-] Error : ' + str(e))
