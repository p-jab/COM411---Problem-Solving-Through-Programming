phonebook = {}

while True:
  name = input("Enter the name: ")
  number = input("Enter the number: ")
  phonebook[name] = number
  if input("Type 'x' to stop") == 'x':
    break


def calling(n, book = {}):
  print(f"Calling {n} with a phone number {book[n]}")

phonebook["Tadek"] = "35263562536"

calling("Piotr", phonebook)