def print_list(l):
  for c in l:
    print c,
  print

def print_all_parentheses_rec(
    n, left_count, right_count, output):

  if left_count >= n and right_count >= n:
    print_list(output)

  if left_count < n:
    output += '{'
    print_all_parentheses_rec(
      n, left_count + 1, right_count, output)
    output.pop()

  if right_count < left_count:
    output += '}'
    print_all_parentheses_rec(
      n, left_count, right_count + 1, output)
    output.pop()

def print_all_parentheses(n):
  output = []
  print_all_parentheses_rec(n, 0, 0, output)

def main():
  print_all_parentheses(3)
