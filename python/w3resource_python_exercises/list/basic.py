import random
import itertools
list1=[1,2,3,4,5,6,7]
sum=0
mul=1
for i in list1:
    sum+=i
    mul*=i
print(sum,mul, max(list1), min(list1))

sample11=['abc', 'xyz', 'aba', '1221']
count=0
for i in sample11:
    if len(i)>2:
        if i[0]==i[-1]:
            count+=1
print(count)

sort_to=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(sort_to, key=lambda s :s[1]))
dummy= [1,4,7,8,9,13,1,3,5]
neww=dummy.copy()

for i,a in enumerate(dummy):
    if a in dummy[i+1:]:
        neww.remove(a)
print(neww)
neww.clear()
if not len(neww):
    print("is empty")

neww.append(2)
def check_one_common(a,b):
    count=0
    for i in a:
        if i in b:
            count+=1
    return count
print(check_one_common(dummy,neww))
l1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l2=[x for (i,x) in enumerate(l1) if i not in (1,4,5)]
print(l2)
l3=[[['*' for i in range(6)] for j in range(4) ]for k in range(3)]
print(l3)
l4= [x for x in range(15)]
l5= [x for x in l4 if x%2!=0]
l6= [(x+1)**2 for x in range(30)]
print(l6)
print(l6[:5])
l66=l6[:5]
l7=list(itertools.permutations(l66))
#print(l7)
s = ['a', 'b', 'c', 'd']
s=''.join(s)
print(l6.index(36))
l8= [[2,4,3],[1,5,6], [9], [7,9,0]]
print(list(itertools.chain(*l8)))
l8.extend(l6)
print(l8)
print(random.choice(l8))


