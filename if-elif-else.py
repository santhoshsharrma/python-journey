# if elif else conditions

age = input("What is your age?: ")
ask= input("Are you single or married?: ").lower()
age_tc = int(age)
if age_tc <= 20: print("Teen")
elif age_tc > 21 and ask.lower() == "single":
    print("Single Adult")
else:
    print("Married Adult")
    
# The below is the same example i initially tried and made few mistakes that i fixed on the above code.
""" 
age = input("What is your age?")
ask = input("What is your status?: (single/married)")
age_integer = int(age)
if age_integer <= 20:
    print("Teen")
if ask.lower() == "single":
      print("Single Adult")
else:
    print("Married Adult")
    """
