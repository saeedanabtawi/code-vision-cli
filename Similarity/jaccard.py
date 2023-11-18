# function  that calculate union between two lists of keywords
def union(list_a, list_b):
    # ulist : is the union  list
    # copying list_b to union list
    ulist = list(list_b)

    # take evey element in list_a then search in list_b if does not exist add it to the union list
    for x in list_a:
        if not x in list_b:
            # add element to union list
            ulist.append(x)

    return ulist


# function  that calculate intersection between two lists of keywords
def intersection(list_a, list_b):
    return [x for x in list_a if x in list_b]


# function to calculate the similarity between two lists
def calculate_sim(list_a, list_b):
    try:
        return (len(intersection(list_a, list_b))) / (len(union(list_a, list_b)))
    except Exception as e:
        print('[-] Error : ' + str(e))
