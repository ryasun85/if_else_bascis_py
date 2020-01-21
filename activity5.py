age = 10

if  age <= 17: 
    print("You aren't old enough.")
else :
    print("Yes, I can serve you.")

age = 66
country = "UK"
if  age <=21 and country == "UK":
    print("You aren't old enough to purchase this.")
elif age > 65:
    print("should you be drinking?")
else :
    print("Yes, I can serve you as you are over 21.")

#COME BACK TO THIS:
age = 25
country ="UK"
if age > 25 and country.upper() == "UK":
    print("cool")
elif age > 17 and country.upper() == "UK":
    print("can I have your ID?")
else:
    print ("too young")