import numpy as np
from .utils import NTT

class Polynomial:
    """Represents polynomials in Z_q[x] / (x^n + 1)"""

    def __init__(self, coeffs, n, q, ntt=None):
        self.coeffs = np.array(coeffs) % q
        self.n = n
        self.q = q
        self.ntt = ntt  # Optional NTT for fast multiplication

    @staticmethod
    def random(n, q, centered=False):
        """Generate a random polynomial with coefficients in Z_q."""
        if centered:
            coeffs = np.random.randint(-q // 2, q // 2, size=n)  # Small coefficients
        else:
            coeffs = np.random.randint(0, q, size=n)  # Uniform in Z_q
        return Polynomial(coeffs, n, q)

    def __add__(self, other):
        """Polynomial addition"""
        return Polynomial((self.coeffs + other.coeffs) % self.q, self.n, self.q, self.ntt)

    def __sub__(self, other):
        """Polynomial subtraction"""
        return Polynomial((self.coeffs - other.coeffs) % self.q, self.n, self.q, self.ntt)

    def __neg__(self):
        """Negate the polynomial (element-wise negation of coefficients)."""
        return Polynomial((-self.coeffs) % self.q, self.n, self.q, self.ntt)

    # In polynomial.py
    def __mul__(self, other):
        """NTT-accelerated polynomial multiplication"""
        if self.ntt and other.ntt:
            # Convert to NTT domain
            a_ntt = self.ntt.ntt(self.coeffs)
            b_ntt = self.ntt.ntt(other.coeffs)

            # Point-wise multiplication
            result_ntt = (a_ntt * b_ntt) % self.q

            # Convert back from NTT domain
            return Polynomial(self.ntt.intt(result_ntt), self.n, self.q, self.ntt)
        else:
            # Schoolbook multiplication with proper reduction
            result = np.polymul(self.coeffs, other.coeffs)

            # Reduce mod x^n + 1 by folding upper coefficients
            # Split into low (degree 0..n-1) and high (degree n..2n-2)
            low = result[:self.n]
            high = result[self.n:] if len(result) > self.n else []

            # Pad high with zeros to match low's length
            high_padded = np.pad(high, (0, self.n - len(high)), 'constant')

            # Final reduction: low - high_padded
            reduced = (low - high_padded) % self.q
            return Polynomial(reduced, self.n, self.q)

    def __repr__(self):
        return f"Polynomial({self.coeffs.tolist()})"