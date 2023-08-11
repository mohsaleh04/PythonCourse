# def say_hello_world():
# 	print("Hello World!")
#
#
# say_hello_world()

# def say_hello_world2():
# 	print("Hi World")
# 	return "Hello World"
#
#
# print(say_hello_world2())

# def say_hello_world3(text):
# 	return f"Hello {text}"
#
# print(say_hello_world3("My World"))


# def say_hello_world4(text="World"):
# 	return f"Hello {text}"
#
# print(say_hello_world4("My World"))

# def check_hellos(text):
# 	if text == "Hello":
# 		return "Hello World"
# 	elif text == "Hi":
# 		return "Hi World"
# 	else:
# 		return False
#
# result = check_hellos("Hellos")
# print(result) if result else print("No result")
#
# def check_hellos(text1, text2):
# 	checkResult = 0
# 	for char1 in text1:
# 		for char2 in text2:
# 			if char1 > char2:
# 				checkResult = 1
# 				break
# 			elif char1 < char2:
# 				checkResult = -1
# 				break
# 			# else:
# 			# 	checkResult = 0
#
# 	if checkResult == 1:
# 		return f"{text1} is greater than {text2}"
# 	elif checkResult == -1:
# 		return f"{text1} is less than {text2}"
# 	else:
# 		return f"{text1} is equal to {text2}"
#
#
# print(check_hellos("Hello", "Hi"))
# def submit_signup_form(firstName, lastName, age, nationality, gender = "Unknown"):
# 	return {
# 		"firstName": firstName,
# 		"lastName": lastName,
# 		"age": age,
# 		"nationality": nationality,
# 		"gender": gender
# 	}

# form = submit_signup_form("John", "Doe", 25, "USA")
# print(form)

# form = submit_signup_form(age=30, firstName="Daniel", lastName="XYZ", gender="Male", nationality="USA")
# print(form)

# def submit_signup_form2(*form):
# 	return {
# 		"firstName": form[0],
# 		"lastName": form[1],
# 		"age": form[2],
# 		"nationality": form[3],
# 		"gender": form[4]
# 	}
#
#
# form = submit_signup_form2("Saleh", "Masoudi", 19, "IR", "Male")
# print(form)

# def submit_signup_form3(**valForm):
# 	[print(f"{key}: {val}") for key, val in valForm.items()]

# submit_signup_form3(firstName="Saleh", lastName="Masoudi", age=12, nationality="IR", gender="Male")

# myForm = {
# 	"firstName": "Saleh",
# 	"lastName": "Masoudi",
# 	"age": 12,
# 	"nationality": "IR",
# 	"gender": "Male"
# }

# submit_signup_form3(**myForm)

# myFunc = lambda x, y: print(f"Hello {x}"); ...
#
# myFunc(13, 14)

# names = ["Saeed", "Saleh", "Reza", "Sara"]
# filterName = lambda name: name.startswith("S")
#
# filteredNames = filter(filterName, names)
# print(list(filteredNames))
#
# print(list(map(filterName, names)))

# print(list(map(lambda name: f"Hello {name}", names)))

numbers = [1, 10, 4, 6, 8, 2]

# print(all(numbers))
# print(any(numbers))

# print(sorted(numbers, reverse=True))

users = [
	{
		"firstName": "Saleh",
		"lastName": "Masoudi",
		"age": 12,
		"nationality": "IR",
		"gender": "Male"
	},
	{
		"firstName": "Saeed",
		"lastName": "Darabi",
		"age": 19,
		"nationality": "IR",
		"gender": "Male"
	},
	{
		"firstName": "Sara",
		"lastName": "Tehrani",
		"age": 20,
		"nationality": "IR",
		"gender": "Female"
	}
]
#
# sortedUsersByFirstName = sorted(users, key=lambda user: user["age"])
# print(sortedUsersByFirstName)

# print(max(users, key=lambda user: user["age"]))
# print(min(users, key=lambda user: user["age"]))
# print(sum([user["age"] for user in users]) / len(users))
# print(round(3.141592653589793, 2))

# print(abs(-10))

#zipObj = zip([1, 2, 3], [4, 5, 6])
# print(len(list(zipObj)))

# Error , Exception
#
# errorCount = 0
# while True:
# 	if errorCount >= 3:
# 		raise Exception("دیگه بسه!!!")
#
# 	try:
# 		number = int(input("Enter a number: "))
# 		print("Even") if number % 2 == 0 else print("Odd")
# 	except ValueError:
# 		print("Please enter a valid number!")
# 		errorCount += 1
# 		continue
# 	else:
# 		print("Thank you!")
# 		break
# 	finally:
# 		print("Finally")
#
#


