class Solution:
    def numberOfMatches(self, n: int) -> int:
        m = 0
        advance = n

        while advance != 1:

            if advance % 2 == 0:
                m += (advance/2)
                advance = advance / 2
            else:
                m += ((advance - 1) /2 )
                advance = (advance-1)/2 + 1

        return int(m)
