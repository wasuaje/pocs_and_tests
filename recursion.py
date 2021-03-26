

a=[1, 2, [11, 13, [3, 4, [7, 56, 6], 5, 6]], 8]
def recursive_sum(nested_num_list):
	sum = 0
	for element in nested_num_list:		
		if type(element) == type([]):
			sum = sum + recursive_sum(element)
		else:
			sum = sum + element
	return sum

z=recursive_sum(a)
print z
