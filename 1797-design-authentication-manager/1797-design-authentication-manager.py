class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.life = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime+self.life

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.life

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0
        for i in self.tokens:
            if self.tokens[i] > currentTime:
                ans+=1
        return ans