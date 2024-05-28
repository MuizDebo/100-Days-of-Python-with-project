# Welcome Message
print("Welcome!\nLeap year or not? Check it out!\n")

# Which year do you want to check?
year = int(input("Which year do you want to check? "))

# contact me @ muiz.debo@gmail.com to learn an easier way of writing this ;)
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not a leap year")
  else:
    print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")
