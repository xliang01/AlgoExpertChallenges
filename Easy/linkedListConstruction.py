class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if node == self.head:
            return
        self.remove(node)
        self.insertBefore(self.head, node)
        self.head = node
        self.setDefaultTail()

    def setTail(self, node):
        if node == self.tail:
           return
        self.remove(node)
        self.insertAfter(self.tail, node)
        self.tail = node
    
    def insertBefore(self, node, nodeToInsert):
        if node is None:
            return

        nodeToInsert.next = node

        if node.prev is not None:
            nodeToInsert.prev = node.prev
            node.prev.next = nodeToInsert

        if node == self.head:
            self.head.prev = nodeToInsert
            self.head = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if node is None:
            return

        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        node.next = nodeToInsert

        if node == self.tail:
            self.tail = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        curr = self.head
        for index in range(1, position):
            curr = curr.next
        self.insertBefore(curr, nodeToInsert)

    def removeNodesWithValue(self, value):
        curr = self.head
        while curr:
            nextNode = curr.next
            if curr.value == value:
                self.remove(curr)
            curr = nextNode

    def remove(self, node):
        if node is not None:
            if node == self.head and self.head is not None:
                node = node.next
                self.head = node
            elif node == self.tail and self.tail is not None:
                node = node.prev
                node.next = None
                self.tail = node
            else:
                if node.prev is not None:
                    node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev

    def containsNodeWithValue(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def setDefaultTail(self):
        if self.tail is not None:
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        self.tail = curr

    def print(self):
        curr = self.head
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        output = "->".join(str(value) for value in values)
        print(output)

# Init Data
list = DoublyLinkedList()
head = Node(1)
curr = head
prev = None

for index in range(2, 6):
    prev = curr
    curr.next = Node(index)
    curr = curr.next
    curr.prev = prev

list.setHead(head)
print("Sample Input")
list.print()

# Test
print("Set head to 4")
list.setHead(Node(4))
list.print()

print("Set tail to 6")
list.setTail(Node(6))
list.print()

print("Insert 3 before 6")
list.insertBefore(list.tail, Node(3))
list.print()

print("Insert 3 after 6")
list.insertAfter(list.tail, Node(3))
list.print()

print("Insert 3 at position 1")
list.insertAtPosition(1, Node(3))
list.print()

print("Remove all nodes with value 3")
list.removeNodesWithValue(3)
list.print()

print("Remove all nodes with value 2")
list.removeNodesWithValue(2)
list.print()

print("Check if list contains 5")
print(list.containsNodeWithValue(5))
