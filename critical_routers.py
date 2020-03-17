from collections import defaultdict

class Solution:
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        
        disc = [None for _ in range(n+1)]
        low = [None for _ in range(n+1)]

        res = []
        self.cur = 0
        
        def dfs(node, parent):
            if disc[node] is None:
                disc[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for n in graph[node]:
                    if disc[n] is None:
                        dfs(n, node)
                if parent is not None:
                    l = min([low[i] for i in graph[node] if i!=parent]+[low[node]])
                else:
                    l = min(low[i] for i in graph[node]+[low[node]])
                low[node] = l
        
        dfs(1, None)
        
        for v in connections:
            if low[v[0]] > disc[v[1]] or low[v[1]] > disc[v[0]]:
                res.append(v)
        
        return res
solution = Solution()
print(solution.criticalConnections(7, [[1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4,5]]))
    
        
# [[1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4,5]]