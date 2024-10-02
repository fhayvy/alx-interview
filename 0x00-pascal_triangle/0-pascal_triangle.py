#!/usr/bin/python3


def pascal_triangle(n):
	if n <= 0:
		return []
	
	result = [[1]]

	for row in range(1, n):
		new_row = [1]

		for i in range(1, row):
			new_row.append(result[-1][i-1] + result[-1][i])

		new_row.append(1)
		result.append(new_row)

	return result