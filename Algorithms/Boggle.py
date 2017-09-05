class Boggle:
  #code assumes that both dimensions of grid are same
  def __init__(self, grid, dictionary):
    self.grid = grid
    self.dictionary = dictionary
    self.state = [[False for x in xrange(len(grid))] \
                  for y in xrange(len(grid))]

  def find_all_nbrs(self, x, y): 
    nbrs = []
    for i in xrange(max(0, x - 1), min(x + 2, len(self.grid))):
      for j in xrange(max(0, y - 1), min(y + 2, len(self.grid))):
        if i == x and j == y:
          continue          
        if self.state[i][j] == False:
          nbrs.append([i, j])
    return nbrs

  def find_words_rec(self, i, j, current, words):    
    if len(current) > 0 and (current in self.dictionary):
      words.add(current)

    # we can really speed up our algorithm if we have prefix method available
    # for our dictionary by using code like below
    
    #if not dictionary.is_prefix(current):
    #  // if current word is not prefix of any word in dictionary
    #  // we don't need to continue with search
    #  return

    nbrs = self.find_all_nbrs(i, j)
    for pr in nbrs:  
      first = pr[0]
      second = pr[1]  
      current += self.grid[first][second]
      self.state[first][second] = True
      self.find_words_rec(first, second, current, words)
      current = current[:-1] #equivalent to current = current[0:len(current) - 1]
      self.state[first][second] = False

  def find_all_words(self):
    words = set([])
    for i in xrange(0, len(self.grid)):
      for j in xrange(0, len(self.grid)):
        current_word = ""
        self.find_words_rec(i, j, current_word, words)
    return words
