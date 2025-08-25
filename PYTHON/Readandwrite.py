with open("employees.txt, 'r') as file:
     data = file.read()
print(data)

with open("employees.txt", "w") as file:
  file.write("Welcome to the company!")
print(data)

with open("new_employees.txt, 'w') as outfile:
            outfile.write(data)
try:
  with open("employees_new","r") as file:
    data = file.read()
except FileNotFoundError:
    print("File not found.please check filename.")

