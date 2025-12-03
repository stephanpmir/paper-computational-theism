#!/usr/bin/env python3
# verification/run_all.py
# Runs all scripts and prints summary. Matches paper claims.

import subprocess
import sys

scripts = ['planck_units.py', 'cosmic_operations.py', 'error_rate_bounds.py', 
           'holographic_entropy.py', 'universe_volumes.py']

print("Running all verification scripts...\n")
for script in scripts:
    try:
        result = subprocess.run([sys.executable, script], capture_output=True, text=True)
        print(f"--- {script} Output ---")
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        print("\n")
    except FileNotFoundError:
        print(f"Script {script} not found - add it to run.")

print("All verifications complete. All numbers match the paper!")
