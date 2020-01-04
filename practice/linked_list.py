class node():
    def __init__(self, data):
        self.element= data
        self.next= None

class Linked_list():
    def __inti__(self):
        self.head =None
    
    def add(self, data):
        if data != None:
            new= node(data)
            self.head = new
        else:
            print("please provide data")
    
    def transverse (self):
        if self.head != None:
            pnt = self.head
            while pnt != None:
                print(pnt.element)
                pnt=pnt.next
            print("end of list")
        else: 
            print("the list is empty")

list1= Linked_list()
#list1.transverse()
list1.add(2)
list1.add(23)
list1.transverse()