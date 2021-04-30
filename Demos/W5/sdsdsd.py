def observed():
  observations = []
  for i in range(7):
    observations.append(input())
  return observations

def run():
  print("Counting observations...")
  list_of_observations = observed()
  set_of_observations = set()
  for i in range (len(list_of_observations)):
    set_of_observations.add(list_of_observations[i])
  set_of_tuples = set()
  for item in set_of_observations:
    count = 0
    for i in range (len(list_of_observations)):
      if list_of_observations[i] == item:
        count +=1
    set_of_tuples.add((item, count))
  print(set_of_tuples)


run()


# Extra session 5pm-6pm