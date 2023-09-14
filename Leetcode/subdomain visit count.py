class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        res = []
        for cpd in cpdomains:
            count, dom = cpd.strip().split()
            domains = dom.split(".")
            if len(domains) == 3:
                f, sec = dom.split(".", 1)
                counter[domains[-1]] += int(count)
                counter[dom] += int(count)
                counter[sec] += int(count)
            else:
                counter[dom] += int(count)
                f, sec = dom.split(".")
                counter[sec] += int(count)
                
        for i in counter:
            a = str(counter[i]) + " " + i
            res.append(a)
            
        return res
                
                
