#  working with strings #
message = "Hello"
name = "Lucas"
greeting = "Hi"

print (message[5:])
print(message.lower())
print(message.count('o'))
print(message.find('o'))
print(f'{greeting}, {name}, Welcome!')
print(message + ', ' + name + ' ' + 'Welcome!')
print(help(str.find))