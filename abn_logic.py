import numpy as np


def run_abn_simulation():
    # 1. Parameters from the ABN Paper
    r0 = 147.0  # Mpc (BAO scale)
    sig_BAO = 1.47  # ~1% BAO uncertainty
    sig_z = 1.20  # mid-z spectroscopic redshift
    sig_ang = 1e-3  # rad (CMB dipole angular resolution)
    theta0 = np.pi / 3  # 60 degrees

    # 2. Case 1: CMB + BAO only
    var_ang = r0**2 * sig_ang**2 * (1 + np.sin(theta0) ** 2)
    var_r1 = sig_BAO**2
    sig_tot1 = np.sqrt(var_r1 + var_ang)

    # 3. Case 2: Optimal Fusion (ABN Framework)
    # Redshift acts as an independent constraint like time in GPS
    var_r_combined = 1.0 / (1.0 / sig_BAO**2 + 1.0 / sig_z**2)
    sig_tot2 = np.sqrt(var_r_combined + var_ang)

    # 4. Results Generation
    improvement = 100 * (1 - sig_tot2 / sig_tot1)
    r_star = np.sqrt(var_r_combined) / sig_ang  # Transition scale

    print("--- ABN Framework Validation ---")
    print(f"BAO-only Uncertainty: {sig_tot1:.4f} Mpc")
    print(f"Fused (ABN) Uncertainty: {sig_tot2:.4f} Mpc")
    print(f"Positional Precision Gain: {improvement:.1f}%")
    print(f"Transition Scale (r*): {r_star:.0f} Mpc")


if __name__ == "__main__":
    run_abn_simulation()
