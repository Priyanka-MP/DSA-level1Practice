def minmaxFind(my_list):
    max_value = max(my_list)
    min_value = min(my_list)
    return(max_value, min_value)
my_list = [2,5,1,8,10,23,4,7]
N = len(my_list)
print(minmaxFind(my_list))
print("Number of elements in my_list: " ,N)

