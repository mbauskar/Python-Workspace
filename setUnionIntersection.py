def getUnion(s): 
	""" return a union from a set of lists """
	u = set()
	for x in s:
		u = u | set(x)
	return u

def getIntersection(s):
	""" returns a intersection from a set of lists """
	i = set(s[0])
	for x in s[1:]:
		i = i & set(x)
	return i

if __name__ == "__main__":
	s = []
	s.append([1,2,3,4])
	s.append([2,3,5,7])
	s.append([2,4,6])

	u = getUnion(s)
	i = getIntersection(s)
	
	print "input %s" %(s)
	print "size of input %d" %(len(s))
	
	print "union %s size %d" %(u, len(u))
	print "intersection %s size %d" %(i, len(u))

