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
		lastest = element_list[0]
		result.append(lastest)
		for element in element_list[1:]:
			if element != lastest:
				lastest = element
				result.append(lastest)
	else:
		return list(set(element_list))
	return result

def pack_duplicates(element_list):
	result = []
	if element_list and len(element_list) > 2:
		lastest = element_list[0]
		pack = []
		for element in element_list[1:]:
			pack.append(lastest)
			if element != lastest:
				result.append(pack)
				lastest = element
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
		lastest = element_list[0]
		pack = [lastest]
		for element in element_list[1:]:
			if element != lastest:
				lastest = element
				result.append(pack)
				pack = [lastest]
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
	if element_list and len(element_list) > 2:
		lastest = element_list[0]
		count = 1
		pack = []
		for element in element_list[1:]:
			if element != lastest:
				result.append([lastest, count])
				lastest = element
				count = 1
			else:
				count += 1
		result.append([lastest, count])
	return result


element_list = ['a','b','c','d']
duplicates = [1,1,1,1,1,1,2,2,2,1,1,3,3,4,4,4,4,4,4,4]
list_tobe_flatten = [1,[2,[3,4],5],6]

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