'''
A brute-force solution would involve two nested loops, yielding a quadratic-runtime solution. How can we use a hash table in order to implement a solution with a better runtime?

Think about what we can store in the hash table in order to help us to solve this problem more efficiently.

What if we store each weight in the input list as keys? What would be a useful thing to store as the value for each key?

If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for limit - weight. If it does, then we've found the two items whose weights sum up to the limit!
'''


def get_indices_of_item_weights(weights, length, limit):
    # list of weights
    # weight limit item
    # find two items, sum of weight values == weight limit
    # return tuple of integers, ie. (zero, one), represents index of the item weights
    # if pair does not exist, return None
    if length <= 1:
        return None

    cache = {}

    # lines 39-48
    dup_bool = False  # initialize boolean for duplicates as False
    dup = {}  # cache duplicate values

    for i in range(0, length):
        # store weight value as key
        # store index as value
        current = weights[i]
        cache[current] = i
        # check if hashtable contains value for limit - weight
        target = limit - current

        if target in cache:
            if current > target or current < target:
                return (i, cache[target])

            # test fails if current == target
            # need elif to account for duplicate values
            # implemented boolean conditional above
            elif current == target:
                if dup_bool == False:
                    dup_bool = True
                    dup[current] = i

                elif dup_bool == True:
                    return (i, dup[current])

    return None


print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
