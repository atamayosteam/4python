x = ['apple','orange','pear','grape','watermelon']

print(x)

x.append('strawberry')
print(x[2])

x[0] = 'fruit'
print(x)

del x[2]
print(x)

# my_tuple = ('blue','red','green','yellow')
# my_tuple[2] = 'navy'
# print(my_tuple)

print(len(x))

x.sort()

print(x)

x.reverse()

print(x)

y = ['brown','red','blue','pink','orange']


print( x + y)

#combined two lists into one lists 

print('  '.join(x + y)) 

# removed the commas and quotes by using the .join function

names = ("john,sam,bob".split(","))

print(names)