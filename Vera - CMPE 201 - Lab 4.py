class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.tail = newNode
            self.head = newNode

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
    
    def remove_beginning(self):
        if self.head is None:
            return None

        deletedData = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return deletedData

    def remove_at_end(self):
        if self.tail is None:
            return None

        if self.head.next is None:
            deletedData = self.head.data
            self.head = None
            self.tail = None
            return deletedData
        
        current = self.head
        while current.next.next:
            current = current.next

        deletedData = current.next.data
        current.next = None
        self.tail = current
        return deletedData
    
    def remove_at(self, data):
        if not self.head:
            return None
        
        if self.head.data == data:
            deletedData = self.head.data
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return deletedData

        current = self.head
        while current.next:
            if current.next.data == data:
                deletedData = current.next.data
                current.next = current.next.next
                if not current.next:
                    self.tail = current
                return deletedData
            current = current.next
        return None

    def get_linked_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
vct26pac_pr = LinkedLists()
vct26pac_pr.insert_at_beginning("DRX")

vct26pac_pr.insert_at_beginning("T1")
vct26pac_pr.insert_at_beginning("RRQ")
vct26pac_pr.insert_at_beginning("Paper Rex")
vct26pac_pr.insert_at_end("Zeta Division")
vct26pac_pr.insert_at_end("Talon Esports")
vct26pac_pr.insert_at_end("Gen.G")
vct26pac_pr.insert_at_end("Global Esports")
vct26pac_pr.insert_at_end("Team Secret")

print(vct26pac_pr.remove_beginning())
print(vct26pac_pr.remove_at_end())
print(vct26pac_pr.remove_at("RRQ"))
print(vct26pac_pr.remove_at("DFM"))

print(vct26pac_pr.get_linked_list())