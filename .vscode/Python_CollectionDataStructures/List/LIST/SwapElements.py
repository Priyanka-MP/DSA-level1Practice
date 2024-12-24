def swapElements(my_list):
    my_list[1],my_list[5] = my_list[5],my_list[1]
    return my_list

my_list = [1,2,3,4,5,6]
print(swapElements(my_list))
"""
Swapping:

The line n_list[1], n_list[3] = n_list[3], n_list[1] swaps the values at these indices using tuple unpacking.
"""