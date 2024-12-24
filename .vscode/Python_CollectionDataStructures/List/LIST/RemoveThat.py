def remove_that(lst, x):
    if 1 <= x <= len(lst):
        lst.pop( x - 1)
    return lst    
"""
  Logic for if stmt : checks the range that x value doesnt exceed outside from the lst
  lst.pop (x -1) works as O based index in python whereas if 
          x = 3, then 
          x-1 = 3-1 = 2, that removes 2nd index element in the list which is 30
"""  
A = [10,20,30,40,50]
X = 0
#Note: For x = 0, the condition 1 <= x fails, so the lst.pop() operation is not executed.
updated_list = remove_that(A,X)
print(" ".join(map(str, updated_list)) + " ")
#map == converts the integer element to string such as "10,20,30,40,50"
#.join == joins the strings such as '10','20','30','40','50'
# +" " == adds trailing space at the end such as [ '10','20','30','40','50' ]

    