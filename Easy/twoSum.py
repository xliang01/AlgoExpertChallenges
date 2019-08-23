# def twoNumberSum(array, targetSum):
#     numSet = set()
#     ans = []
#
#     for num in array:
#         diff = targetSum - num
#         if diff in numSet:
#             ans.extend([num, diff])
#         else:
#             numSet.add(num)
#     ans.sort()
#     return ans


def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left <= right:
        leftNum = array[left]
        rightNum = array[right]

        if leftNum + rightNum == targetSum:
            return [leftNum, rightNum]
        elif leftNum + rightNum > targetSum:
            right -= 1
        else:
            left += 1
    return []


ans = twoNumberSum([1, 2, 3], 3)
print(ans)
