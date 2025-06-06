import random
#list comprehension
numbers = [1, 2, 3, 4, 5]
new_numbers = [n**2 for n in numbers]
print(new_numbers)
name = "zeal"
name_list = [letter for letter in name]
print(name_list)

list_l = [n*2 for n in range(1,5)]
print(list_l)
possible_names = [
    "Alice", "Bob", "Charlie", "Diana", "Eve",
    "Frank", "Grace", "Hannah", "Isaac", "Julia",
    "Kevin", "Liam", "Mona", "Nina", "Oscar",
    "Paul", "Quinn", "Rita", "Sam", "Tina"
]

short_names = [name for name in possible_names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in possible_names if len(name) > 5]
print(long_names)

#Dictionary comprehension

student_score = {student:random.randint(1,101) for student in short_names}
print(student_score)

print(student_score.items())# returns a list of tuples 

passed_students = {student:score for (student, score) in student_score.items() if score > 60}
print(passed_students)