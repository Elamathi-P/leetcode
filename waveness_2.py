class Solution(object):
    def totalWaviness(self, num1, num2):

        def solve(n):
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            memo = {}

            def dp(pos, tight, started, prev2, prev1):
                key = (pos, tight, started, prev2, prev1)

                if key in memo:
                    return memo[key]

                if pos == len(digits):
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, ntight, False, -1, -1)

                    elif not started:
                        cnt, wav = dp(pos + 1, ntight, True, -1, d)

                    else:
                        add = 0

                        if prev2 != -1:
                            if ((prev1 > prev2 and prev1 > d) or
                                (prev1 < prev2 and prev1 < d)):
                                add = 1

                        cnt, wav = dp(pos + 1, ntight, True, prev1, d)
                        wav += add * cnt

                    total_cnt += cnt
                    total_wav += wav

                memo[key] = (total_cnt, total_wav)
                return memo[key]

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)