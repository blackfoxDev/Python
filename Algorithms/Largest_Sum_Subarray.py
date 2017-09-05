def find_max_sum_sub_array(A):
  if len(A) < 1:
    return 0

  curr_max = A[0]
  global_max = A[0]
  lengthA = len(A)
  for i in xrange(1, lengthA):
    if curr_max < 0:
      curr_max = A[i]
    else:
      curr_max += A[i]

    if global_max < curr_max:
      global_max = curr_max

  return global_max
