class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0])
        
        def fill(i, j):
            if i<0 or i >= m or j <0 or j>= n or image[i][j] != current or image[i][j] == color:
                return
            
            image[i][j] = color
            fill(i+1, j)
            fill(i-1, j)
            fill(i, j+1)
            fill(i, j-1)
        
        current = image[sr][sc]
        fill(sr, sc)
        return image