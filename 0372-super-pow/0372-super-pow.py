class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def mod_pow(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                half = mod_pow(x, n // 2)
                return (half * half) % MOD
            else:
                half = mod_pow(x, n // 2)
                return (half * half * x) % MOD
        
        result = 1
        for digit in b:
            result = (mod_pow(result, 10) * mod_pow(a, digit)) % MOD

        return result