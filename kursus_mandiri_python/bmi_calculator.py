height = input("Height: ")
weight = input("Weight: ")

weight_as_int = int(weight)
height_as_float = float(height)

# using the exponent operator
bmi = weight_as_int / height_as_float ** 2
print(bmi)

# using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi)