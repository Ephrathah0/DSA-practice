class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dp = [0 for _ in range(len(pressedKeys) + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(1, len(pressedKeys) + 1):
            dp[i] = dp[i - 1]
            if i >= 2 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                dp[i] += dp[i - 2]
            else:
                continue
            if i >= 3 and pressedKeys[i - 1] == pressedKeys[i - 3]:
                dp[i] += dp[i - 3]
            else:
                continue
            if i >= 4 and (pressedKeys[i - 1] == '7' or pressedKeys[i - 1] == '9') and pressedKeys[i - 1] == pressedKeys[i - 4]:
                dp[i] += dp[i - 4]
            else:
                continue
        return dp[len(pressedKeys)] % (10 ** 9 + 7)