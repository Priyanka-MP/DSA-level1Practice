def inverted_pyramid(N):
    for i in range(N, 0, -1):
        for j in range(1, i+1):
            if j > 1:
                print(" ", end= " ")
            print(j, end= " ")
        print()  
print(inverted_pyramid(4))              