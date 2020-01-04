def reverseVowels(s):
    l=list(s)
    ov={'a','e','i','o','u'}
    """l1=[]
    l2=[]
    for i in range(len(l)):
        if l[i].lower() in ov:
            l1.append(i)
            l2.append(l[i])
    l2=l2[::-1]
    for i, j in enumerate(l1):
        l[j]=l2[i]
    return "".join(l)"""
    
    if s: 
        i=0
        j=len(l)-1
        while i<j:
            while l[i].lower() not in ov:
                i+=1
                if i>=len(l):
                    break
                print("i:", i)
            if i>=j:
                break
            while l[j].lower() not in ov:
                    j-=1
                    print("j:", j)
                    if i>=j:
                        break   
            if l[i] in ov and l[j] in ov:
                tem=l[i]
                l[i]=l[j]
                l[j]=tem
                i+=1
                j-=1
        return "".join(l)
    else: 
        return s

print(reverseVowels('hello'))
print(reverseVowels("  "))
print(reverseVowels(""))
print(reverseVowels("aA"))
print(reverseVowels("0011"))