def union(list_a, list_b):
    # Convert both lists to sets
    set_a = set(list_a)
    set_b = set(list_b)

    # Compute the union of the two sets
    union_set = set_a.union(set_b)

    # Convert the union set back to a list if needed
    ulist = list(union_set)

    return ulist


def intersection(list_a, list_b):
    # Convert both lists to sets
    set_a = set(list_a)
    set_b = set(list_b)

    # Compute the intersection of the two sets
    intersection_set = set_a.intersection(set_b)

    # Convert the intersection set back to a list if needed
    intersection_list = list(intersection_set)

    return intersection_list


def calculate_sim(list_a, list_b):
    try:
        intersection_len = len(intersection(list_a, list_b))
        union_len = len(union(list_a, list_b))

        # Check for division by zero
        if union_len == 0:
            return 0.0

        return intersection_len / union_len
    except Exception as e:
        print('[-] Error : ' + str(e))
