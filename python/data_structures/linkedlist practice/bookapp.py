import booklist
import fileinput

categories =[]
def split_lines(name):
    with open(name) as f:
        lines=f.read().splitlines()
    return lines

file_name=split_lines("categories.txt")

for line in file_name:
    categories.append(line+".txt")
#print(categories)

for i,category in enumerate(categories):
    new=file_name[i]
    file_name[i]=booklist.Booklist(new)
    book_names= split_lines(category)
    for book in book_names:
        details=book.split(",")
        #print(details)
        file_name[i].add_book(details[0],details[1],details[2],details[3])
    print("Book List: {}".format(file_name[i].name))
    file_name[i].get_books()


merge=booklist.Booklist("merge")

for lists in file_name:
    current=lists.head
    while current:
        if current.next:
            print(lists.name)
            lists.head=current.next
            temp=current
            current=current.next
            temp.next=None
            merge.add_node(temp)

        else:
            print("here now")
            merge.add_node(current)
            current=None
            lists.head=None

merge.get_books()
second=booklist.Booklist("second")
current=merge.head
while current:
    if current.book.last[0]>"M" :
        #current=current.next
        temp=current
        current=current.next
        temp.next=None
        second.add_node(temp)
    else:
        current=current.next

merge.get_books()
second.get_books()

            


