had_water = False
had_food = True

if had_water:
    print("I am hydrated!")
elif had_food:
    print("I am full!")
else :
    print("I need to drink water.")    

# switch case statement
number = int(input("Enter a number: "))
name = input("Enter your name:").upper()

match number:
    case 10:
        print(f"{name} got 10")
    case 20:
        print(f"{name} got 20")
    case 0:
        print(f"{name} is failed")
    case _:
        print("Invalid number")

# Ternary operator
age = int(input("Enter your age:"))

is_adult = True if age>=18 else False
print(is_adult)
