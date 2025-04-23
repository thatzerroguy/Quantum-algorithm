from lattice.polynomial import Polynomial
from lattice.utils import generate_parameters

def keygen(n, q, sigma, ntt):
    """Generate public and secret keys for Ring-LWE"""
    a = Polynomial.random(n, q)  # Uniform in Z_q
    s = Polynomial.random(n, q, centered=True)  # Small coefficients
    e = Polynomial.random(n, q, centered=True)  # Error term

    b = -a * s + e  # Public key
    return (b, a), s  # Public and secret keys