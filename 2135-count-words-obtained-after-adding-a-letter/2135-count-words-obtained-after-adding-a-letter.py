class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        count = 0
        groups = set()

        for word in startWords:
            group = [0] * 26

            for c in word:
                group[ord(c) - ord('a')] += 1

            groups.add(tuple(group))

        for word in targetWords:

            exists = False

            for i in range(len(word)):

                newWord = word[:i] + word[i + 1:]
                group = [0] * 26

                for c in newWord:
                    group[ord(c) - ord('a')] += 1

                if tuple(group) in groups:
                    exists = True
                    break

            if exists:
                count += 1

        return count