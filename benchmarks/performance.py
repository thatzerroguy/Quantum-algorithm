import time
import numpy as np
from lattice.polynomial import Polynomial
from lattice.ring_lwe import RingLWE
from lattice.utils import generate_parameters


def benchmark(iterations=100):
    params = generate_parameters(n=256, q=12289)
    rlwe = RingLWE(**params)

    times = {'keygen': [], 'encrypt': [], 'decrypt': []}

    for _ in range(iterations):
        # Keygen
        start = time.time()
        pk, sk = rlwe.generate_keys()
        times['keygen'].append(time.time() - start)

        # Encrypt
        message = Polynomial.random(256, 12289)
        start = time.time()
        ciphertext = rlwe.encrypt(pk, message)
        times['encrypt'].append(time.time() - start)

        # Decrypt
        start = time.time()
        _ = rlwe.decrypt(sk, ciphertext)
        times['decrypt'].append(time.time() - start)

    print(f"Average KeyGen: {np.mean(times['keygen']) * 1000:.2f}ms")
    print(f"Average Encrypt: {np.mean(times['encrypt']) * 1000:.2f}ms")
    print(f"Average Decrypt: {np.mean(times['decrypt']) * 1000:.2f}ms")

if __name__ == "__main__":
    benchmark()