class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = defaultdict(list)
        ret = []
        for folder in paths:
            f = folder.strip().split()
            head = f[0]
            for file in f[1:]:
                u, comp = file.split("(")
                q = head + "/" + u
                files[comp].append(q)
                
        for i in files:
            if len(files[i]) >= 2:
                ret.append(files[i])
      
        return ret
