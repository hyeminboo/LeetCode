from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges) == 0:
            return True

        flag1 = [x for x in edges if x[0] == destination and x[1] == source]
        flag2 = [x for x in edges if x[0] == source and x[1] == destination]
        if len(flag1) > 0 or len(flag2) > 0:
            return True

        d = defaultdict(list)

        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
        
        used = []

        def find(val):
            used.append(val)
            if destination in d[val]:
                return True

            for i in d[val]:
                if i not in used and i in d.keys():
                    if find(i):
                        return True
            return False

        return find(source)
    
        return False