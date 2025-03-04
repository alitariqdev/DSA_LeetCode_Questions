# Solution Using Two Pointer Approach
def Daily_Temperatures_Two_Pointers_Approach(T):
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
print(Daily_Temperatures_Two_Pointers_Approach(T))




# Solution Using Monotonic Stack 

def dailyTemperatures(T):
        s = []
        r = [0] * len(T)

        for i in range (len(T)):
            while s and T[i] > T[s[-1]]:
                index = s.pop()
                r[index] = i - index
            s.append(i)
        
        return r


print(dailyTemperatures(T))
