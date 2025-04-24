class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def mod_pow(x, n):
            x %= MOD
            if n == 0:
                return 1
            half = mod_pow(x, n // 2)
            result = (half * half) % MOD
            if n % 2 == 1:
                return (result * x) % MOD
            return result
        
        result = 1
        for digit in b:
            result = (mod_pow(result, 10) * mod_pow(a, digit)) % MOD

        return result