class Solution:
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
      return None

    def connectTwoNodes(p, q) -> None:
      if not p:
        return
      p.next = q
      connectTwoNodes(p.left, p.right)
      connectTwoNodes(q.left, q.right)
      connectTwoNodes(p.right, q.left)

    connectTwoNodes(root.left, root.right)
    return root
