def is_prime(num):
    #num = int(input("Enter the num: "))
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # Found a divisor, not prime
    return True  # No divisors found, number is prime

def print_primes(N):
    for num in range(1, N + 1):
        if is_prime(num):
            print(num)  # Print each prime number on a new line

# Input the value of N
N = int(input("Enter the value of N: "))
print_primes(N)


