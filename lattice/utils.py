import numpy as np
import math
from typing import Tuple, List


class NTT:
    """
    Number Theoretic Transform (NTT) implementation for polynomial multiplication
    in ring Z_q[x]/(x^n + 1) where q ≡ 1 mod 2n
    """

    def __init__(self, n: int, q: int):
        if not self.is_valid_ntt_parameters(n, q):
            raise ValueError("Invalid NTT parameters: q must be prime and q ≡ 1 mod 2n")

        self.n = n
        self.q = q
        self.psi, self.psi_inv = self.find_primitive_roots()
        self.ntt_table, self.intt_table = self.precompute_ntt_tables()

    def is_valid_ntt_parameters(self, n: int, q: int) -> bool:
        """Check if parameters support NTT"""
        if q < 2 or any(q % i == 0 for i in range(2, int(math.sqrt(q)) + 1)):
            return False
        return (q - 1) % (2 * n) == 0

    def find_primitive_roots(self) -> Tuple[int, int]:
        """Find primitive 2n-th roots of unity modulo q"""
        for psi in range(2, self.q):
            if pow(psi, self.n, self.q) == self.q - 1:  # Ensure psi^n ≡ -1 mod q
                psi_inv = pow(psi, -1, self.q)
                return psi, psi_inv
        raise ValueError("No primitive root found")

    def precompute_ntt_tables(self) -> Tuple[List[int], List[int]]:
        """Precompute NTT and INTT twiddle factors"""
        n, q, psi = self.n, self.q, self.psi
        ntt_table = [pow(psi, i, q) for i in range(n)]
        intt_table = [pow(self.psi_inv, i, q) for i in range(n)]
        return ntt_table, intt_table

    def ntt(self, a: np.ndarray) -> np.ndarray:
        """In-place NTT implementation with precomputed tables"""
        a = a.copy()
        n, q, table = self.n, self.q, self.ntt_table

        k = n
        while k > 1:
            for i in range(0, n, k):
                for j in range(k // 2):
                    w = table[j * (n // k)]
                    x = a[i + j]
                    y = a[i + j + k // 2]
                    a[i + j] = (x + y) % q
                    a[i + j + k // 2] = (w * (y - x)) % q  # Fixed sign issue
            k //= 2
        return a

    def intt(self, a: np.ndarray) -> np.ndarray:
        """In-place inverse NTT implementation"""
        a = a.copy()
        n, q, table = self.n, self.q, self.intt_table

        k = 2
        while k <= n:
            for i in range(0, n, k):
                for j in range(k // 2):
                    w = table[j * (n // k)]
                    x = a[i + j]
                    y = (a[i + j + k // 2] * w) % q
                    a[i + j] = (x + y) % q
                    a[i + j + k // 2] = (x - y) % q  # Fixed reduction issue
            k *= 2

        ninv = pow(n, -1, q)
        return (a * ninv) % q  # Explicit scaling


# In utils.py
def encode_message(message: bytes, n: int, q: int) -> np.ndarray:
    """Encode bytes to polynomial coefficients in Z_q using MSB encoding"""
    # Convert message to bit string
    bit_str = ''.join(format(byte, '08b') for byte in message)

    # Pad with zeros to fill n coefficients
    bit_str = bit_str.ljust(n, '0')[:n]

    # Map bits to coefficients (0 → 0, 1 → q//2)
    return np.array([(int(bit) * (q // 2)) % q for bit in bit_str], dtype=int)


def decode_message(coeffs: np.ndarray, q: int, original_length: int) -> bytes:
    """Decode polynomial coefficients to bytes"""
    bits = ['1' if abs(c - q // 2) < q // 4 else '0' for c in coeffs]

    # Convert to bytes and truncate to original length
    byte_str = bytes(int(''.join(bits[i:i + 8]), 2) for i in range(0, original_length * 8, 8))
    return byte_str


def generate_parameters(n: int = 256, q: int = 7681) -> dict:
    """Generate consistent parameters for testing"""
    return {
        'n': n,
        'q': q,
        'sigma': 3.2,
        'ntt': NTT(n, q) if (q % (2 * n) == 1) else None
    }