class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        """ 
        # bubble sort
        n = len(names)
       
        for i in range(n - 1):
         
            for j in range(n - i -1):
                if heights[j] < heights[j + 1]:
                    names[j], names[j + 1] = names[j + 1], names[j]
                    heights[j], heights[j + 1] =  heights[j + 1], heights[j]
                    
        
        # selection sort
        for i in range(len(names) - 1):
            max_idx = i
            for j in range(i + 1, len(names)):
                if heights[j] > heights[max_idx]:
                    max_idx = j
                    
            heights[max_idx], heights[i] = heights[i], heights[max_idx]
            names[max_idx], names[i] = names[i], names[max_idx]
       
        # insertion sort
      
        n = len(names)

        for i in range(1, n):
            name_key = names[i]
            height_key = heights[i]
            j = i - 1

            while j >= 0 and heights[j] < height_key:
                names[j + 1] = names[j]
                heights[j + 1] = heights[j]
                j -= 1

            names[j + 1] = name_key
            heights[j + 1] = height_key
    
        # counting sort
        maxim = max(heights) + 2
        new = []
        counting_array = defaultdict(list)
        for i in range(maxim):
            counting_array[i]
        for i, elem in enumerate(heights):
            counting_array[elem].append(names[i])
        for i in counting_array:
            if counting_array[i]:
                new += counting_array[i]
        new.reverse()
    
        return new

        """
        
        n = len(names)
        for i in range(n):
            m = heights[i]
            idx = i            
            for j in range(i + 1,n):
                if heights[j] > m:
                    m = heights[j]
                    idx = j
            
            heights[i], heights[idx] = heights[idx], heights[i]
            names[i], names[idx] = names[idx], names[i]

        return names
                
