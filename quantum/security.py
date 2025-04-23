import numpy as np


class RingLWESecurity:
    """Security analysis tailored to your Ring-LWE parameters"""

    def __init__(self, params):
        self.n = params['n']
        self.q = params['q']
        self.sigma = params['sigma']

    def security_level(self):
        """Calculate security against quantum lattice attacks"""
        # Security estimation from https://estimate-all-the-lwe-ntru.ccs.2019.rwtsec.org/
        log2_time = 0.265 * self.n - 1.8 * np.log2(self.sigma)
        security_bits = log2_time - np.log2(self.q)
        return max(0, security_bits)

    def parameter_safety(self):
        """Check if parameters meet NIST recommendations"""
        safe = True
        if self.n < 256:
            safe = False
        if self.sigma > self.q / (4 * self.n):
            safe = False
        return safe