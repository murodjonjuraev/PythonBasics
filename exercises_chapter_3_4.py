# chapter 3
my_pizzas = ['artichoke', 'margarita', 'cheese', 'pepperoni']
friend_pizzas = my_pizzas[:]
my_pizzas.append("vegiterian")
friend_pizzas.append("mushroom")
print("my favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friend's favorite pizza are:")
for pizza in friend_pizzas:
    print(pizza)

# TUPLES
demensions = (200, 50)
print(demensions[0])
print(demensions[1])
print("Original demensions")
for demension in demensions:
    print(demension)
demensions = (400, 100)
print("\nModified demensions")
for demension in demensions:
    print(demension)

print("*****************************************************************************")
foods = ('shrimp', 'chicken', 'pizza', 'lobster', 'soup')
for food in foods:
    print(food)
print("*****************************************************************************")
foods = ('shrimp', 'chicken', 'pizza', 'manti', 'shurbo')
for food in foods:
    print(food)
