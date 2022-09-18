class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        lookup = {}
        
        N = len(accounts)
        parent = list(range(N))
        rank = [1] * N
        
        def ufind(x):
            if x != parent[x]:
                parent[x] = ufind(parent[x])
            return parent[x]
        
        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)
            if rank[ua] < rank[ub]:
                ua, ub = ub, ua
            rank[ua] += rank[ub]
            parent[ub] = ua
        
        for idx, account in enumerate(accounts):
            name, *emails = account
            for email in emails:
                if email not in lookup:
                    lookup[email] = idx
                else:
                    uunion(lookup[email], idx)
              
        emailsList = defaultdict(set)
        for idx, account in enumerate(accounts):
            name, *emails = account
            for email in emails:
                emailsList[ufind(idx)].add(email)
                
        ans = []
        for idx in range(N):
            if ufind(idx) == idx:
                ans.append([accounts[idx][0]] + list(sorted(emailsList[idx])))
        return ans