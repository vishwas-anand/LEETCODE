class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod=10**9+7
        c=0
        def solve(day):
            if day==1:
                return 1
            t=0
            for j in range(1, day):
                if j+delay<=day<=j+forget-1:
                    t+=solve(j)
            return t%mod

        for i in range(n-forget+1, n+1):
            c=(c+solve(i))%mod
        return c
        