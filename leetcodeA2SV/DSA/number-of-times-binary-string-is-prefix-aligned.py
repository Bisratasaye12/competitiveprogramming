class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        m_flipped_idx = -1
        j = 0
        count = 0
        for i in flips:
            j += 1
            m_flipped_idx = max(i, m_flipped_idx)
            if m_flipped_idx == j:
                count += 1


        return count