from typing import List

def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for i in range(len(image)):
        image[i].reverse()
        for j in range(len(image[i])):
            if image[i][j] == 0:
                image[i][j] = 1
            elif image[i][j] == 1:
                image[i][j] = 0
    return image




print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))