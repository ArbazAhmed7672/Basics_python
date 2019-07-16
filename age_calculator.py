#age_calculator_and_voter_predictor

ww = int(input("your date of birth:> "))
if ww in range(0, 5000):
    print(ww, "-birth year")
    if ww <= 2019:
        age = 2019 - int(ww)
    else:
        age = 0.1
    if age == 1:
        yr = "year"
        print("you have completed your", age, yr)
    elif age == 0:
        print("you are just months older or you have not born yet")
    elif age == 0.1:
        print("you have not born yet")
    else:
        yr = "year's"
        print("you have completed your", age, yr)

    if age > 18:
        print('''you have the right to vote''')
    elif age == 18:
        print("you are the voter for the next year")
    elif age == 0:
        print("you failed to provide your correct birth-date")
    elif age == 0.1:
        print("you failed to provide your correct birth-date")
    else:
        print("But you are under 18 year's")
else:
    print(f"you entered string(letters).")
