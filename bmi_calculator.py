name = input("What is your name? ")
weight = float(input("What is your weight? (Kg) "))
height = float(input("What is your height? (m) "))

bmi = weight / (height ** 2)

print(f"{name}, Your BMI is {bmi}")