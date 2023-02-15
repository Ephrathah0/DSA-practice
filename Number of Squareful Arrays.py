class Solution(object):
    def numSquarefulPerms(self, A: List[int]) -> int:
        def rec(i, x):
            if i>1:
                curr = x[i-2] + x[i-1]
                sqr = math.sqrt(curr) == math.floor(math.sqrt(curr))
                if not sqr:
                    return
            if i == len(x):
                res.append(x)
                return
            for j in range(i, len(x)):
                x[i], x[j] = x[j], x[i]
                search = (i, x[i], tuple(x[:i]))
                if search not in sett:
                    sett.add(search)
                    rec(i+1, x)
                x[i], x[j] = x[j], x[i]

        res = []
        sett = set()
        rec(0, A)
        return len(res)
