weights_kg = [145, 100, 76, 80]
weights_pds = []

counter = 0

while counter < 4:
    pound = weights_kg[counter] * 2.2
    rounded_pound = round(pound, 3)
    weights_pds.append(rounded_pound)
    counter += 1
else:
    print(weights_pds)


# break
# continue
# pass 