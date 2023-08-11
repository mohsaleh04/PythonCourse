users = list()

def get_users():
	return users

def add_user(**user):
	users.append(user)

def remove_user(**user):
	users.remove(user)

def update_user(**user):
	users.remove(user)
	users.append(user)

def print_users():
	[print(user) for user in users]

