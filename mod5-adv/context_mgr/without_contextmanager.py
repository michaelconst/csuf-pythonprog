greeting = 'Hello! '

def many_greetings(msg, count):
    global greeting
    greeting = msg * count

print('before call: %s' % greeting)
many_greetings(greeting, 3)
print('after call: %s' % greeting)


