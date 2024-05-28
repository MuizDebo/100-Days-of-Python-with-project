# 1st input: enter height in meters e.g: 1.65
height = float(input("Please, enetr your height(m): "))

# 2nd input: enter weight in kilograms e.g: 72
weight = int(input("Please, enetr your weight(g): "))


bmi = weight/(height*height)
print(round(bmi))
