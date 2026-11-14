class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None 
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.m = {}
        self.start = Node(0, 0)
        self.end = Node(0, 0)
        
        self.start.next = self.end
        self.end.prev = self.start

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev 

    def addFirst(self, node):
        temp = self.start.next

        self.start.next = node
        node.prev = self.start
        node.next = temp
        temp.prev = node 

    def get(self, key: int) -> int:
        ## if not in cache

        if key not in self.m:
            return - 1

        ## if it is in cache
        node = self.m[key]
        res = node.val
        ## move the node to the start because it is just visited
        self.deleteNode(node)
        self.addFirst(node)

        return res
        

    def put(self, key: int, value: int) -> None:

        ## if not in cache
        if key not in self.m:
            if len(self.m) == self.cap:
                nodeToRenove = self.end.prev
                self.deleteNode(nodeToRenove)
                del self.m[nodeToRenove.key]

            node = Node(key, value)
            self.m[key] = node
            self.addFirst(node)
            return
        
        node = self.m[key]

        self.deleteNode(node)
        self.addFirst(node)
        node.val = value
        self.m[key] = node

        return
        
