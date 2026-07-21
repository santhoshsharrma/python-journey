# AN example to provide a senior discount using nested if else
age = input("Please enter your age: ")
age_renew = int(age)
member_check = input("Are you a member of our store? (yes/no)").lower()

if age_renew>=60:
    if member_check == "yes":
        print("50% off")
    else:
        print("30% off")
else:
    print("You're not eligible for senior off")