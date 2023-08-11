# x = 15
# # Prints the type of variable x
# x = '''
# This is a multiline comment
# f
# sd
# fasf
#
# '''
# print(type(x))
# x = "hello"
# print(x)
# x = 3.14
# print(x)

# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
# print("Your name is " + firstName + " " + lastName)
# print(f"Your name is {firstName} {lastName}")
# # print("Your name is {} {}".format(firstName, lastName))
"""
   snake_case -> first_name last_name    Variable, **Function**
   camelCase -> firstName lastName       **Variable**, Function
   PascalCase -> FirstName LastName      Class
   CONSTANT_CASE -> FIRST_NAME LAST_NAME Constant Variables

"""
# birthYear = int(input("Enter your birth year: "))
# print(1402 - birthYear)
# print("Hello!! My name is amir", end="")
# print("\rYour name is reza")
# print("My mom said my: \"Your dinner is prepared\"")
"""
	Escpae Chars:
	\n -> Enter, \t -> Tab, \b -> Backspace, \\ -> Backslash, \r -> Replace Line,
	 \0 -> None, \" -> DoubleQuote, \' -> SingleQuote
"""
# a, b = 13, 14
a = 2
b = 4
# a -= b
# print(a)

"""
	+ -> Sum, - -> Subtraction, * -> Multiplication, / -> Division, % -> Remaining Value, ** -> Power, // -> Radical  
"""

# print(a ** b) # -> 16
# print(b // a) # -> 2

if a > b:
	print("A is larger that B")
elif a == b:
	print("A is equal with B")
else:
	print("A is smaller than B")
# print("A is larger that B") if a > b else print("A is small or equal with B") # Inline

# Truthiness & Falseness
a = list()
b = ["a1", b, 2, "sadfad"]
# ? : -> (a) ? a : "a is unavailable"
print(a if a else "a is unavailable")
print(b if b else "b is unavailable")

