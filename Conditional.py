marks = int(input("Enter your marks:"))
#----------------if condition---------------
if marks > 90:
    print("Excellent")
#--------------if-else condition-------------
if marks >= 33:
    print("You are pass")
else:
    print("You are fail")
#--------------if-elif-------------------
if marks >= 80:
    print("Grade = A+")
elif marks >= 60:
    print("Grade = B")
elif marks >= 33:
    print("Grade = C")
else:
    print("Grade = F")
#--------------Nested-if------------------
if marks >= 33:
    print("You are pass")
    if marks >= 80:
        print("You are topper")
    else:
        print("Keep improving")
else:
    print("Work hard")