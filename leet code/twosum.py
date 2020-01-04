numbers=[2,7,11,15]
target=9
d={}
for a,i in enumerate(numbers):
    print(a,i, target-i,d)
    if target-i in d:
        print([d[abs(target)],a+1])
    else:
        d[abs(target-i)]=a=1
                