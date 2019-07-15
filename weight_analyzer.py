name = input("please provide your name:> ")
weight_kg = int(input("weight is"))
height_m = float(input("height is"))
bmi = weight_kg/ (height_m ** 2)
print("bmi: ",bmi)
if bmi < 25:
    print(name + ", you are not overweight")

elif bmi == 25:
    print(name +", you are at the border of overweight")

else:
    print(name +", you are over weight")
