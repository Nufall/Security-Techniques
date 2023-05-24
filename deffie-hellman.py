import random

def generate_prime_number():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return random.choice(primes)

def generate_primitive_root(prime):
    primitive_roots = [2, 3, 5]
    primitive_root = random.choice(primitive_roots)
    while pow(primitive_root, (prime-1)//2, prime) == 1:
        primitive_root = random.choice(primitive_roots)
    return primitive_root

def generate_private_key(prime):
    return random.randint(2, prime-2)

def generate_public_key(prime, primitive_root, private_key):
    return pow(primitive_root, private_key, prime)

def generate_shared_secret(prime, public_key, private_key):
    return pow(public_key, private_key, prime)

# Generate prime number and primitive root
prime = generate_prime_number()
primitive_root = generate_primitive_root(prime)

# Generate private and public keys for both parties
private_key_A = generate_private_key(prime)
public_key_A = generate_public_key(prime, primitive_root, private_key_A)

private_key_B = generate_private_key(prime)
public_key_B = generate_public_key(prime, primitive_root, private_key_B)

# Generate shared secrets
shared_secret_A = generate_shared_secret(prime, public_key_B, private_key_A)
shared_secret_B = generate_shared_secret(prime, public_key_A, private_key_B)

# Verify that shared secrets match
print("Shared secrets match:", shared_secret_A == shared_secret_B)
print("Shared secret:", shared_secret_A)
