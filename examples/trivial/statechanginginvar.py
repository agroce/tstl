state = 0

def check():
    global state
    state += 1
    return True

def foo(n):
    global state
    state = n

def bar(n):
    global state
    assert state < 6
