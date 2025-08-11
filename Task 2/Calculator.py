a,b = 0,0

def num():
    a = int(input("Enter First no. : "))
    b = int(input("Enter Second no. : "))

def menu():
    print("\n")
    print("\n--------- SIMPLE CALCULATOR -----------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Division")
    print("5. Remainder")
    print("6. Sqaure")
    print("7. Cube")

def add():
    print(a+b)


while True :
    menu()
    choice = int(input("Choose a option : "))
    if choice == 1:
        num()
        print(a+b)