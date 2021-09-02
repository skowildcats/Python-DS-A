def deleteNode(self, node):
  node.val = node.next.val
  node.next = node.next.next

# Time complexity: O(1)
# Space complexity: O(1)

# Recognizing that deleting a node does not necessarily mean removing it from memory
# Copying the next node and changing the reference essentially "deletes" it
