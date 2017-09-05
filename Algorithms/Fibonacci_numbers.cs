def get_fibonacci_rec(n):

  if n == 0 or n == 1:
    return n

  return get_fibonacci_rec(n-1) + get_fibonacci_rec(n-2)
