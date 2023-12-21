class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m_int = float('-inf')
        for i in range(len(num)-2):
            window = num[i:i+3]
            for j in window:
                if j != window[0]:
                    break
            else:
                m_int = max(int(window), m_int)

        if m_int == 0:
            return "000"

        return "" if m_int == float('-inf') else str(m_int)

        
