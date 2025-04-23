import numpy as np
from lattice.polynomial import Polynomial
from lattice.ring_lwe import RingLWE
from lattice.utils import encode_message, decode_message, generate_parameters


def main():
    # Initialize with standard RLWE parameters
    params = generate_parameters(n=256, q=12289)
    rlwe = RingLWE(params['n'], params['q'], params['sigma'])

    # Generate keys
    public_key, secret_key = rlwe.generate_keys()

    # Encrypt message
    message = b"Hello Quantum World!"
    original_length = len(message)

    # Encode message
    encoded = encode_message(message, params['n'], params['q'])
    encoded_poly = Polynomial(encoded, params['n'], params['q'])

    # Encrypt
    ciphertext = rlwe.encrypt(public_key, encoded_poly)

    # Return encrypted message first ten elements
    print("Encrypted message after encoding and encryption:")
    print(ciphertext[0].coeffs[:10], ciphertext[1].coeffs[:10])

    # Decrypt
    decrypted_poly = rlwe.decrypt(secret_key, ciphertext)
    decrypted = decode_message(decrypted_poly.coeffs, params['q'], original_length)

    print(f"Original: {message}")
    print(f"Decrypted: {decrypted}")


if __name__ == "__main__":
    main()