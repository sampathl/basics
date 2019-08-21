def func(strs) -> str:

    # save the first sting 
    n='abc'
    # use a variable for cout of the char
    if len(strs)==0:
        return ''
    elif len(strs)==1:
        return strs[0]
    string=strs[0]
    if string=='':
        return ''
    # work on all other elements in the list 
    for i in range(1,len(strs)): 
        print('i=',i)
        if n == 'abc':
            n=0
            for a in range(min(len(strs[i]),len(string))):
                
                if string[a]==strs[i][a]:
                    n+=1
                else:
                    break
                print("123, n=",n,a)
        elif n==0:
            break
        else:
            for a in range(min(len(strs[i]),len(string))):
                print(string,strs[i][a])
                if a <= n: 
                    if string[a] == strs[i][a]:
                        continue
                    elif a <= n :
                        n = a
                else:
                    break

    print('n=',n)
    if n == 0:
        return ''
    elif isinstance(n,int) and n >0 :
        return string[:n]
    elif n == 'abc':
        print("there is an error")
            

new= func(['aa','ab'])
print(new)