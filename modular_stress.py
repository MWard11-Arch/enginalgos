# Define formulas
def get_stress(Force, Area):
    """Calculates stress (Pa)"""
    return Force / Area


def get_strain(stress, YoungsModulus):
    """Calculates strain"""
    return stress / YoungsModulus


# Define variables
F = 50000
A = 0.02
E = 200e9

# Call Formulas
sigma = get_stress(F, A)
epsilon = get_strain(sigma, E)

# Output
print(f"Calculated Stress: {sigma / 1e6:.2f} MPa")
print(f"Calculated Strain: {epsilon:.6f}")
