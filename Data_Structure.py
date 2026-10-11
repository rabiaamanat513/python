#--------------List-----------------
my_list = ["Apple" , "Mango" , "Banana" , "Apple"]
print(f"My List: {my_list}")
my_list.append("Orange")
print(f"My List after adding: {my_list}")
print(f"First term: {my_list[0]}")
#-------------Tuple-----------------
my_tuple = ("Red" , "Green" , "Blue" , "Green")
print(f"My Tuple: {my_tuple}")
print(f"Second item: {my_tuple[1]}")
#------------Set-------------------
my_set = {10, 20, 30, 20, 10}
print(f"My set: {my_set}")
my_set.add(40)
print(f"After adding 40: {my_set}")
#------------Dictionary--------------
my_dict = {
    "name" : "Rabia",
    "age" : 20,
    "city" : "Sheikhupura"
}
print(f"My Dictionary: {my_dict}")
print(f"My name: {my_dict['name']}")
my_dict["age"] = 21
print(f"After updating age: {my_dict}")