def reverseFunction(n,temp=" "):
    """
    Reverse a number n = 123 into 321 using recursive fn call and temp to store variables
    """
    
    if n == 0:
        return temp
    
    lastNum = n  % 10
    newNum = n // 10
    temp += str(lastNum)
    return reverseFunction(newNum, temp)
n = int(input("Enter the number to be reversed:  "))
print(reverseFunction(n))
