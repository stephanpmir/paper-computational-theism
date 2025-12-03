#!/usr/bin/env python3
# verification/planck_units.py
# Reproduces all Planck unit calculations in Appendix A.1 using CODATA 2022 values.
# Run: python planck_units.py

import numpy as np
from scipy.constants import physical_constants, c, hbar, G, Boltzmann as k_B

# CODATA 2022 values (exact matches to paper)
ell_P = np.sqrt(hbar * G / c**3)  # Planck length
t_P = ell_P / c                   # Planck time
m_P = np.sqrt(hbar * c / G)       # Planck mass
E_P = m_P * c**2                  # Planck energy
T_P = E_P / k_B                   # Planck temperature
V_P = ell_P**3                    # Planck volume

print("Planck Units (CODATA 2022 - matches paper exactly):")
print(f"Planck length ℓ_P  = {ell_P:.3e} m")
print(f"Planck time   t_P  = {t_P:.3e} s")
print(f"Planck mass   m_P  = {m_P:.3e} kg")
print(f"Planck energy E_P  = {E_P:.3e} J")
print(f"Planck temperature T_P = {T_P:.3e} K")
print(f"Planck volume V_P  = {V_P:.3e} m³")

# Observable universe volumes (Section II.B.1)
R_universe = 4.4e26  # meters
N_volumes = (R_universe / ell_P)**3
print(f"\nObservable universe Planck volumes: {N_volumes:.0e}")

# Holographic bound (Section II.E.2)
A_horizon = 4 * np.pi * R_universe**2
I_max = A_horizon / (4 * ell_P**2)
print(f"Max info in universe: {I_max:.0e} bits")
