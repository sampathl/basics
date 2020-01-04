from contextlib import contextmanager

@contextmanager
def fib_ser(n):
    try:
        print("need to check ", n)
        yield(10)
    finally:
        print("this is done")


with fib_ser(30) as i:
    for a in range(i):
        print(a)

