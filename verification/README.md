# Verification Scripts for "The Code of Creation: Computational Theism"

This directory contains Python scripts that reproduce every numerical claim in the paper and Appendix A using CODATA 2022 constants. 

## Quick Start
1. Install dependencies: `pip install numpy scipy`
2. Run any script: `python planck_units.py`
3. All output matches the paper exactly (e.g., Planck length = 1.616e-35 m).

## File List
- `planck_units.py`: Planck length, time, mass, energy, temperature, volume.
- `cosmic_operations.py`: Lloyd's 10^120 operations bound.
- `error_rate_bounds.py`: Cosmic error rate < 10^-120 per operation.
- `holographic_entropy.py`: Universe max info = 10^122 bits.
- `universe_volumes.py`: 10^183 Planck volumes in observable universe.
- `run_all.py`: Master script to execute everything and print a summary table.

## Example Output (from planck_units.py)
Planck length ℓ_P  = 1.616e-35 m
Planck time   t_P  = 5.391e-44 s
... (full table in paper)

For full reproducibility, see the Zenodo archive: doi.org/10.5281/zenodo.13869183
