def calculateBMI(weight, height):
    bmi = weight / (height * height)
    rounded_bmi = round(bmi, 1)
    return rounded_bmi

calculated_bmi = calculateBMI(80, 1.75)

if calculated_bmi > 24:
    print("Overweight")
else:
    print("Not overweight")

# calculateBMI(100, 1.85)
# calculateBMI(50, 1.60)

