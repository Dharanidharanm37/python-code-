salary=int(input("Enter your salary:"))
age=int(input("Enter your age:"))
if(salary>=20000 or age<=25):
    loan=input("enter loan amount:")
    if(loan<="50000"):
        print("you are eligible")
    else:
        print("maximum loan amount is 50K")
