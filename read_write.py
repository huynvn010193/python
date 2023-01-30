CURRENT_YEAR = 2023

print('Your frist name')
firstname = input()

print('Your last name')
lastname = input()

print('Your name is: ' + firstname + ' ' + lastname)

print('When you was born')
year_born = input()
year_born = int(year_born) #overide

age = CURRENT_YEAR - year_born

print("You are " + str(age) + " years old in " + str(CURRENT_YEAR))
