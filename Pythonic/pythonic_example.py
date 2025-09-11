my_list = ['A', 'B', 'C']
for item in my_list:
    print(item)

for num, item in enumerate(my_list):
    print(f"{num}:{item}")



# non Pythonic
result = []
for item in my_list:
    if item not in result:
        result.append(item)
 
# Pythonic
result = list(set(my_list))