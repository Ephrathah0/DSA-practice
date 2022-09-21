class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def canConstract(target,words):
            if target in memo : return memo[target]
            if len(target) == 0 : return True

            for word in words :
                if target[0:len(word)] == word :
                    memo[target] = canConstract(target[len(word):],words)
                    if memo[target]:
                        return True
                elif target[-len(word):] == word :
                    memo[target] = canConstract(target[0:len(target)-len(word)],words)
                    if memo[target]:
                        return True

            memo[target] = False
            return memo[target]
        
        return canConstract(s,wordDict)