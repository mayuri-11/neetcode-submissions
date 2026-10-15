class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapp = {}

        self.a = Node(0,0)
        self.b = Node(0,0)

        self.a.next = self.b
        self.b.prev = self.a

    def remove(self,node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

    def insert(self,node):
        after = self.a.next

        self.a.next = node
        node.prev = self.a

        node.next = after
        after.prev = node        

    def get(self, key: int) -> int:
        if key not in self.mapp:
            return -1
        
        node = self.mapp[key]
        self.remove(node)
        self.insert(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            self.remove(self.mapp[key])
        
        node = Node(key, value)
        self.mapp[key] = node

        self.insert(node)

        if len(self.mapp) > self.capacity:
            lru = self.b.prev
            self.remove(lru)
            del self.mapp[lru.key]

        
