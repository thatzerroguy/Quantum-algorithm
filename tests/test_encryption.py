import numpy as np
from lattice.sampling import sample_ternary, sample_error
from lattice.encryption import encrypt
from lattice.decryption import decrypt


def test_ring_lwe_encryption_decryption():
    """
    Tests whether encryption and decryption correctly recover the original message.
    """
    n, q = 256, 32768  # ✅ Increase q

    # Generate public and secret keys
    A = np.random.randint(0, q, size=n)
    s = sample_ternary(n)
    B = (np.polyval(A[::-1], s) + sample_error(n)) % q

    # Generate a random binary message
    m = np.random.randint(0, 2, size=n)

    # Encrypt the message
    C1, C2 = encrypt(A, B, m, n, q)  # ✅ Expect only 2 values

    # Decrypt the message
    decrypted_m = decrypt(C1, C2, s, q)

    print("Original message m:", m[:10])
    print("Decrypted message m:", decrypted_m[:10])

    # Check if decrypted message matches original
    assert np.array_equal(m, decrypted_m), "Decryption failed!"  # ✅ Compare directly with `m`
    print("Encryption & Decryption test passed! ✅")


if __name__ == "__main__":
    test_ring_lwe_encryption_decryption()
