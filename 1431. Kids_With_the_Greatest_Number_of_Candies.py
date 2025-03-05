from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:

    result = []
    maxCandies = max(candies)
    for i in range(len(candies)):
        if int(candies[i]) + extraCandies >= maxCandies:
            result.append(True)
        else:
            result.append(False)

    return result


candies = [2,3,5,1,3]
extraCandies = 3 
print(kidsWithCandies(candies, extraCandies))