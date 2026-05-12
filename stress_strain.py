# stress_strain.py

# 1. Constants (Steel properties)
# 200e9 is scientific notation for 200,000,000,000
E = 200e9

# 2. Input Variables
F = float(input("Enter the force (N): "))  # Force in Newtons
A = float(input("Enter the cross-sectional area (m^2): "))  # Area in Square meters

# 3. Calculation
sigma = F / A  # Stress in Pa
epsilon = sigma / E  # Strain

# 4. Output

# Title
print("-" * 30)
print("ENGINEERING REPORT")

# Stress
if sigma >= 1e6:
    # Convert to MPa
    print(f"Stress: {sigma / 1e6:.2f} MPa")
elif sigma >= 1e3:
    # Convert to kPa
    print(f"Stress: {sigma / 1e3:.2f} kPa")
else:
    print(f"Stress: {sigma:.2f} Pa")

# Strain
print(f"Strain: {epsilon:.8f}")

# Bottom
print("-" * 30)
