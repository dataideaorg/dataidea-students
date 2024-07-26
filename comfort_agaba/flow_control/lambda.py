def calculateBMI(weight, height):
    bmi = weight / (height * height)
    rounded_bmi = round(bmi, 1)
    return rounded_bmi

calculated_bmi = calculateBMI(80, 1.75)
print(calculated_bmi)