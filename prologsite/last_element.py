def mylast(element_list):
	if element_list:
		return element_list[-1]

def last_but_one(element_list):
	if element_list and len(element_list) >= 2:
		return element_list[-2]

def kth_element(element_list, k=1):
	if element_list and k and k>0 and len(element_list) > k:
		return element_list[k-1]

def element_length(element_list):
	return len(element_list)

def element_in_reverse(element_list):
	return element_list[::-1]

def is_pallindrome_list(element_list):
	reverse_list = element_in_reverse(element_list)
	if reverse_list == element_list:
		return True
	else:
		return False

def flatten_list(list_tobe_flatten):
	result = []
	for element in list_tobe_flatten:
		if not isinstance(element, list):
			result.append(element)
		else:
			result.extend(flatten_list(element))
	return result

def remove_duplicates(element_list):
	# return list(set(element_list))
	result = []
	if element_list and len(element_list) >= 2:
		latest = element_list[0]
		result.append(latest)
		for element in element_list[1:]:
			if element != latest:
				latest = element
				result.append(latest)
	else:
		return list(set(element_list))
	return result

def pack_duplicates(element_list):
	result = []
	if element_list and len(element_list) > 2:
		latest = element_list[0]
		pack = []
		for element in element_list[1:]:
			pack.append(latest)
			if element != latest:
				result.append(pack)
				latest = element
				pack = []
			else:
				pack.append(element)
	elif len(element_list) == 2:
		result = [element_list] if element_list[0] == element_list[1] else [[element_list[0]],[element_list[1]]]
	else:
		return element_list
	return result

def pack_duplicates(element_list):
	result = []
	if element_list and len(element_list) > 2:
		latest = element_list[0]
		pack = [latest]
		for element in element_list[1:]:
			if element != latest:
				latest = element
				result.append(pack)
				pack = [latest]
			else:
				pack.append(element)
		result.append(pack)
	elif len(element_list) == 2:
		result = [element_list] if element_list[0] == element_list[1] else [[element_list[0]],[element_list[1]]]
	else:
		return element_list
	return result

def length_encoding(element_list):
	result = []
	if element_list and len(element_list) >= 2:
		latest = element_list[0]
		count = 1
		pack = []
		for element in element_list[1:]:
			if element != latest:
				result.append([count, latest])
				latest = element
				count = 1
			else:
				count += 1
		result.append([count, latest])
	elif element_list:
		return [[element_list[0], 1]]
	return result

def modified_length_encoding(element_list):
	# result = []
	# if element_list and len(element_list) >= 2:
	# 	latest = element_list[0]
	# 	count = 1
	# 	pack = []
	# 	for element in element_list[1:]:
	# 		if element != latest:
	# 			result.append([count, latest]) if count > 1 else result.append(latest)
	# 			latest = element
	# 			count = 1
	# 		else:
	# 			count += 1
	# 	result.append([count, latest])
	# elif element_list:
	# 	return [[element_list[0], 1]]
	# return result

	# OR

	result_set = length_encoding(element_list)
	return [result if result[0] >= 2 else result[1]  for result in result_set]

def decode_lenth_encoding(encoded_list):
	from itertools import repeat
	result = []
	# [result.append(element) if not isinstance(element, list) else result.extend(list(repeat(element[1], element[0]))) for element in encoded_list]
	
	# OR

	for element in encoded_list:
		if not isinstance(element, list):
			result.append(element)
		else:
			result.extend(list(repeat(element[1], element[0])))
	return result

def duplicate_the_list(element_list, count):
	from itertools import repeat
	result = []
	[result.extend(list(repeat(element, count))) for element in element_list]
	return result

def drop_nth_element(element_list, n):
	if n == 0 or n >= len(element_list):
		return
	else:
		idx = (n - 1)
		for i in range(0, len(element_list) / n):
			element_list.pop(idx)
			idx += (n -1)
		return element_list

def spilt_list(element_list, length):
	return [element_list[:(length)], element_list[(length):]]

element_list = ['a','b','c','d']
# element_list = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd']
list_tobe_flatten = ['a',['b',['c','d'],'e'],'f']
duplicates = ['a','a','a','a','a','a','b','b','b','a','c','c','d','d','d','d','d','d','d']
encoded_list = [[6, 'a'], [3, 'b'], 'a', [2, 'c'], [7, 'd']]

print mylast(element_list)
print last_but_one(element_list)
print kth_element(element_list, 3)
print element_length(element_list)
print element_in_reverse(element_list)
print is_pallindrome_list(element_list)
print flatten_list(list_tobe_flatten)
print remove_duplicates(duplicates)
print pack_duplicates(duplicates)
print length_encoding(duplicates)
print modified_length_encoding(duplicates)
print decode_lenth_encoding(encoded_list)
print duplicate_the_list(element_list, 3)
print drop_nth_element(['a','b','c','d','e','f','g','h','i','k'], 3)
print spilt_list(['a','b','c','d','e','f','g','h','i','k'], 3)