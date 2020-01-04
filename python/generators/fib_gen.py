def fib_gen(n):
    a=1
    b=1
    for i in range(n):
        if i<=1:
            yield(1)
        elif i>1:
            cu=a+b
            a=b
            b=cu
            yield(cu)
        
print(list(fib_gen(10)))