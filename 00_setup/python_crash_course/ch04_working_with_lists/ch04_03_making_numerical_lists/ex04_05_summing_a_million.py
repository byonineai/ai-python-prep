# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million . Also, use the sum() function to see how quickly Python can add a million numbers .

# numbers = list(range(1,1_000_001))
# print("Min:", min(numbers))   # should be 1
# print("Max:", max(numbers))   # should be 1_000_000
# print("Sum:", sum(numbers))   # should be 500000500000

#More efficient - doesn't store 1 million numbers in memory
nums = range(1, 1_000_001)
print(min(nums), max(nums), sum(nums))