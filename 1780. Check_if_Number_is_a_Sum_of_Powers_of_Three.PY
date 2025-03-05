def check_number(n):
    while (n):
        if n % 3 == 2:
            return False
        
        n //= 3
    return True




n = 21
print(check_number(n))
