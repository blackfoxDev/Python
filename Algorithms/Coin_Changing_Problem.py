def solve_coin_change_dp(denominations, amount):
  # this solution requires O(amount) space to store solution
  # until current amount.
  solution = array('i',(0 for i in range(0, amount + 1)))
  solution[0] = 1;
  for den in denominations:
    for i in xrange(den, amount + 1):
      solution[i] += solution[i - den] 

  return solution[len(solution) - 1]
