def getmefruits():
  fruits = []
  print("How many fruits would you like to enter?")
  n = int(input())
  for i in range(n):
    print("Type in the next fruit:")
    fruits.append(input())
  return fruits

def get_fruits():
  fruits = ["apple", "kiwi", "banana", "mango", "pineapple", "pear"]
  fruits2 = getmefruits()
  #Print all items
  print("Your fruits are {}".format(fruits[1]))

  #Print only few items by Slicing
  print(f"Sliced list: {fruits[0:5]}")

  #Print only few items by using negative index
  print(f"Negative index: {fruits[-2:0:-1]}")

  fruits2.append("pear")

  print("The second list is {}".format(fruits2))

get_fruits()