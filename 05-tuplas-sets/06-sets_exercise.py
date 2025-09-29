
python_course = {'Ana', 'Luis', 'Pedro', 'Maria'}
java_course = {'Pepito', 'Pedro', 'Carlos', 'Ricardo'}

two_course = python_course.intersection(java_course)
print(two_course)

only_python = python_course.difference(java_course)
print(only_python)

all_students = python_course.union(java_course)
print(all_students)