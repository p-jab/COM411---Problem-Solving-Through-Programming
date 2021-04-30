def actors():
  real = input("Name:")
  role = input("Role:")
  return real,role

def rate_a_movie(title):
  return float(input(f"What would you rate \"{title}\"?\n"))

def new_movie(t):
  #Function to create a movie page
  movie = {}
  movie["Title"] = t
  #movie["Released"] = input("What year was it released?\n")
  movie["Genre"] = input("What genre it is?\n")
  #movie["Duration"] = input("How long is this movie?\n")
  actor_list = []
  i = 0
  print("Provide details of the cast. How many actors are in the cast?")
  n=int(input())
  while i < n:
    actor_list.append(actors())
    i+=1
  movie["Actors"] = actor_list
  movie["Rating"] = 5.0, 0
  return movie

def movie_search(database = {}):
  print("Search by: Title, Genre or Actor?")
  opt = input()
  movie = {}
  if opt.lower() == "title":
    t = input("Enter the title: ")
    if t in database:
      movie = database[t]
    else:
      print("The database contains no info about this movie :(")
  elif opt.lower() == "genre":
    g = input("Enter the genre: ")
    for details in database.values():
      if details["Genre"] == g:
        movie = details
  elif opt.lower() == "actor":
    a = input("Enter actor's name: ")
    for details in database.values():
      for actor in details["Actors"]:
        if actor[0] == a:
          movie = details
  return movie


def max_rated(database = {}):
  max_rating = 0
  movie = {}
  for details in database.values():
    if details["Rating"][0] > max_rating:
      max_rating = details["Rating"][0]
      movie = details
  return movie

def movie_print(movie = {}):
  print("*"*10 + " "*2 + "{}".format(movie["Title"]) + " "*2 + "*"*10)
  for item in movie.items():
    print(f"{item[0]} ------------> {item[1]}")

def imdb():
  imdb = {}
  print("Welcome to the best movie database!\n\n")
  while True:
    print("Chose an item from the menu:\n1-Add a movie\n2-Search for a movie\n3-Display all movies\n4-Get a top rated movie\n5-Rate a movie\n9-Exit")
    option = int(input())
    if option == 1:
      m_title = input("What is the title of the movie?")
      imdb[m_title] = new_movie(m_title)
    elif option == 2:
      print("Suitable movie:\n ")
      movie_print(movie_search(imdb))
    elif option == 3:
      print(imdb)
    elif option == 4:
      print("You chose to find out the highest rated movie\nThis is the one:\n")
      print(max_rated(imdb))
    elif option == 5:
      print("You are rating a movie. Please be gentle")
      m = movie_search(imdb)
      current_rating = m["Rating"][0]
      number_ratings = m["Rating"][1]
      x = rate_a_movie(m["Title"])
      new_rating = (number_ratings*current_rating + x)/(number_ratings+1)
      m["Rating"] = new_rating,number_ratings+1
      imdb[m["Title"]] = m
    elif option == 9:
      break
    else:
      print("Invalid option. Try Again. You noob.\n")
  return imdb

imdb()