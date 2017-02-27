from contextlib import contextmanager


greeting = 'Hello! '


# @contextmanager
# def many_greetings(msg, count):
#     original_msg = msg
#     global greeting
#     greeting = msg * count
#     yield greeting
#     greeting = original_msg

@contextmanager
def many_greetings(msg, count):
    original_msg = msg
    global greeting
    greeting = msg * count
    errmsg = ''
    try:
        yield greeting
    except Exception as e:
        errmsg = 'error %s' % str(e)
    finally:
        greeting = original_msg
        if errmsg:
            print(errmsg)

try:
    print('before with: %s' % greeting)
    with many_greetings(greeting, 3) as say:
        print('in with: %s' % say)
        if len(say) > 10:
            raise ValueError('greeting is too long')
finally:
    print('after with: %s' % greeting)


