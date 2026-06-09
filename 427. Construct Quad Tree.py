class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(size, startx,starty):
            #base condition
            leaf = True
            
            first_Val = grid[startx][starty]
            for i in range(size):
                for j in range(size):
                    if first_Val != grid[startx+i][starty+j]:
                        leaf = False
                        break;
                if not leaf:
                    break

            if leaf:
                return Node(first_Val, True, None, None,None,None)
          
            node = Node()
            node.isLeaf = leaf
            node.val = 1 if leaf else first_Val

            half = size//2 
            node.topLeft = dfs(half, startx,starty)
            node.topRight = dfs(half, startx,starty+half)
            node.bottomLeft = dfs(half, startx+half,starty)
            node.bottomRight = dfs(half, startx+half,starty+half)

            return node

        return dfs(n,0,0)
