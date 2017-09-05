def connect_next_level(head):
  current = head
  next_level_head = None
  prev = None

  while current != None:
    if current.left != None \
    and current.right != None:
      if next_level_head == None:
        next_level_head = current.left
        
      current.left.next = current.right
      
      if prev != None:
        prev.next = current.left
        
      prev = current.right
    elif current.left != None:
      if next_level_head == None:
        next_level_head = current.left

      if prev != None:
        prev.next = current.left

      prev = current.left  
    elif current.right != None:
      if next_level_head == None:
        next_level_head = current.right

      if prev != None:
        prev.next = current.right

      prev = current.right

    current = current.next

  if prev != None:
    prev.next = None

  return next_level_head

def populate_sibling_pointers(root):

  if root == None:
    return

  root.next = None
  
  while root != None:
    root = connect_next_level(root)
