class HashNode():
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.next=None
        
class MyHashMap:
    def _hash_key(self,key):
        return key%10000
            
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap=[None]*10000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hkey=self._hash_key(key)
        #counter=0
        prev=None
        pnt=self.hashmap[hkey]
        if pnt==None:
            self.hashmap[hkey]=HashNode(key,value)
        else:
            while pnt:
                if pnt.key==key:
                    pnt.value=value
                    break
                prev=pnt
                pnt=pnt.next
            if prev:
                prev.next=HashNode(key,value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hkey=self._hash_key(key)
        #counter=0
        if self.hashmap[hkey]==None:
            return -1
        else:
            pnt=self.hashmap[hkey]
            while pnt:
                if pnt.key==key:
                    return pnt.value
                pnt=pnt.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hkey=self._hash_key(key)
        #counter=0
        if self.hashmap[hkey]==None:
            pass
        else:
            pnt=self.hashmap[hkey]
            while pnt:
                print("--",pnt.key)
                pnt=pnt.next
            pnt=self.hashmap[hkey]
            if pnt.key==key:
                self.hashmap[hkey]=pnt.next
            elif pnt.next:
                while pnt.next:
                    #print(key, pnt.next.key)
                    if pnt.next.key==key:
                        pnt.next=pnt.next.next
                        break
                    pnt=pnt.next


obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(10002,1)
obj.remove(10002)