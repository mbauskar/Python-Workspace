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
	if element_list and len(element_list) > 2:
		lastest = element_list[0]
		result.append(lastest)
		for element in element_list[1:]:
			if element != lastest:
				lastest = element
				result.append(lastest)
	elif len(element_list) == 2:
		return list(set(element_list))
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