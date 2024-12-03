from diffie_hellman import generate_prime, find_primitive_root, calculate_public_key, calculate_shared_secret
import random

def main():
    # Both the persons will be agreed upon the common prime number p and base g
    p = generate_prime()
    g = find_primitive_root(p)

    print(f"Using prime: {p} and primitive root: {g}")

    # Alice's private and public keys
    a_private = random.randint(2, 100)
    A_public = calculate_public_key(g, a_private, p)

    # Bob's private and public keys
    b_private = random.randint(2, 100)
    B_public = calculate_public_key(g, b_private, p)

    # Secret keys calculated by both
    alice_secret = calculate_shared_secret(B_public, a_private, p)
    bob_secret = calculate_shared_secret(A_public, b_private, p)

    print(f"Alice's Secret: {alice_secret}")
    print(f"Bob's Secret: {bob_secret}")

    assert alice_secret == bob_secret
    print("Shared secret confirmed.")

if __name__ == "__main__":
    main()