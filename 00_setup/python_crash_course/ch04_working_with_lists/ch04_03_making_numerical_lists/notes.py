# #Making numerica lists

# # for value in range(1,5):
# #   print(value)

# #Transform range directly into lists

# # numbers = list(range(1,6))
# # print(numbers)

# # print(numbers[0])

# # squares = []
# # for value in range(1,11):
# #   square = value**2
# #   squares.append(square)

# # print(squares)

# #More concise
# squares = []
# for value in range(1,11):
#   squares.append(value**2)
# print(squares)

# #Simple Statistics

# digits = list(range(0,10))
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# #List comprehensions

#combines the loop and the creation of new elements in one line

squares = [value ** 2 for value in range(1,11)]
print(squares)