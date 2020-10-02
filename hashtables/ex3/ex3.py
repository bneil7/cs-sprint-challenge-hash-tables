'''
(Output can be in any order.)

Limits:

There can be up to 10 lists in the list of lists.
The lists can contain up to roughly 1,000,000 elements each.
'''


def intersection(arrays):
    # empty dictionary initialized
    dict = {}

    list_of_lists = len(arrays)  # up to 10 lists inside list_of_lists

    # loop through the "arrays" input for each list inside
    for each_list in arrays:
        # then loop through each_list for each item inside
        for each_item in each_list:
            # if an item exists in our dict{}, then increment the key count by 1
            if each_item in dict:
                dict[each_item] += 1
            # if not, then add 1 to the key count (which is zero since there's nothing there)
            else:
                dict[each_item] = 1

    result = []  # store the key counts from the items in the lists
    # loop through the dict to check the count of lists the item is in
    for key in dict:
        if dict[key] == list_of_lists:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

print(intersection([
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1, ]
]))
