#Program that imitates a small database in the sense that it can: 
#insert new student and their mark
#keep continually add students
#print out student's name and their mark
#average mark of all students
#find the maximum mark among all students

def generate_stds():
  print("Enter the name: ")
  name = input()
  print("Enter the grade: ")
  grade = int(input())
  return name, grade

def all_stds():
  all_students = []
  while True:
    all_students.append(generate_stds())
    print("To stop adding students, type 0")
    x = input()
    if x == '0':
      break
  return all_students


def print_students(lista):
  for std in lista:
    print(f"{std[0]} earned a grade {std[1]}")


def avr_mark(lista):
  total=0
  for std in lista:
    total += std[1]
  return total/len(lista)

listb = all_stds()
print_students(listb)
print(avr_mark(listb)