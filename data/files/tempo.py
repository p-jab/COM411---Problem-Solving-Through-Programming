def search(file_name):
  print("Searching...")
  data = {}
  with open(file_name) as file:
    section_name = ""
    for line in file:
      if line.startswith("Section"):
        section_name = line.split(":")[1]
      elif (section_name in data):
        data[section_name].append(line.strip())
      else:
        data[section_name] = [line.strip()]
  print("Done!")
  return data

def run():
  data = search("data/files/txt/books.txt")
  
  with open ("data/files/txt/generated.csv", "w") as f:
    for key, val in data.items():
      for item in val:
        f.write(f"{key},{val[0]}\n")


run()