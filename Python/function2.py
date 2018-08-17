def royal(name, city):
    return(" The Honorable " + name+ " of " +city)
name = input("What is thou name?\n")
city = 'Dublin'
royal_greet = royal(name, city)
print("Behold" + royal_greet + "!")