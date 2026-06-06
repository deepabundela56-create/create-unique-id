nos=int(input("Enter the number of students"))
for i in range(nos):
        fname=input("enter the first name:")
        lname=input("enter the last name:")
        dob=input("enter the date of birth (dd-mm-yyyy):")
        mob=input("enter the mobile number:")
        uid=fname[:2]+lname[-2:]+dob[-2:]+mob[-4:]
        print("user ID generated", uid)
