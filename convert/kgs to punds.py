#weight convert

weight = float(input("enter your weight: "))
unit = str(input("kilograms or pounds? (k or l): "))

if unit == "kilograms":
    weight = weight * 0.453592
    print("your weight is ",{weight})
elif unit == "pounds":
    weight = weight / 2.220
    print("your weight is ",{weight})
else:
    print(f"invalid unit")
