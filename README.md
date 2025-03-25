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