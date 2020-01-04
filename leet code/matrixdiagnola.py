def findDiagonalOrder(matrix):
    m=len(matrix)
    n=len(matrix[0])
    l=[]
    if m+n==0:
        return matrix
    elif m==1:
        print("m")
        return matrix[0][:]
    elif n==1:
        print("n")
        for i in matrix:
            l.append(i[0])
    else:
        c=0
        r=0
        l.append(matrix[r][c])
        coun=0
        while c<n-1 and r<m-1:
            print(c,n)
            if (r==0 or r==m-1) and coun==0:
                if c<n-1:
                    c+=1
                    coun=1
                    l.append(matrix[r][c])
            elif (c==0 or c==n-1) and coun==0:
                if r<m-1:
                    r+=1
                    coun=1
                    l.append(matrix[r][c])
            elif (r==0 or c==n-1) and coun==1:
                while (c>0 or r<m-1):
                    r+=1
                    c-=1
                    l.append(matrix[r][c])
                coun=0
            elif (c==0 or r==m-1) and coun==1:
                while (c<n-1 or r>0):
                    r-=1
                    c+=1
                    l.append(matrix[r][c])
                coun==0
        return l

print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(findDiagonalOrder([[]]))
print(findDiagonalOrder([[1,2,3]]))
print(findDiagonalOrder([[1],[4],[7]]))