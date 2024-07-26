# a dictionary is an unordered and mutable collection of items

person = {
    'name': 'John Tong',
    'age': 23,
    'city': 'Juba',
    'title': 'data scientist',
    'skills': ['python', 'machine learning', 'sql']
}

# nesting dictionary
employees = {
    'person1': {
        'name': 'John',
        'age': 22,
        'city': 'New York'
    },
    'person2': {
        'name': 'Jane',
        'age': 24,
        'city': 'Los Angeles'
    }
}

print(employees['person2']['city'])
