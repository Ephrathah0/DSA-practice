class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def make_signature(n: int):
            if n == 0:
                return 0
            leading, remaining = divmod(n, 10)
            return make_signature(leading) + ( 10 ** remaining )
        signature_of_N = make_signature(N)
        for i in range(32):
            if make_signature( 1 << i ) == signature_of_N:
                return True
        return False
