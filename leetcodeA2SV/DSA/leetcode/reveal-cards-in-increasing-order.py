class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse= True)

        queue = deque()

        for card in deck:
            if queue:
                last = queue.pop()
                queue.appendleft(last)

            queue.appendleft(card)    
        

        return list(queue)