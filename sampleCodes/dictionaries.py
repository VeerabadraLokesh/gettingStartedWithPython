
dictionary = {}

dictionary['a'] = 'b'
dictionary['c'] = 'd'

print(dictionary.get('a'))

for item in dictionary:
    print(dictionary[item])

newDictionary = dictionary.copy()
copyDictionary = dict(dictionary)

print(dictionary.keys())
print(dictionary.values())

for item, value in dictionary.items():
    print(item, value)

if 'a' in dictionary:
    print("dictionary contains 'a'")

if dictionary.pop('b', None):
    print("dictionary had key 'b' but no longer")
else:
    print("there was no item in dictionary with key 'b'")


print(len(dictionary))


dictionary.popitem() # removes last inserted element

del dictionary['a']

print(dictionary)

dictionary = dict(a='b', c='d')
print(dictionary)

copyDictionary.clear()


print(copyDictionary)

print(dict.fromkeys([1,2,3]))

y = dictionary.setdefault('x', 'y')

print(dictionary)

dictionary.update({'ab': 'ba'})

print(dictionary)
