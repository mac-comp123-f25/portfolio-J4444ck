def print_every_other(x):
  while x >= 0:  # x is the loop variable
    print(x)
    x = x - 5
  # when indentation stops, while loop is over
  print("Done!")

print_every_other(20)
print_every_other(11)

# Initialize loop variable
user_inp = input("Enter the next number (negative to quit): ")
user_num = int(user_inp)
while user_num >= 0:
    print(user_num, "squared is", user_num ** 2)
    user_inp = input("Enter the next number (negative to quit): ")
    user_num = int(user_inp)
