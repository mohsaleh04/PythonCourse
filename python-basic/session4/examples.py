# Question 1:
# Given a list of words,
# write a program to count the number of words that start with a vowel and have an odd length.

# Example:
# For the list ['apple', 'banana', 'orange', 'pear', 'grape'], the program should output 1.
#
# items = input("Enter your items: ").split()
# count = 0
# for item in items:
# 	if item[0].casefold() in 'aeiou' and len(item) % 2 == 1:
# 		count += 1
#
# print(count)


# Question 2:
# Write a Python program that takes a string as input and prints a list containing all the words from the string that have more than 4 characters and ends with the letter 's'.


# Example:
# For the input string "The cats are playing in the gardens", the program should return the list ['cats', 'gardens'].

# inputStr = input("Enter your string: ").split()
# output = []
#
# for word in inputStr:
# 	if len(word) >= 4 and word[-1] == 's':
# 		output.append(word)
#
# print(output)


## Inline

# inputStr = input("Enter your string: ").split()
# output = []
#
# # for word in inputStr:
# # 	if len(word) >= 4 and word[-1] == 's':
# # 		output.append(word)
# [output.append(word) for word in inputStr if len(word) >= 4 and word[-1] == 's']
#
# print(output)

# Question:
# Write a Python program that takes a list of numbers as input and returns a new list containing only the odd numbers greater than 10.

# Example:
# For the input list [5, 8, 12, 15, 20, 25, 30], the program should return the list [15, 25].
#
# numbers = set(input("Enter your numbers: ").split())
# output = []
#
# for number in numbers:
# 	if int(number) > 10 and int(number) % 2 != 0:
# 		output.append(int(number))
#
# print(output)


# Question:
# Write a Python program that takes two sets A and B as input and returns a new set containing the elements that are present in set A but not in set B.

# Example:
# For set A {1, 2, 3, 4} and set B {3, 4, 5, 6}, the program should return the set {1, 2}.

# A = set(input("Enter your set A: ").split())
# B = set(input("Enter your set B: ").split())

# print(A.difference(B))

# print(A - B) -> difference
# print(A & B) -> intersection
# print(A | B)  # -> union
# print(A ^ B)  # -> symmetric difference
