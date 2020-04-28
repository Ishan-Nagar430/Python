def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [8,6,9,4,2,1,3,7]

bubbleSort(arr)

print("sorted array is : ")
for i in range(len(arr)):
	print("%d" %arr[i])