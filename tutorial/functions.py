"""Content: Function, Partial, OperatorOverloading, Generator, Coroutines."""


# =================================================================================================
# Functions: AKA  procedure, subroutine, subprocess
# Global: enables write permissions to upper level vars, need to be defined at each level
def outer1():
    """Outer1."""
    a = 2
    print("a pre inner:", a)

    def inner():
        a = 3
        print("a at inner:", a)

    inner()
    print("a post inner:", a)


a = 5
outer1()
print("a outside:", a)  # = 2 3 2 5


def outer2():  # using global/nonlocal
    """Outer2."""
    a = 2
    print("a pre inner:", a)  # = 2

    def inner():
        global a  # enables access to global only, not edit
        a = 3  # if didn't need to assign any, a would be 2
        print("a at inner:", a)  # but now it's 3

    inner()
    print("a post inner:", a)  # =2, because no global a in outer()


a = 5
outer2()
print("a outside:", a)  # 2, 3, 2, 3 --> inner() overwrote 5


# Nonlocal: doesn't write to top level, but at 1 level above only
def outer3():  # using global/nonlocal
    """Outer3."""
    a = 2
    print("a pre inner:", a)  # = 2

    def inner():
        nonlocal a  # neither local nor global
        a = 3  # similarly, if not assigned, a would be 2
        print("a at inner:", a)  # = 3, overwrites at outer() level, but not at global level

    inner()
    print("a post inner:", a)  # =2, because no global a in outer()


a = 5
outer3()
print("a outside:", a)  # 2, 3, 3, 5


# -------------------------------------------------------------------------------------------------
# Packing:
lst1 = [1, 2, 3]
a, b, c = lst1  # unpacks
lst2 = a, b, c  # packs


# *args/**kwargs: used to pass varying number of args to a func, (kwarg = keyword + arg)
def fun(a, b, c, **kwargs):  # c = fun(a, b, c, d, e, f)
    """Return the sum of all args."""
    total = a + b + c
    print(a, b, c, end=" ")  # 1 2 3
    for k, v in kwargs.items():  # print a packed dict arg
        print(k, v, end=" ")  # 4 5 6
        total = total + v
    return total


arg1 = 1
args = [2, 3]  # *args for (b, c), can also use tuple (2, 3)
kwargs = {"d": 4, "e": 5, "f": 6}  # **kwargs for (d, e, f),
fun(arg1, *args, **kwargs)  # = 1 2 3 4 5 6 21
fun(arg1, *args, d=4, e=5, f=6)  # = 1 2 3 4 5 6 21

# -------------------------------------------------------------------------------------------------
# Partial: creates a subset of another func, helps code reuse
from functools import partial


def adder(a, b, c):  # general adder func
    """Create abc number from a,b, and c."""
    return 100 * a + 10 * b + c


add_bc = partial(adder, 1, 2)  # partial func with fixed a=1, b=2 (first items first)
print(add_bc(5))  # = 100*1 + 10*2 + 5  = 125

add_ab = partial(add_bc, c=2)  # partial (sub) func with fixed c=2
print(add_ab(2, 3))  # = 200*1 + 30*2 + 2  = 232, had to provide 2 args now


# -------------------------------------------------------------------------------------------------
# OperatorOverloading: creates a superset of another func, helps code reuse
# - Python doesn't support overloading, so we will overwrite it.
def adder(a, b, c, d):
    """Define empty function."""
    pass  # defines an empty function


del adder


def adder(*args):  # workaround: add/concat manually using packing
    """Sum the given arguments."""
    total = 0
    n = len(args)
    for i in range(n):
        if not isinstance(args[i], int):  # all items should be int o.w. can't add up
            return None
        total = total + args[i] * pow(10, n - i - 1)  # = 1000*a + 100*b + 10*c + d
    return total


adder(1, 2, 3, 4)  # = 1234


# -------------------------------------------------------------------------------------------------
# Generators: Func with yield, used for iterative algo that we only care about the next
def gen():
    """Generate preset values."""
    yield 1
    yield 3


x = gen()  # create a gen object and iterate
x.__next__()  # = 1
x.__next__()  # = 3
x.__next__()  # StopIteration err


def fib(limit):
    """Perform x = x-1 + x-2."""
    n1, n2 = 0, 1  # init first 2 items
    while n1 < limit:
        yield n1
        n1, n2 = n2, n1 + n2  # w/o using a temp var


x = fib(5)  # call it, a1 = 5 is the limit
print(list(x))


# -------------------------------------------------------------------------------------------------
def func1(func):
    func.data = func(3) + 2
    return func.data


# @func1                                # to specify the decorator to be applied on fun1
def func3(x3):
    return x3


func1(func3)  # = 3+2 = 5


# -------------------------------------------------------------------------------------------------
# Closures: inner functions remember how their enclosing namespaces look like when they are defined
# - Enables the inner function see stuff beyond the outer function
# - object that remembers values even if they aren't in the memory
def func4():
    arr = [1]  # mutable list

    def inner(x):  # immutable str
        arr.extend([x])  # compiler calls LOAD_DEREF, looks for the list ref only
        return l

    return inner


func4_in = func4()  # points directly to the inner function (N/A yet)
func4_in(2)  # = [1, 2]
print(inner(3))  # = [1, 2, 3]


def func5():
    arr = [1]

    def inner(x):
        nonlocal arr  # to fix Unbound err, so the next line can use the global var above
        arr += [x]  # compiler calls LOAD_FAST to check list value --> UnboundLocalError
        return 1

    return inner


func5_in = func5()
print(func5_in(2))
print(func5_in(3))


# another ex:
x0 = 5  # enables the inner function see stuff beyond the outer function


def fun1(x1):
    x1 = 2

    def fun2():  # won't see x0
        return x0 + x1

    return fun2  # we are not calling it but instead returning it


print(fun1(3))  # = 5 + 3 = 8
# fun2.__closure__      # screw it --> just write a class instad


# -------------------------------------------------------------------------------------------------
# Coroutines: generalization of subroutines, used for cooperative multitasking
# it can suspend and transfer (yield) control to other coroutine, then resume again
# just like OS switches between threads using scheduler, OOP language switch coroutines
# works like Generators in producing iterable data, but Coroutines can also consume data
# send() methods sends values to Coroutine, which sends back with (yield) expression


def print_name(prefix):
    """Advance execution to the first yield expression."""
    print(f"Searching prefix:{prefix}")
    while True:
        name = yield
        if prefix in name:
            print(name)
        # calling coroutine, nothing will happen


corou = print_name("Dear")  # start sending input
corou.__next__()
corou.send("Atul")  # not in the name yielded
corou.send("Dear Atul")  # it's in the name --> it'll print the inputs so far
corou.close()  # generates GeneratorExit exception (can be catched)
corou.send("Atul")  #  //   StopIteration exception


# initial source(producer) starts the pipeline, sink ends it with possible data display/save
def producer(sentence, next_coroutine):
    """Split strings and feed it to pattern_filter."""
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):  # search for words ending with -ing
    print(f"Searching prefix:{prefix}")
    print(f"Searching for {pattern}")
    try:
        while True:
            token = yield
            if pattern in token:  # if pattern got matched, send it to next coroutine (print)
                next_coroutine.send(token)
    except GeneratorExit:  # catch exit exception and display
        print("Done with filtering!!")


def print_token():  # sink, display the received tokens
    try:  # i
        while True:
            token = yield
            print(token)
    except GeneratorExit:
        print("Done with printing!")


pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)  #
pf.__next__()
sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)  # --> running, moving
