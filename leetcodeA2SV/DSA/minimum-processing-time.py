class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse= True)
        processorTime.sort()
        j = 0
        m = 0
        for i in range(0,len(tasks),4): 
            # We map the processor that started at an earlier time with task of length higher
            # since the task is sorted in reverse the first max number of time for the first
            # processor will be at index 0 then for the second at 4 ..etc

            m = max(m, (tasks[i] + processorTime[j]))
            j += 1
            
        return m


