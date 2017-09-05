# this method determines if a queen can
# be placed at proposed_row, proposed_col
# with current solution i.e. this move 
# is valid only if no queen in current 
# solution should attacked square at
# proposed_row and proposed_col
def is_valid_move(
    proposed_row,
    proposed_col,
    solution):

  # we need to check with all queens
  # in current solution
  for i in xrange(0, proposed_row):
    old_row = i
    old_col = solution[i]

    diagonal_offset = proposed_row - old_row
    if (old_col == proposed_col or 
         old_col == proposed_col - diagonal_offset or 
         old_col == proposed_col + diagonal_offset):
      return False

  return True

def solve_n_queens_rec(n, solution, row, results):
  if row == n:
    results.append(copy.deepcopy(solution))
    return

  for i in xrange(0, n):    
    if is_valid_move(row, i, solution):
      solution[row] = i
      solve_n_queens_rec(n, solution, row + 1, results)

def solve_n_queens(n, results):
  solution = [-1, -1, -1, -1, -1, -1, -1, -1]
  solve_n_queens_rec(n, solution, 0, results)
