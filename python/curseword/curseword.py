import urllib
import fileinput
import requests
"""
list_of_words=[]
with fileinput.input(files="message.txt") as f:
    for lines in f:
        print(lines)
        list_of_words.extend(re.split(r'\s+',lines))

print(list_of_words)"""

new_file=open("message.txt",'r')
content=new_file.read()
print(content)
new_file.close()

new_request= requests.get("http://www.wdylike.appspot.com/?q="+content)
print(new_request.text)
