#!/usr/bin/env python3
data = [1, 2, 1, 3, 5, 6, 4]
max_val = data[0]
index = 0

if __name__ == '__main__':
	for x in range(len(data)):
		if data[x] > max_val:
			max_val = data[x]
			index = x

	print("max val : {}, index : {}".format(max_val, index))

