#February 4 2025
# https://leetcode.com/problems/subdomain-visit-count/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        top = {}
        middle = {}
        bottom = {}
        for c in cpdomains:
            count, domain = c.split(" ")
            domain = domain.split(".")
            count = int(count)
            d2 = domain[-2] + '.' + domain[-1]

            top[domain[-1]] = top.get(domain[-1],0) + count

            middle[d2] = middle.get(d2,0) + count

            if len(domain) == 3:
                d3 = '.'.join(domain)
                bottom[d3] = bottom.get(d3,0) + count
        for t in top:
            res.append(f"{str(top[t])} {t}")
        for t in bottom:
            res.append(f"{str(bottom[t])} {t}")
        for t in middle:
            res.append(f"{str(middle[t])} {t}")
        return res