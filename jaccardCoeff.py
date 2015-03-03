from __future__ import division
import itertools

def jaccard(s1, s2):
	""" takes two set as input and returns its Jaccards Coefficients """
	st1 = set(s1)
	st2 = set(s2)

	u = set(st1).union(st2)
	i = set(st1).intersection(st2)

	#print "union %s" %(u)
	#print "intersection %s" %(i)

	return len(i)/len(u)

if __name__ == "__main__":
	s = []
	s.append([1,2,3,4])
	s.append([2,3,5,7])
	s.append([2,4,6])
	s.append([8,9,10,11,12])

	print "input %s" %(s)

	combinations = list(itertools.combinations([x for x in range(len(s))], 2))

	for c in combinations:
		i1 = c[0]
		i2 = c[1]
		jac = jaccard(s[i1], s[i2])
		print "%s : %s,%s : jaccard=%s" %(c, s[i1], s[i2], jac)
	
	
