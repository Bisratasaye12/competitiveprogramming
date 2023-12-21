class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        m_ghost_step = float('inf')
        my_step = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            ghost_step = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            m_ghost_step = min(m_ghost_step, ghost_step)



        return True if my_step < m_ghost_step else False