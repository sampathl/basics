import book

class Booklist(object):
    def __init__(self,name_,head=None):
        self.head=head
        self.name=name_

    def add_book(self,isbn_,last_,first_,title_):
        if self.head:
            current=self.head
            if current.book.isbn>isbn_:
                new=book.Booknode(isbn_,last_,first_,title_)
                new.next=current
                self.head=new
                #print("added as the first node")
                return
            elif current.book.isbn==isbn_:
                #print("duplicate book")
                return
            else:    
                while current.next and current.next.book.isbn<=isbn_ :
                    if current.next.book.isbn==isbn_:
                        #print("duplicate book")
                        return
                    elif current.next.book.isbn<isbn_:
                        current=current.next
                if current.next==None:
                    new=book.Booknode(isbn_,last_,first_,title_)
                    current.next=new
                    #print("added as last node")
                    return
                elif current.next.book.isbn>isbn_:
                    new=book.Booknode(isbn_,last_,first_,title_)
                    new.next=current.next
                    current.next=new
                    #print("added as a node")
                    return
        else:
            self.head=book.Booknode(isbn_,last_,first_,title_)
            #print("added as the new node")
    
    def get_books(self):
        #print(self.name)
        if self.head:
            counter=0
            current=self.head
            while current:
                dp=current.book
                print("Book{"+"ISBN={}, last={}, first={}, title={}".format(dp.isbn,dp.last,dp.first,dp.title)+"}")
                current=current.next
                counter+=1
            print("count: {}".format(counter))        

    def add_node(self, new_ele):
        if self.head:
            current=self.head
            isbn_=new_ele.book.isbn
            if current.book.isbn>isbn_:
                new_ele.next=current
                self.head=new_ele
                print("added at first")
            elif current.book.isbn==isbn_:
                print("duplicate book")
                return
            else:
                while(current.next and current.next.book.isbn<=isbn_):
                    if (current.next.book.isbn==isbn_):
                        print("duplicate")
                        return
                    elif (current.next.book.isbn<isbn_):
                        current=current.next
                if current.next==None:
                    current.next=new_ele
                    new_ele.next=None
                    print("added at last")
                    return
                elif(current.next.book.isbn>isbn_):
                    new_ele.next=current.next
                    current.next=new_ele
                    print("in the middle")
                    return
        else:
            self.head=new_ele
            new_ele.next=None
            print("added as first")
        return


