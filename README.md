# POST-QUANTUM RESISTANCE LATTICE BASED CRYPTOGRAPHY ALGORITHM USING RING LWE
<hr>

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [References](#references)
<hr>

## Introduction
This project is a Python implementation of a post-quantum resistance lattice based cryptography algorithm using Ring LWE. The Ring Learning With Errors (RLWE) problem is a hard problem that is used as the basis for many cryptographic schemes. The Ring-LWE problem is a generalization of the Learning With Errors (LWE) problem, where the underlying algebraic structure is a ring instead of a group. The Ring-LWE problem is believed to be hard to solve, even for quantum computers. This project implements a Ring-LWE based encryption and decryption algorithm using Python.
<hr>

## Project Structure
The project is structured as follows:
```
quantum_algorithm/
├── lattice/
│   ├── __init__.py
│   ├── polynomial.py
│   ├── ring_lwe.py
│   ├── sampling.py
│   ├── keygen.py
│   └── utils.py
│ 
├── quantum/
│   ├── __init__.py
│   ├── attacks.py
│   └── security.py
│ 
├── tests/
│   └── test_*.py
│ 
├── examples/
│   ├── basic_encryption.py
│   ├── secure_communication.py
│   └── quantum_analysis.py
│ 
├── protocols/
│   ├── __init__.py
│   ├── handshake.py  # Secure key exchange
│   ├── encryption.py  # Encrypting & decrypting messages
│   └── authentication.py  # Secure authentication mechanisms
│ 
├── network/
│   ├── __init__.py
│   └── transport.py
│ 
├── benchmarks/
│   ├── __init__.py
│   ├── encryption_speed.py  # Time complexity analysis
│   └── security_analysis.py  # Strength against attacks
│
├── LICENSE
├── requirements.txt
└── README.md
    
```
<hr/>

## Project Packages
The following packages were necessary for the success of the project:
<li>Numpy</li>
<li>Numba</li>
<li>Scipy</li>
<li>Matplotlib</li>
<li>Qiskit</li>

<hr/>

## Installation
To clone the project repository
```bash
    git clone 
```

To install the required packages, run the following command:
```bash
  pip install -r requirements.txt
```

To run the tests, navigate to the `tests` directory and run:
```bash
  pytest test_*.py
```

To run the examples, navigate to the `examples` directory and run:
```bash
  python basic_encryption.py
  python secure_communication.py
  python quantum_analysis.py
```


## Project Should knows
- **Ring LWE**: The Ring Learning With Errors (RLWE) problem is a hard problem that is used as the basis for many cryptographic schemes. The Ring-LWE problem is a generalization of the Learning With Errors (LWE) problem, where the underlying algebraic structure is a ring instead of a group. The Ring-LWE problem is believed to be hard to solve, even for quantum computers.


- **Lattice-based cryptography**: Lattice-based cryptography is a type of public-key cryptography that is based on the hardness of certain problems in lattice theory. It is believed to be secure against quantum attacks, making it a promising candidate for post-quantum cryptography.


- **Lattice encryption**: Lattice encryption is a type of encryption that is based on the hardness of certain problems in lattice theory. It is believed to be secure against quantum attacks, making it a promising candidate for post-quantum cryptography.


- **Encryption Equation**: c(x) = (A(x) \cdot s(x) + e(x)) \mod (x^n + 1, q)


- **Ring-LWE Equation**: 
  - A(x) is a polynomial in the ring R_q
  - s(x) is the secret polynomial
  - e(x) is the error polynomial
  - c(x) is the ciphertext polynomial
  - q is a prime number
  - n is the degree of the polynomial
  - R_q = \mathbb{Z}_q[x] / (x^n + 1)
  - degree n = 2^k = 512
  - modulus q = 2^k - 1 = 2^32 - 1
  - error distribution = Uniform distribution [-B,B] where B = 8