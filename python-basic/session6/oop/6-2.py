class University:
	id: int
	name: str
	address: str
	students: list()
	teachers: list()
	totalScore: float

	def __init__(self, name, address):
		self.name = name
		self.address = address
		self.students = list()
		self.teachers = list()
		self.totalScore = 0

	def add_student(self, student):
		self.students.append(student)
		self.totalScore += student.score

	def add_teacher(self, teacher):
		self.teachers.append(teacher)

	def show(self):
		print(f"Total Score: {self.totalScore}")
		print(f"Students: {len(self.students)}")
		print(f"Teachers: {len(self.teachers)}")
		[print(student.name) for student in self.students]
		[print(teacher.name) for teacher in self.teachers]

class Teacher:
	id: int
	name: str
	age: int
	university: University
	students: list()
	classes: list()

	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.students = list()
		self.classes = list()

	def add_student(self, student):
		self.students.append(student)

	def add_class(self, class_):
		self.classes.append(class_)

class Student:
	id: int
	name: str
	age: int
	university: University
	teacher: Teacher
	score: float

	def __init__(self, name, age, score, uni, teacher):
		self.name = name
		self.age = age
		self.score = score
		self.university = uni
		self.teacher = teacher

	def show(self):
		print(f"Name: {self.name}")
		print(f"Age: {self.age}")
		print(f"Score: {self.score}")
		print(f"University: {self.university.name}")
		print(f"Teacher: {self.teacher.name}")

	def get_score(self):
		return self.score

idSalej = {
	"name": 'Saleh',
	"age": 4,
	"code": 2345345345345
}
idSalejEdited = {

}

idSalejKeys = list(idSalej.keys())
idSalejKeys.sort()
# [print(f"{key}: {idSalej[key]}") for key in idSalejKeys]
for key in idSalejKeys:
	idSalejEdited[key] = idSalej[key]

print(idSalejEdited)