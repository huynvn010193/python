CURRENT_YEAR = 2023
METER_TO_FEET = 3.281

firstname = input('Your frist name: ')
lastname = input('Your last name: ')
year_born = input('When you was born: ')
height_meter = input('Your height (meter): ')

year_born = int(year_born) #overide
age = CURRENT_YEAR - year_born

height_meter = float(height_meter)
height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet, 1)

print('\n-----')
print('Your name is: ' + firstname + ' ' + lastname)
print("{2} is {0} years old in {1}".format(age,CURRENT_YEAR, firstname))
print("You are " + str(height_feet) + " feet tall")

gender_input = input("Are you male (yes/no): ")
is_name = None

if (gender_input == "yes") or (gender_input == "y") or (gender_input == "Yes"):
  is_male = True
elif gender_input == "no" or (gender_input == "n") or (gender_input == "No"):
  is_male = False
else:
  is_male = None

if is_male is None:
  print("Invalid Answer")
elif is_male == True:
  if height_feet > 6.5:
    print("You are very tall as a man")
  elif height_feet > 6.0:
    print("You are tall as a man")
  else:
    print("You are short as a man")
elif is_male == False:
  if height_feet > 5.7:
    print("You are tall as a girl")
  else:
    print("You are short as a girl")
else:
  print("system error, variable 'is_male' is not conrrect")