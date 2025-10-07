#weight convert

weight = float(input("enter your weight: "))
unit = str(input("kilograms or pounds? (k or l): "))

if unit == "kilograms"or "kg":
    weight = weight * 0.453592
    print("your weight is ",{weight})
    print("thanks ")
elif unit == "pounds"or "p":
    weight = weight / 2.220
    print("your weight is ",{weight})
    print("thanks ")
else:
    print(f"invalid unit")
    print("thanks ")
