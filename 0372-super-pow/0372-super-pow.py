class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def mod_pow(x, n):
            x %= MOD
            result = 1
            while n:
                if n % 2 == 1:
                    result = (x * result) % MOD
                x = (x * x) % MOD
                n = n // 2
            return result
        
        result = 1
        for digit in b:
            result = (mod_pow(result, 10) * mod_pow(a, digit)) % MOD

        return result