#!/usr/bin/python2


def highest_product(lst):
    if len(lst) < 3:
        raise "List should have at least 3 items."

    highest_values = [0, 0, 0]
    highest_values_n = [0, 0]
    for v in lst:
        if v >= 0:
            if v > min(highest_values):
                idx = highest_values.index(min(highest_values))
                highest_values[idx] = v
        if v < 0:
            # If abs new value more that min in negative list
            # replace it with new value
            if v < max(highest_values_n):
                idx = highest_values_n.index(max(highest_values_n))
                highest_values_n[idx] = v

    prod_of_two_p = reduce(lambda x, y: x * y, highest_values)/max(highest_values)
    prod_of_two_n = reduce(lambda x, y: x * y, highest_values_n)

    if prod_of_two_n > prod_of_two_p:
        final_prod = reduce(lambda x, y: x * y, highest_values_n) * max(highest_values)
    else:
        final_prod = reduce(lambda x, y: x * y, highest_values)

    print final_prod


if __name__ == "__main__":
    list_of_ints = [-10,-10,1,3,2]
    highest_product(list_of_ints)
