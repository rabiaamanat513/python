#--------------for loop----------------
for i in range(1 , 6):
    print(f"Number: {i}")
#-------------While loop---------------
num = 1
while num <= 5:
    print(f"Count: {num}")
    num = num + 1 
#------------Break+Continue-------------
for i in range(1 , 11):
    if i == 3:
        continue
    if i == 8:
        break
    print(f"value: {i}")
#------------Else with loop-------------
for i in range(1 ,4):
    if i == 2:
        print("Breaking loop at i = 2")
        break
    print(f"i = {i}")
else:
        print("Loop was broken")

