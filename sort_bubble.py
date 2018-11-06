# -*- coding:utf-8 -*-

# 冒泡排序
# 时间复杂度:<O(n^2)
# 稳定排序
# 思路:
# 	1. 遍历,将最大的值移动到最后
# 	2. 依次操作直到排序结束

# 最基本冒泡排序
def sortBubble(argv):
	l = len(argv)
	for i in range(l):
		for j in range(l - i - 1):
			if argv[j] > argv[j + 1]:
				argv[j], argv[j + 1] = argv[j + 1], argv[j]

# 改进1:增加是否有变化标记
def sortBubble1(argv):
	l = len(argv)
	exchange = False
	for i in range(l):
		for j in range(l - i - 1):
			if argv[j] > argv[j + 1]:
				argv[j], argv[j + 1] = argv[j + 1], argv[j]
				exchange = True
		if not exchange:
			break
		exchange = False

# 改进2:记录最后一次交换的位置,因为之后的都无需交换,所以不处理,减少循环次数
def sortBubble2(argv):
	i = len(argv) - 1
	while i > 0:
		pos = 0
		for j in range(i):
			if argv[j] > argv[j + 1]:
				argv[j], argv[j + 1] = argv[j + 1], argv[j]
				pos = j
		i = pos

# 改进3:同时找出最大最小值
def sortBubble3(argv):
	low = 0
	height = len(argv) - 1
	while low < height:
		for i in range(low, height):
			if argv[i] > argv[i + 1]:
				argv[i], argv[i + 1] = argv[i + 1], argv[i]
		height -= 1
		for i in range(height, low, -1):
			if argv[i] < argv[i - 1]:
				argv[i], argv[i - 1] = argv[i - 1], argv[i]
		low += 1

if __name__ == "__main__":
	a = [3, 1, 5, 7, 2, 4, 9, 6]
	# sortBubble(a)
	# sortBubble1(a)
	# sortBubble2(a)
	sortBubble3(a)
	print(a)