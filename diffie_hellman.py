import random 
from sympy import isprime

def generate_prime():
    """Generates a large prime number."""
    while True:
        num = random.randint(10000, 100000)  # Adjust range for better primes
        if isprime(num):
            return num

def find_primitive_root(p):
    """Finds a primitive root for prime p."""
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1

    # Check for all the numbers between 2 and p-1
    for g in range(2, p):
        if (pow(g, (p - 1) // p1, p) != 1 and
            pow(g, (p - 1) // p2, p) != 1):
            return g
    return -1    
    
        
def calculate_public_key(base, private_key, p):
    """Calculates a public key."""
    return pow(base, private_key, p)

def calculate_shared_secret(public_key, private_key, p):
    """Calculates the shared secret."""
    return pow(public_key, private_key, p)
