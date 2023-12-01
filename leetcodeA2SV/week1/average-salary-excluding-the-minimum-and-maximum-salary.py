class Solution:
    def average(self, salary: List[int]) -> float:
        _min = float("inf")
        _max = float("-inf")

        running_sum = 0

        for i in salary:
            _min = min(_min, i)
            _max = max(_max, i)

            running_sum += i

        return (running_sum - _min - _max) / (len(salary) - 2)

