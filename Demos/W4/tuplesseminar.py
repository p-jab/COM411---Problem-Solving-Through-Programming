def simple_tuples():
  person = ("Piotr", 67, True)

  print(person)

  #Access elements via index - just as you do with lists
  print(person[1])
  if person[2]:
    print("Yay - you have a doggo!")
  else:
    print("No doggo no fun!")

  print("Which item to print?")
  n = int(input())
  if n < len(person): 
    print(person[n-1])

  #You cannot modify (mutate) a tuple!
  #person[0] = "Peter"
  #print(person)

  tuple2 = person + (2000, "black")
  print(tuple2)
  print(person)
  print(tuple2)

def student():
  print("Enter your name:")
  name = input()
  print("What is your age?")
  age = int(input())
  print("Do you have a dog?")
  dog = input()
  if dog == "yes":
    dog_bool = True
  else:
    dog_bool = False
  return name,age,dog_bool
  
print("How many students to generate?")
n = int(input()) #Inputs 5
count = 1 #Keep  track how many repetitions we have done
all_students = []
while(count <= n):
  tuplex = student()
  all_students.append(tuplex)
  count+=1
print(all_students)