# -*- coding:utf-8 -*-

def sortQuick(argv, low = None, height = None):
	if low == None:
		low = 0
		height = len(argv) - 1
	if low >= height:
		return
	key = argv[low]
	front = low
	back = height
	while front < back:
		while front < back and argv[back] >= key:
			back -= 1
		argv[front] = argv[back]
		while front < back and argv[front] <= key:
			front += 1
		argv[back] = argv[front]
	argv[front] = key
	sortQuick(argv, low, front - 1)
	sortQuick(argv, front + 1, height)

if __name__ == "__main__":
	a = [3, 1, 5, 7, 2, 4, 9, 6]
	sortQuick(a)
	print(a)
