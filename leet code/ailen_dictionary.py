def isAlienSorted(words,order):
    d={}
    for i in range(len(order)):
        d[order[i]]=i+1
        
    if len(words)>=2:
        for i in range(len(words)-1):
            a=words[i]
            b=words[i+1]
            print(a,b)
            for j in range(min(len(a),len(b))):
                print(a[j],b[j],d[a[j]],d[b[j]])
                if d[a[j]]==d[b[j]]:
                    continue
                elif d[a[j]]>d[b[j]]:
                    return False
                elif d[a[j]]<d[b[j]]:
                    break                   
    return True

print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))