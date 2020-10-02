def has_negatives(a):
    # input & output can be in any order

    cache = {}  # initialize empty cache
    result = []  # result needs to be a list

    # loop through input list
    for i in a:
        # if the negative version of i is in the list, add to result list
        if -i in cache:
            if i > 0:  # must be greater than zero in order to have a corresponding negative value
                result.append(i)
            else:
                result.append(-i)
        else:  # if there is not a corresponding negative, add i to cache
            cache[i] = ""

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


print(has_negatives([1, -1, -3, 4, 5, 3, -2, 2, 111, 112, -111]))
