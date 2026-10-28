# List comprehension

list_sqre = []

for value in range(0,10):
    list_sqre.append(value**2)

print(f"Square numbers are : {list_sqre}")

list_sq = [value ** 2 for value in range(0,10)]
print(f"Square numbers are : {list_sq}")