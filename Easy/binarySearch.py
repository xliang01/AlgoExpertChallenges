def binarySearch(array, target):
	start = 0
	end = len(array)-1

	while start <= end:
		mid = int((start + end) / 2)
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			start = mid + 1
		else:
			end = mid - 1
	return -1

print(binarySearch([1, 2, 3, 4, 5, 6], 5))