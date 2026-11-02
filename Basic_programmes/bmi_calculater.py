weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {round(bmi, 2)}")