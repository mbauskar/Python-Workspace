input = [{'a':50, 'b':5}, {'c':21}, {'a':2, 'b':3}]
result = {}
[{result.update({key:(result.get(key, 0) + val)}) \
for key, val in _dict.iteritems()} for _dict in input]
print result

