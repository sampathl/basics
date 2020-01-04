def compress(chars):
    element=""
    count=0
    index=None
    for i,s in enumerate(chars):
        if count==0 and element=='':
            count=1
            element=s
        elif count==1 and element==s:
            count+=1
            index=i
        elif count>=2 and element==s:
            count+=1
            chars[i] = False
        elif element!=s:
            if count==1:
                pass
            if count>=2:
                if len(str(count))>1:
                    l=list(str(count))
                    for i in range(len(l)):
                        chars[index+i]=l[i]
                else:    
                    chars[index]=str(count)
            count=1
            element=s
    if count>1:
        if len(str(count))>1:
            l=list(str(count))
            for i in range(len(l)):
                chars[index+i]=l[i]
        else:    
            chars[index]=str(count)
            
    chars=[i for i in chars[:] if i !=False]
    return chars


print(compress(["a","a","a","b","b","a","a"]))