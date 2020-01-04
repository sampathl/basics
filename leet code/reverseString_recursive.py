def reverseString(s):
    if len(s)==1:
        #print("--",s)
        return s
    elif len(s)>1:
        #print(s[-1],s[:-1])  
        s[:-1]=reverseString(s[:-1])
        s.insert(0,s.pop())
        return s

print(reverseString(['h','e','l','l','o']))