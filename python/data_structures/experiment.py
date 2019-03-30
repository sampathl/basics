"""some_guy="fred"

def new_function(new_li):
    new_li.append("sam")
    print(new_li)
    return
new_list=[]
new_list.append(some_guy)

my_list=new_list
my_list.append("george")

some_guy = "new"

print(some_guy, my_list,new_list)
new_function(my_list)
print(some_guy, my_list,new_list)"""

def f(a, L=0,*arg, **kwarg):
    """Do not show this 

        sampath lakkaraju"""
    if L is None:
        L = []
    print(a,L)
    for ar in arg:
        print("this is arg {}".format(ar))
    for kw in kwarg:
        print("these are arguments")
        print(kw,kwarg[kw])

new={"a":"0","L":"2", "new":"0","strn":"neww"}
f( **new)
print(f(4,5,4,L=5))
f()