def getNthFib(n):
    if n-1 == 0:
    	return 0
    elif n-1 == 1:
    	return 1
    else:
        prev = 0
        curr = 1
        ans = 0
        for num in range(2, n):
            ans = prev + curr
            prev = curr
            curr = ans
        return ans

# 0 1 1 2 3 5 8
# print(getNthFib(0))
print(getNthFib(1))
print(getNthFib(2))
print(getNthFib(3))
print(getNthFib(4))
print(getNthFib(5))
print(getNthFib(6))
print(getNthFib(7))
