# Solution Using Two Pointer Approach
def DailyTemperatures(T):
    n = len(T)
    result = [0] * n

    for l in range(n):
        r = l + 1
        while r < n and T[r] < T[l]:
            r += 1

        if r < n:
            result[l] = r - l 

    return result






T = [73,74,75,71,69,72,76,73]
print(DailyTemperatures(T))