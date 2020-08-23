for i in range(3):
    num = int(input("enter your number"))
    if num % 3 == 0 and num % 5 == 0:
        print("Fuzz-Buzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fuzz")