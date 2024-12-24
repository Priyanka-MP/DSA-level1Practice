def CheckOccurences(Array,B):
    count = 0
    for num in Array:
        if num == B:
            count += 1
    return count
Array = [2,1,3,1,5,6,1,7,8,1]
B = 1
print(CheckOccurences(Array,B))
        