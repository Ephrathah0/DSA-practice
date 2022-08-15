class Solution(object):
	def __init__(self):
		self.result = []

	def helper(self, candidates, target,op=[],index = 0):
		if index>=len(candidates):

			if target==0:
				self.result.append(op[::])
			return
		if candidates[index]<=target:
			op.append(candidates[index])
			self.helper(candidates, target-candidates[index],op,index)
			op.pop()
		self.helper(candidates, target,op,index+1)


	def combinationSum(self, candidates, target,op=[],index = 0):
		
		self.helper(candidates,target)
		return self.result