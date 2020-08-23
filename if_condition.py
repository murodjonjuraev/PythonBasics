# cars = ['lexus', 'bugatti', 'bmw', 'ferrari']
# if 'bmw5' not in cars:
#     cars.append('bmw5')
# print(cars)
#
# for car in cars:
#     if 'bmwx5' != car:
#         cars.append('bmwx5')
#     else:
#         print(car + "in not bmwx5")
# print(cars)

# Multiple conditions
cars = ['lexus', 'bugatti', 'bmw', 'ferrari']
states_17 = ['NY', 'CA', 'NC', 'VA', 'CT']
states_16 = ['NJ', 'WA', 'MA', 'TX', 'VT']
for i in range(3):
    age = int(input("Enter your age:"))
    state = input("enter your state:").upper()
    if age >= 16 and state in states_16:
        print("your are eligible to apply for DL")
        print("available cars in your state:")
        for car in cars[2:]:
            print(f"\t{car}")

    elif age >= 17 and state in states_17:
        print("your are eligible to apply for DL")
        print("available cars in your state:")
        for car in cars[2:]:
            print(f"\t{car}")
    else:
        # diff = 17 - age
        print(f"you are not eligible to apply")