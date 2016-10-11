#!/usr/bin/python2


def get_products_of_all_ints_except_at_index(lst):
    product_lst = []
    for index in range(len(lst)):
        # Backup original value at index
        orig_val = lst[index]
        # Set value at index to 1
        lst[index] = 1
        # Calculate product and write to resulting list
        product_lst.insert(index, reduce(lambda x, y: x * y, lst))
        # Set original value at index
        lst[index] = orig_val
    print product_lst


if __name__ == "__main__":
    lst = [1, 7, 3, 4, 0]
    get_products_of_all_ints_except_at_index(lst)
