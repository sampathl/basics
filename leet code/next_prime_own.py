def is_prime(l,h):
    primes=[]
    #print("this is printing")
    for i in range(l,h+1):
        counter=0
        #print(i)
        for j in range(2,i):
            if i%j==0:
                #print(i,j)
                counter+=1
                break
        if counter==0:
            #print(chr(i), end=" ")
            primes.append(i)
    return primes

def isPrime(n) : 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def next_prime(s):
    lpri=is_prime(ord('a'),ord('z'))
    #cpri=is_prime(ord('A'),ord('Z'))
    d={}
    ss=set(s)
    for i in ss:
        if ord(i)>lpri[-1]:
            d[i]=lpri[0]
        else:
            for k in lpri:
                if k >=ord(i):
                    d[i]=k
                    break
    lpri.clear()
    for i in s:
        lpri.append(chr(d[i]))
    return "".join(lpri)


print(next_prime('abcdefgz'))

            