class ATM:

    def __init__(self):
        self.current_notes = [0] * 5
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotes_count: List[int]) -> None:
        for i, n in enumerate(banknotes_count):
            self.current_notes[i] += n

    def withdraw(self, amount: int) -> List[int]:
        res = []
        for val, n in zip(self.values[::-1], self.current_notes[::-1]):
            need = min(n, amount // val)
            res = [need] + res
            amount -= (need * val)
        if amount == 0:
            self.deposit([-x for x in res])
            return res
        else:
            return [-1]
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)


