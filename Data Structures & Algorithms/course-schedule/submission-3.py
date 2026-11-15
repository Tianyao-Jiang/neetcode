class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        m = defaultdict(list)

        for c, pre in prerequisites:
            m[c].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if m[crs] == []:
                return True

            visited.add(crs)
            
            for pre in m[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)

            m[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

            