# Implementation of Stack 

#node 
class Node():
    def __init__(self,data,previous=None):
        self.data=data
        self.prev=previous

#stack 
class Stack():
    def __init__(self, data=None):
        self.top = None
        self.size=0
        if data:
            self.top=Node(data)
            self.size+=1
    
    def push(self,data):
        node=Node(data)
        if self.top:
            node.prev=self.top
        self.top=node
        self.size+=1

    def pop(self):
        if self.top:
            temp= self.top
            self.top = temp.prev
            return temp
        return False
    
    def find(self, data):
        node=self.top
        while node:
            if node.data==data:
                return True
            node=node.prev
        return False
    
    def print(self):

        node= self.top
        while node:
            print(node.data, end=",")
            node=node.prev
        print(" ")


        
if __name__ == "__main__":
    s = Stack()
    s.print()
    s.push(5)
    s.push(6)
    s.print()
    print(s.pop())
    s.print()
    print(s.find(5))
    