import timeit
from lattice.ring_lwe import RingLWE


def benchmark_encryption():
    rlwe = RingLWE(256, 7681, 3.2)
    public_key, _ = rlwe.generate_keys()

    def _encrypt():
        rlwe.encrypt(public_key, [0] * 256)

    return timeit.timeit(_encrypt, number=100)