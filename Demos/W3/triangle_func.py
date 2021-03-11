#Defining my own function to calculate area of a triangle
def calculate_area(h = 10,b = 5):
  area = 0.5*h*b
  return area

def run():
  x = calculate_area(4)
  x += 1
  print(f"The area of triangle is {x}")

#Call for the function
run()



# calculate_area(5)
# calculate_area(b=20)
# calculate_area(13,7)





#Paremeter - a value that you plug into a function