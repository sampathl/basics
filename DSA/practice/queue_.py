# Implementation of Queue

#node
class Node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

#queue
class Queue():
    def __init__(self, data=None):
        self.head=None
        self.tail=None
        self.length=0
        if data:
            node=Node(data)
            self.head=node
            self.tail=node
            self.length+=1

#push
    def push(self,data):
        node=Node(data)
        if self.length == 0:
            self.head=node
            self.tail=node
        else:
            temp=self.tail
            temp.next=node
            self.tail=node
        self.length +=1
        return True

#pop
    def pop(self):
        if self.head:
            temp=self.head
            self.head=self.head.next
            self.length-=1
            return temp
        return False

#find
    def find(self, data):
        node=self.head
        while node:
            if node.data == data:
                return node 
            node=node.next
        return False
#print
    def __str__(self):

        temp="["
        node=self.head
        while node:
            temp+=str(node.data)+","
            node=node.next
        return temp+"]"


if __name__ == "__main__":
    q= Queue(1)
    q.push(2)
    q.push(3)
    print(q)
    print(q.pop())
    print(q.find(2))
    q.pop()
    q.pop()
    print(q)
    print(q.push(1))
    print(q)

