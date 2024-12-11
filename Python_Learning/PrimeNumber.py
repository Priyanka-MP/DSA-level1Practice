A = int(input("enter number: "))
if A <= 1:
    print("Oops, I m not Prime number")
else:    
    for i in range(2,A):
        if A % i == 0:
            print("No!I m not a Prime")
        break
    else:
        print("Yes you find me!!Prime here ")          

   
   
