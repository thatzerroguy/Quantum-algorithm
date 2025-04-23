import numpy as np

def sample_gaussian(n: int, sigma: float, q: int) -> np.ndarray:
    """Samples n coefficients from a centered discrete Gaussian distribution mod q"""
    samples = np.round(np.random.normal(0, sigma, n)).astype(int) % q
    samples[samples > q // 2] -= q  # Center values
    return samples