
#  Dictionary in python


# Diclearing a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
    }

print(f"Person dictionary: {person}")

# Accessing values in a dictionary

print("Name : ", person["name"])
print("Age : ", person["age"])
print("City : ", person["city"])
print("Occupation : ", person["occupation"])

# Modifying values in a dictionary

person["Phone"] = "123-456-7890"
print("Phone : ", person["Phone"])

person["Email"] = "john30@gmail.com"
print("Email : ", person["Email"])

# Removing values from a dictionary

del person["age"]
print(f"Person dictionary after removing age: {person}")