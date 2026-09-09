name = input("What is yor name? ")
age = int(input("Hpw old are you? "))
hight = float(input("How tall are you? "))
weight = float(input("How much do you weight? "))

bmi = (weight / (pow(hight, 2)))

print(f"Mr/Mrs {name}, {age} ywars old, hight {hight}, wight {weight}, your body mass index is {bmi:.2f}")