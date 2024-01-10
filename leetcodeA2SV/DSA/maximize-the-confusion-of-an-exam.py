class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        l, r= 0, 0
        t_count, f_count = 0, 0
        m_count = 0

        while r < n:
            if answerKey[r] == "T":
                t_count += 1
            else:
                f_count += 1

            if min(t_count, f_count) > k:
                m_count = max(m_count, r-l)
                if answerKey[l] == "T":
                    t_count -= 1
                else:
                    f_count -= 1
                l += 1

            r += 1
        m_count = max(m_count, r-l)

        return m_count

            
