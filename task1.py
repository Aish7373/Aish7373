# Creating a list
my_list = [1, 2, 3, 4, 5]

# Adding an element to the list
my_list.append(6)

# Removing an element from the list
my_list.remove(3)

# Modifying an element in the list
my_list[0] = 10

print("updated list:", my_list)

# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'Delhi'}

# Adding to the dictionary
my_dict['gender'] = 'male'

# Removing from the dictionary
del my_dict['age']

# Modifying the dictionary
my_dict['city'] = 'Mumbai'

print("updated dictionary:", my_dict)

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding to the set
my_set.add(6)

# Removing from the set
my_set.remove(3)

# Modifying the set
my_set.discard(1)
my_set.add(10)

print("updated set:", my_set)