# DATA TYPES:
"""
Strings: Any character within quotes - single or double

Integers: Numbers - Whole numbers positive or negative

Floats: Decimal Numbers - positive or negative

List: It contains multiple data types within square brackets = [1, 2, 'Kundil']

Tuple: It's like a list but it is immutable, uses paranethesis instead of square brackets = (1, 2, 'Kundil')

Dictionary: Like list, stored in curly brackets, with key-value pairs
"""

examples = "Examples"
print(examples.upper())
number = 32
print(number+1)
decimal = 32.5
print(decimal-29)
friends = ['Ibrahim', 'Ahmad']
print(friends[1])
print(len(friends))
friends.pop(0)
numbers = ('Ibrahim', 'Ahmad')
print(len(numbers))
person = {"height":2.1, "age":16, "name":"Ismail Musa Kundil", "weight":26.1}
print(person['name'])
print(len(person['name'].split()))

# CONDITIONALS
if number > 5:
    print(examples)
else: print(number)

# LOOP
for name in person['name'].split():
    print(name)

# FUNCTIONS

def myfunction():
    if number > 5:
        print(examples)
    else: 
        print(number)
    
    for name in person['name'].split():
        print(name)

myfunction()