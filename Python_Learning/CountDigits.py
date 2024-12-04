def count_digits(N):
    if N == 0:
        return 1
    count = 0
    while N > 0:
        N //= 10
        count += 1
    return count    

T = int(input("TestCases: "))
for _ in range(T):
    N = int(input("CountOfDigits: ")) 
    print(count_digits(N))





    

