def sum3(input_list):

    if len(input_list) < 3:
        raise ValueError("Input list must contain at least three values.")


    for i in range(3):
        if not isinstance(input_list[i], (int, float)):
            raise TypeError("The first three elements of the list must be numbers.")


    first_three_elements = input_list[:3]

    return sum(first_three_elements)

if __name__ == "__main__":
  print( sum3([5, 2, 8, -2, 6, 15]) )
  print( sum3([5, 2]) )
  print( sum3(5) )
  print( sum3(["h", "i", 1, 2, 3]) )
  print( sum3([1, 2, 3, "h", "i"]) )
