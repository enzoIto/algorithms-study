
def car(pair):
    def first(a, _):
        return a
    return pair(first)

def cdr(pair):
    def last(_, b):
        return b
    return pair(last)

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

pair = cons(3,4)
print(car(pair))  # prints 3
print(cdr(pair))  # prints 4
