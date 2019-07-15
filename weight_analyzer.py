name = "any one"
print("weight is")
weight_kg = int(input())
print("height is")
height_m = float(input())
bmi = weight_kg/ (height_m ** 2)

print("bmi: ",bmi)
if bmi < 25:
    print("not overweight")

elif bmi == 25:
    print("you are at the border of overweight")

else:
    print("you are over weight")
