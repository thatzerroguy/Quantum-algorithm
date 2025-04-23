from quantum.attacks import RingLWEAttacks
from quantum.security import RingLWESecurity
from lattice.utils import generate_parameters


def main():
    # Your parameters
    params = generate_parameters(n=256, q=12289)

    # Security analysis
    security = RingLWESecurity(params)
    print(f"Security Level: {security.security_level():.1f} bits")
    print(f"Parameters Safe? {security.parameter_safety()}")

    # Quantum attack simulation
    attacker = RingLWEAttacks(params)
    advantage = attacker.estimate_quantum_advantage()
    print(f"\nQuantum Advantage Factor: {advantage['security_margin']:.1e}")


if __name__ == "__main__":
    main()