def numeric_stair_pattern(N):
    for i in range(1,N +1):
        for j in range(1, i+1):
            if j == i:
                print(j, end = " ")
            else:
                print(j, end = " ")
        print()
print(numeric_stair_pattern(5))                    
    
