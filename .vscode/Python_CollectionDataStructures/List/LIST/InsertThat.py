def InsertElement(Num,Array,Xposition,Yelement):
    Array.insert(Xposition - 1, Yelement)
    return Array

Num = 5
Array = [1,2,3,4,5]
Xposition = 3
Yelement = 3
print(InsertElement(Num,Array,Xposition,Yelement))

