#Code for a random band name generator
print("Welcome to the Band Name Generator.")
#asks for city name
city: str = input("What's the name of the city you grew up in?\n").strip().title()
#asks for pet 
pet_name: str = input("What's your pet's name?\n").strip().title()
print()
print(f"Your band name could be {city} {pet_name}")