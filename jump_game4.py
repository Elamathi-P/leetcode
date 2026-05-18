class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        mp = {}
        for i in range(n):
            if arr[i] not in mp:
                mp[arr[i]] = []
            mp[arr[i]].append(i)
        q = [0]
        visited = [False] * n
        visited[0] = True
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                i = q.pop(0)
                if i == n - 1:
                    return steps
                for j in mp[arr[i]]:
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q.append(i - 1)
                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    q.append(i + 1)
                mp[arr[i]] = []
            steps += 1