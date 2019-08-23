from collections import deque

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        self.depthFirstSearchHelperStack(self, array)
        return array

    # T: O(N)
    # S: O(N) with stack overflow possibility
    def depthFirstSearchHelperRecursive(self, node, array):
        if node is None:
            return
            
        array.append(node.name)

        for child in node.children:
            self.depthFirstSearchHelper(child, array)

    # T: O(N)
    # S: O(N) without stack overflow possibility
    def depthFirstSearchHelperStack(self, node, array):
        stack = []
        stack.append(node)

        while stack:
            node = stack.pop()
            array.append(node.name)
            for child in reversed(node.children):
                stack.append(child)


tree = Node("A")
# For A
tree.children.extend([Node("B"), Node("C"), Node("D")])
# For B
tree.children[0].children.extend([Node("E"), Node("F")])
# For F
tree.children[0].children[1].children.extend([Node("I"), Node("J")])
# For D
tree.children[2].children.extend([Node("G"), Node("H")])
# For G
tree.children[2].children[0].children.extend([Node("K")])


array = []
print(tree.depthFirstSearch(array))
