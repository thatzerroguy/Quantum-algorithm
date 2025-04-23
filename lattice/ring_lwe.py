import numpy as np
from .polynomial import Polynomial
from .sampling import sample_gaussian


class RingLWE:
    """Implements Ring-LWE encryption and decryption"""

    def __init__(self, n: int, q: int, sigma: float, ntt=None):
        self.n = n
        self.q = q
        self.sigma = sigma
        self.ntt = ntt  # Optional NTT acceleration

    def generate_keys(self):
        a = Polynomial.random(self.n, self.q)
        s = Polynomial(sample_gaussian(self.n, self.sigma, self.q), self.n, self.q)
        e = Polynomial(sample_gaussian(self.n, self.sigma, self.q), self.n, self.q)
        b = a * s + e
        return (b, a), s  # Public key is (b, a)

    def encrypt(self, pk: tuple, message: Polynomial) -> tuple:
        b, a = pk
        r = Polynomial(sample_gaussian(self.n, self.sigma, self.q), self.n, self.q)
        e1 = Polynomial(sample_gaussian(self.n, self.sigma, self.q), self.n, self.q)
        e2 = Polynomial(sample_gaussian(self.n, self.sigma, self.q), self.n, self.q)

        u = a * r + e1
        v = b * r + e2 + message
        return (u, v)

    def decrypt(self, sk: Polynomial, ciphertext: tuple) -> Polynomial:
        """Decrypts ciphertext using secret key"""
        u, v = ciphertext

        # Ensure u and v are Polynomial objects
        u_poly = Polynomial(u.coeffs, self.n, self.q, self.ntt) if not isinstance(u, Polynomial) else u
        v_poly = Polynomial(v.coeffs, self.n, self.q, self.ntt) if not isinstance(v, Polynomial) else v

        # Ensure that the result of u * sk is a Polynomial
        u_sk = u_poly * sk  # This should return a Polynomial
        m_hat = v_poly - u_sk
        return m_hat