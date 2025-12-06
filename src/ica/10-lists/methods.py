def end_points(numbers_list):
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    return (min_value, max_value)


my_list = [5, 2, 8, 1, 9, 4]

my_tuple = end_points(my_list)
print(f"The tuple returned is: {my_tuple}")


minimum_value, maximum_value = end_points(my_list)
print(f"The minimum value is: {minimum_value}")
print(f"The maximum value is: {maximum_value}")