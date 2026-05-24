class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [0] * n

        def dfs(i):
            if dp[i]:
                return dp[i]

            ans = 1

            # right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))

            # left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))

            dp[i] = ans
            return ans

        res = 0
        for i in range(n):
            res = max(res, dfs(i))

        return res 