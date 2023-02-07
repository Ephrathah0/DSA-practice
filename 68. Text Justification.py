class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        dec = collections.deque()
        line = maxWidth
        a = 0
        for word in words:
            if len(dec)+a+len(word) <= maxWidth:
                dec.append(word)
                line -= len(word)
                a += len(word)
            else:
                cur = ''
                while dec:
                    spacing = line if len(dec) == 1 else int(ceil(line/(len(dec) - 1.0)))
                    cur += dec.popleft()
                    if line-spacing > 0:
                        cur += (' '*spacing)
                    elif line > 0:
                        cur += (' '*line)
                    line -= spacing
                res.append(cur)
                dec.append(word)
                line = (maxWidth-len(word))
                a = len(word)
        t = ''
        while dec:
            t += dec.popleft()
            if line:
                t += " "
                line -= 1

        if line: t += (' '*line)
        res.append(t)
        return res

