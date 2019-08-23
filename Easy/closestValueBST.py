import sys

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

# T: O(NLogN), Worst O(N)
# S: O(NLogN), Worst O(N)

# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, float("inf"))

# def findClosestValueInBstHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     elif abs(target - tree.value) < abs(target - closest):
#         closest = tree.value
#     if target > tree.value:
#         return findClosestValueInBstHelper(tree.right, target, closest)
#     elif target < tree.value:
#         return findClosestValueInBstHelper(tree.left, target, closest)
#     else:
#         return closest

# T: O(NLogN), Worst: O(N)
# S: O(1), Worst: O(1)
def findClosestValueInBst(tree, target):
    curr = tree
    closest = float("inf")

    while curr is not None:
        if abs(target - curr.value) < abs(target - closest):
            closest = curr.value
        if target > curr.value:
            curr = curr.right
        elif target < curr.value:
            curr = curr.left
        else:
            break

    return closest

test = BST(10).insert(5).insert(2).insert(5).insert(1).insert(15).insert(13).insert(14).insert(22)
ans = findClosestValueInBst(test, 12)
print(ans)
