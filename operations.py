#-----------Arithmetic operators-----------
a = 14
b = 7
print(f"a={a}, b={b}")
print(f"a+b = {a+b}")
print(f"a-b = {a-b}")
print(f"a*b = {a*b}")
print(f"a/b = {a/b}")
print(f"a%b = {a%b}")
#------------Assignment operator------------
x = 5
print(f"x= {x}")
x += 4
print(f"After x +=4, x = {x}")
#-----------Comparison oprrator---------------
print(f"Is a equal to b? a==b = {a==b}")
print(f"Is a not equal to b? a!=b = {a!=b}")
print(f"Is a greater than b? a>b = {a>b}")
print(f"Is a less than b? a<b = {a<b}")
#-----------Logical operators----------------
age = 20
has_id_card = True
print(f"age = {age}, has_id_card ={has_id_card}")
can_vote = (age>=18) and (has_id_card)
print(f"can vote? = {can_vote}")
marks = 49
has_grace_marks = True
is_pass = marks>=50 or has_grace_marks
print(f"is_pass = {is_pass}")
print(f"Not has id_card = {not has_id_card}")
#------------Conditional operator---------------
marks = 65
result = "Pass" if marks >= 33 else "Fail"
print(f"marks = {marks}, Result = {result}")