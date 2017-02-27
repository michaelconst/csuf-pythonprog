from contextlib import contextmanager


greeting = 'Hello! '


@contextmanager
def many_greetings(msg, count):
    original_msg = msg
    global greeting
    greeting = msg * count
    yield greeting
    greeting = original_msg


print('before with: %s' % greeting)
with many_greetings(greeting, 3) as say:
    print('in with: %s' % say)

print('after with: %s' % greeting)


