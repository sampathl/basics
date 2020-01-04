def countAndSay(n): 
    str1=''
    y=[0,0]
    res=''
    if n==1:
        return "1"
    #elif res='':
        #return '11'
    else:
        res=countAndSay(n-1)
        for i in res:
            if y[0]==0:
                y[0]=i
                y[1]=1
            elif y[0]==i:
                y[1]+=1
            elif y[0]!=i:
                str1 =str1+ str(y[1])+str(y[0])
                print(str1, res)
                y[0]=i
                y[1]=1
        str1+=str(y[1])+str(y[0])
        y[0]=0
        y[1]=0
        return str1


print(countAndSay(5))