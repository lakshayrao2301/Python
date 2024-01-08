# if else

# age = int(input("How old are you? "))

# if age < 10:
#     print("You are child")
# elif age >= 18 and age <= 25:
#     print("aspirants")
# elif age > 25:
#     print("adult")
# else:
#     print("not born yet")

# logical operators (and, or, not)
temp = int(input("Enter a Temperature: "))

# and both cond are true
# or only one condition is true

if temp >= 0 and temp <= 30:
    print("The temperature is good")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad")
    print("stay inside!")

# "not" change true into false & false into true

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad")
    print("stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good")
    print("go outside!")

