def times_n(number, numbers_list):
    return [item * number for item in numbers_list]

def remove_all_comprehension(item_to_remove, my_list):
    return [item for item in my_list if item != item_to_remove]