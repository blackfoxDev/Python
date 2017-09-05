def get_bit(num, bit):
      temp = (1 << bit)
  	temp = temp & num
  	if temp == 0:
    	return 0
  	return 1

def get_k_sum_subsets_1(v, target_sum, sets):
  	subsets_count = 2 ** len(v)
  	for i in xrange(0, subsets_count):
    	sum = 0
    	st = set([])
    	for j in xrange(0, len(v)):
      		if get_bit(i, j) == 1:
        		sum = sum + v[j]
        		if (sum > target_sum):
          			break
        	st.add(v[j])

    	if (sum == target_sum):
      		sets.append(st)
