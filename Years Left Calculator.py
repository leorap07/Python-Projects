# Years Left Calculator
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days_in_year = 365
weeks_in_year = 52
months_in_year = 12
years_left = 90 - int(age)
x = days_in_year * years_left
y = weeks_in_year * years_left
z = months_in_year * years_left

print(f"You have {x} days, {y} weeks, and {z} months left.")