print("Thank you for choosing Python Pizza Deliveries!")

size = input("What pizza size do you want?: type 'S' for small, 'M' for medium and 'L' for large\n") # What size pizza do you want? S, M, or L

# Do you want pepperoni? Y or N
add_pepperoni = input("Do you want pepperoni? 'Y' for yes or 'N' for no\n")

# Do you want extra cheese? Y or N
extra_cheese = input("Do you want extra cheese? 'Y' for yes or 'N' for no\n")


bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
