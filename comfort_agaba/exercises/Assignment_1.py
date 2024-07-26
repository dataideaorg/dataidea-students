#Above is how to pick the last name in a list. 
List = ['Agaba', 'Israel', 'Comfort', 'Turindirize']
print(List[3:])
# Negative indexing

#Adding several names in a list
names = ['gaso', 'global', 'perfect']
names_of_buses = ['Higer', 'Isuzu', 'Scania']
names.extend(names_of_buses)
print(names)

#Using Del function to delete
names = ['gaso', 'global', 'perfect']
del names[1]
print(names)

#Length of elements in a list
names = ['gaso', 'global', 'perfect']
print(len(names))

#Checking if an item exists in a list. 
name_check = 'gaso'
names = ['gaso', 'global', 'perfect']
if name_check in names:
    print(f'{name_check} is in the list of names')
else:
    print(f'{name_check} is not in the list of names') 

#SETS
#Number of items in a set. 
names = {'gaso', 'global', 'perfect'}
num_items =len(names)
print(len(names))

#combining 2 sets
names = {'gaso', 'global', 'perfect'}
names_of_buses = {'Higer', 'Isuzu', 'Scania'}
Addition = names | names_of_buses
print(Addition)
# update method

# Checking if an item exists in a set
names = {'gaso', 'global', 'perfect'}
if 'global' in names:
    print('global')
else:
    print('global')

