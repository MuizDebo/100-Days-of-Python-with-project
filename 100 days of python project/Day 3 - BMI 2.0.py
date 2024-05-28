# Enter your height in meters e.g., 1.55
height = float(input("Please, enter your height(m) e.g., 1.25: "))

# Enter your weight in kilograms e.g., 72
weight = int(input("Please, enter your weight(kg) e.g. 70: "))

bmi = weight/(height*height)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
  print(f"Your BMI is {bmi}, you are clinically obese.")


