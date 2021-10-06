# author CJP 10/6/2021
weight = int(input("Enter Weight "))
height = int(input("Enter Height "))
bmi = weight / (height ** 2)

if bmi < 19:
    print("You are underweight")
elif bmi < 25:
    print("You are heathy")
elif bmi < 30:
    print("You are overweight")
elif bmi < 40:
    print("You are obese")
else:
    print("You are extremely obese")
