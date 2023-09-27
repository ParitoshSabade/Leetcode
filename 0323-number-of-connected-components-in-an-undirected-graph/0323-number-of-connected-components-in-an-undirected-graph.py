class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Convert to Adj List
        adj_list = {}
        for x, y in edges:
            if x not in adj_list:
                adj_list[x] = [y]
            else:
                adj_list[x].append(y)
                
            if y not in adj_list:
                adj_list[y] = [x]
            else:
                adj_list[y].append(x)
                
            
        
        def DFS(node,component):
            visited.append(node)
            component.append(node)
            if adj_list[node]:
                for nbors in adj_list[node]:
                    if nbors not in visited:
                        DFS(nbors,component)
        visited = []
        component = []
        cnt = 0               
        for v in adj_list:
            component.clear()
            if v not in visited:
                DFS(v,component)
            
            if component:
                cnt+=1;
                
        isolated = n - len(adj_list.keys())
                
        return cnt+isolated
            
        
                
            
            
        