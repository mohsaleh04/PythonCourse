# Generator
#
# def counter():
# 	i = 1
# 	while i <= 10:
# 		yield i
# 		print(i)
# 		i += 1
#
#
# for j in counter():
# 	print(j)

# Decorator
#
# def say_hello(func):
# 	def wrapper(*args):
# 		print("Hello")
# 		func(*args)
# 		print("Bye")
# 	return wrapper
#
# @say_hello
# def insert_name(name, age, gender):
# 	print(f"{name}")
#
# insert_name("John")
#
# def multiply_by_2(func):
# 	def wrapper(*args):
# 		return func(*args) * 2
# 	return wrapper
#
# @multiply_by_2
# def sum(a, b):
# 	return a + b
#
# def divide(a, b):
# 	return a / b
#
#
# #use_math(2, 3, "**")
# print(divide(4, 3))
