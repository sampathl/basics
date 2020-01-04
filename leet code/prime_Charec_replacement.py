def prime(x):
    k=0
    m = x
    n=x
    count=0
    result = []
    while 1:
        for i in range(2,x):
            if x%i==0:
                count+=1
        if count==0:
            result.append(x)
            break
        else:
            count=0
            x+=1
    x=n
    while 1:
        for i in range(2,x):
            if x%i==0:
                count+=1
        if count==0:
            result.append(x)
            break
        else:
            count=0
            x+=-1
    if abs(result[1]-m)>abs(result[0]-m):
        if result[0]>122:
            out = result[1]
        else:
            out = result[0]
    else:
        out = result[1]
    return chr(out)
        
n = int(input())
for i in range(n):
    s = input()
    arr = list(set(s))
    arr.sort()
    dic = {}
    for i in arr:
        result = prime(ord(i))
        dic[i]=result
    su=""
    for i in s:
        if dic[i].islower():
            su+=dic[i]
        else:
            su+="a"
    print(su)