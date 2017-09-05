let populate_sibling_pointers_1 = function(root) {
  if (!root) {
    return;
  }

  let current = root;
  let last = root;

  while (current) {
    if (current.left) {
      last.next = current.left;
      last = current.left;
    }
    if (current.right) {
      last.next = current.right;
      last = current.right;
    }
    last.next = null;
    current = current.next;
  }
};
