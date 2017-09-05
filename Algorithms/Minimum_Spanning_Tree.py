# This method finds the MST of a graph using
# Prim's Algorithm
# returns the weight of the MST
def find_min_spanning_tree(self):
  vertex_count = 0
  weight = 0

  # Add first vertex to the MST
  current = self.g[0]
  current.visited = True
  vertex_count += 1

  # Construct the remaining MST using the
  # smallest weight edge
  while vertex_count < len(self.g):
    smallest = None
    for i in range(len(self.e)):
      if self.e[i].visited == False and self.e[i].dest.visited == False:
        smallest = self.e[i]
        break
        
    for i in range(len(self.e)):
      if self.e[i].visited == False:
        if self.e[i].src.visited == True and self.e[i].dest.visited == False and self.e[i].weight < smallest.weight:
          smallest = self.e[i]

    smallest.visited = True
    smallest.dest.visited = True
    weight += smallest.weight
    vertex_count += 1
      
  return weight
