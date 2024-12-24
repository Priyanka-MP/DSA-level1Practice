def product_of_elements(ArrayList):
    product = 1
    #formula/logic for initializing product value
    for num in ArrayList:
        product *= num
    return(product)
ArrayList = [2,4,1,3]
"""
Iteration 1:
num in ArrayList = 2
product = product * num
        = 1 * 2
:.updated product value = 2
Then iteration 2 with num = 4,product =2,..
""" 
print(product_of_elements(ArrayList))