# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

	def __init__(self, root: Optional[TreeNode]):
		self.root = root
		self.store = []
		self.inOrderTraversal(root, self.store)

		self.pointer =0

	def inOrderTraversal(self, root, store):
		if not root:
			return

		self.inOrderTraversal(root.left, store)
		store.append(root.val)
		self.inOrderTraversal(root.right, store)

	def next(self) -> int:
		val = self.store[self.pointer]
		self.pointer +=1
		return val

	def hasNext(self) -> bool:
		if self.pointer < len(self.store):
			return True

		return False