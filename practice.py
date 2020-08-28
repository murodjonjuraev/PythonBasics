# def greet_user():
#     """display simple greeting"""
#     print("Hello!")
#
# greet_user()
#
# def greet_user(username):
#     """display a simple greeting"""
#     print(f"Hello {username.title()}!")
#
# greet_user("murod")
#
# def display_message():
#     """Display sample message"""
#     print("I am learning functions in this chapter")
#
# display_message()
#
# def favorite_book(bookname):
#     print(f"{bookname.title()}this is one of my favorite books")
#
# favorite_book("allice in wonderland")
#
# def describe_pet(animal_type, pet_name):
#     """Display info about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
#
# describe_pet("hamster", "harry")
# describe_pet("deg", "whillie")
# describe_pet("cat", "brown")
# describe_pet(pet_name="vasya", animal_type="kuchuk")
#
# def describe_pet(pet_name, animal_type='dog'):
#     """Display info about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
#
# describe_pet(pet_name="abdu")
# describe_pet("willie")
#
# def describe_pet(pet_name, animal_type='dog'):
#     """ A dog named Willie."""
# describe_pet("willie")
# describe_pet(pet_name="willie")
# """hampser named harry"""
# describe_pet("harry", "hamster")
# describe_pet(pet_name="harry", animal_type="hamster")
# describe_pet(animal_type="hamster", pet_name="harry")
# """all this calls would work equaly"""
#
# def make_shirt(shirt_size="large", shirt_text="I love Python"):
#     print(f"This shirt is {shirt_size} size and text on shirt is {shirt_text}")
#
# make_shirt()
# make_shirt(shirt_size="medium")
#
# def describe_city(city, country="tajikistan"):
#     print(f"\n{city.title()} is in {country.title()}.")
#
# describe_city("khujand")
# describe_city("dushanbe")
# describe_city("New York", "USA")
#
# def get_formatted_name(first_name, last_name):
#     """return a full name, neatly formated"""
#     full_name = first_name + " " + last_name
#     return full_name.title()
#
# musician = get_formatted_name("jimi", "hendrix")
# print(musician)
#
# def get_formatted_name(firs_name, middle_name, last_name):
#     """return full name neatly formated"""
#     full_name = firs_name+ " " + middle_name+ " " + last_name
#     return full_name
#
# musician = get_formatted_name("john", "lee", "hooker")
# print(musician)
#
# def get_formatted_name(first_name, last_name, middle_name=""):
#     if middle_name:
#         full_name = first_name+" "+middle_name+" "+last_name
#     else:
#         full_name = first_name + " " + last_name
#     return full_name.title()
# musician = get_formatted_name("jimi", "hendrix")
# print(musician)
#
# musician = get_formatted_name("john", "hooker", "lee", )
# print(musician)
#
# def builf_person(first_name, last_name):
#     """return dictionary of information about a person"""
#     person = {"first": first_name, "last": last_name}
#     return person
# musician = builf_person("jimi", "hendrix")
# print(musician)
#
# def build_person(first_name, last_name, age=""):
#     person = {"first": first_name, "last": last_name}
#     if age:
#         person["age"] = age
#     return person
#
# musician = build_person("jimi", "hendrix", age = 27, )
# print(musician)
#
# def get_formatted_name(first_name, last_name):
#     """return a full name, neatly formated"""
#     full_name = first_name + " " + last_name
#     return full_name.title()
#
# while True:
#     print("\nPlease tell me your name")
#     f_name = input("First name")
#     l_name = input("last name")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# def get_formatted_name(first_name, last_name):
#     """return a full name, neatly formated"""
#     full_name = first_name + " " + last_name
#     return full_name.title()
#
# while True:
#     print("\nPlease tell me your name")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name")
#     if f_name == 'q':
#         break
#
#     l_name = input("last name")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

