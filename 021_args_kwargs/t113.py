# Example 1: Create a Dictionary

def create_dictionary(**kwargs):
    return kwargs


result = create_dictionary(name='Alice', age=30, city='New York')
print(result)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
