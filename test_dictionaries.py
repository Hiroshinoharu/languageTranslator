# method to add elements in dictionary
Dict = {}
print("\nEmpty Dictionary: ")
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 'Geeks'
print("\nDictionary after adding 3 elements: ")
print(Dict)

# method to access elements from a dictionary
Dict = {0: 'Geeks', 1: 'For', 2: 'Geeks'}
print("\nAccessing a element using key: ")
print(Dict[1])

# method to delete elements from a dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("\nInitial Dictionary: ")
print(Dict)
del Dict[1]
print("\nDeleting a specific key: ")
print(Dict)
Dict.pop(3)
print("\nPopping specific element: ")
print(Dict)
Dict.popitem()
print("\nPopping last item: ")
print(Dict)

# method to delete entire dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("\nInitial Dictionary: ")
print(Dict)
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)

# method to copy dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("\nInitial Dictionary: ")
print(Dict)
Dict1 = Dict.copy()
print("\nNew Dictionary: ")
print(Dict1)

# method to create nested dictionary
nested_dict = {1: {'Text': 'Hello', 'Transaltion': 'Hola'}, 2: {'Text': 'Bye', 'Translation': 'Adios'}}
nested_dict[3] = {'Text': 'Thank you', 'Translation': 'Gracias'}
nested_dict.update({4: {'Text': 'Please', 'Translation': 'Por favor'}})
print("\nNested dictionary: ")
for key in nested_dict:
    print(key, nested_dict[key])