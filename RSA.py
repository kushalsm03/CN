def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modular_exponentiation(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result

def rsa_encrypt_decrypt():
    # Input message
    message = input("Enter the message to encrypt: ").strip()
    
    # Input prime numbers
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    
    # Calculate n, phi(n), e, and d
    n = p * q
    phi = (p - 1) * (q - 1)
    e = next(i for i in range(2, phi) if gcd(i, phi) == 1)
    d = next(i for i in range(2, phi) if (e * i) % phi == 1)

    # Encrypt the message
    encrypted = [modular_exponentiation(ord(ch) - 96, e, n) for ch in message]

    # Decrypt the message
    decrypted = ''.join(chr(modular_exponentiation(val, d, n) + 96) for val in encrypted)

    # Output results
    print("Encrypted message:", ' '.join(map(str, encrypted)))
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    rsa_encrypt_decrypt()
