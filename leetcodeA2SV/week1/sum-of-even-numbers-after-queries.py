class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        put a running sum of even integers from the nums

        traverse queries and for each traversal
            check if nums[i] is even:
                subtract the nums[i] from the running sum
                and add nums[i] + val if it's "even"
                append running sum to answer array
            odd:
                add nums[i] + val to runningsum if it's even
                append running sum to answer
        """
        running_sum, answer = 0, []

        for i in nums:
            if i%2 == 0:
                running_sum += i


        for query in queries:
            val, idx = query[0], query[1]
            if nums[idx] % 2 == 0:
                running_sum -= nums[idx]
            
            if (nums[idx] + val) % 2 == 0:
                running_sum += nums[idx] + val
            nums[idx] += val
              
            answer.append(running_sum)
          
        return answer

        