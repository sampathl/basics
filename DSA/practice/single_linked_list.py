# Single linked list implementation.

class Node():
    def __init__(self, data, next:None):
        self.data=data
        self.next=next


class LinkeList():
    def __init__(self, data=None, next=None):
        self.head= None
        self.tail= None
        self.length=0
        if data:
            node = Node(data, next)
            self.head = node
            self.tail=node
            self.length+=1
        
        return self.head
         
    #add data
    def push(self, data,next=None):
        if self.length:
            self.tail.next= Node(data,next)
            self.tail=self.tail.next
            self.length+=1
        else:
            self.__init__(data,next)
         

    #find data
    def find(self,fdata):
        node=self.head
        while node:
            if node.data == fdata :
                return node
            node=node.next
        return False
    

        
    #remove data 
    def pop(self, ddata=None):
        if not ddata:
            ddata =self.tail.data
        
        # if it is head
        if self.head and self.head.data == ddata:
            temp=self.head
            self.head=self.head.next
            return temp
        
        #serch and pop
        node=self.head
        while node.next:
            if node.next.data == ddata:
                temp = node.next
                node.next=node.next.next
                return temp
            node=node.next
        return False
    
    def print(self):
        node=self.head
        while node:
            print(node.data,end=",")
            node=node.next
        print(' ')




if __name__ == "__main__":
    a=LinkeList()
    a.print()
    a.push(1)
    a.push(2)
    a.print()
    a.push(3)
    a.print()
    print(a.pop())
    a.print()
    a.push(3)
    print(a.find(2))
    print(a.pop(2))
    a.print()



