class Solution:
    def smallestNumber(self, num: int) -> int:
        
        new = []
        for i in str(num):
            new.append(i)
        l = len(new)
        #print(new)

        if int(num) >=0: 
        
            for i in range(len(new)):
                for j in range(len(new) -i -1):
                    if new[j] + new[j+1] > new[j+1] + new[j]:
                        new[j], new[j+1] = new[j+1], new[j]

                k = 0
                while k < l and new[k] == "0" :
                    k += 1
                if l > 1:
                    new = new[k:k+1] + new[:k] + new[k+1:]

        else:
            new = new[1:]
            for i in range(len(new)):
                for j in range(len(new) -i -1):
                    # print(new[j] + new[j+1] , new[j+1] + new[j])
                    if new[j] + new[j+1] < new[j+1] + new[j]:
                        new[j], new[j+1] = new[j+1], new[j]


            

        return int("".join(new)) if num > 0 else -1 * int("".join(new))