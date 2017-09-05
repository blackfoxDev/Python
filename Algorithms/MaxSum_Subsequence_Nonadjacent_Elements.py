def find_max_sum_nonadjacent(a):
  if len(a) < 1:
    return 0
  elif(len(a) == 1):
    return a[0]

  lengthA = len(a)
  result = []
  result.append(a[0])
  for i in xrange(1, lengthA):
    result.append(max (a[i], result[i-1]))
    if i-2 >= 0 :
      result[i] = max (result[i], a[i] + result[i-2])
    
  return result[lengthA - 1];
