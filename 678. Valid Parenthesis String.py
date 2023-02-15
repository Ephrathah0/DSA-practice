class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((s[i], i))
            elif s[i] == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((s[i], i))
            else:
                stars.append(i)
        if not stack:
            return True
        else:
            for i in range(len(stack)):
                if stack[i][0] == "(":
                    index = bisect.bisect_left(stars, stack[i][1])
                    if index >= len(stars):
                        return False
                    stars.pop(index)
                elif stack[i][0] == ")":
                    index = bisect.bisect_left(stars, stack[i][1])
                    if index-1 >= 0:
                        stars.pop(index-1)
                    else:
                        return False
                else:
                    return False
        return True
