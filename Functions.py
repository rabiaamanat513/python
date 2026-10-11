#----------------Global variable-----------------
city = "SKP"
#----------------Declaring function---------------
def greet_student(name, marks):
#----------------Local Varaible------------------
    message = f"Hello {name}!"
    print(message)
    print(f"Your city is {city}")
    print(f"Your marks are {marks}")
    if marks >= 33:
        result = "Pass"
        print(f"result: {result}")
    else:
        result = "fail"
        print(f"result: {result}")
def add_numbers(a,b):
    total = a + b
    return total
#--------------Calling function--------------------
greet_student("Rabia" , 85)
my_total = add_numbers(10, 20)
print(f"Total is: {my_total}")
#--------------gloabal varaible scope--------------
print(f"city: {city}")
  