from enginalgos.mechanics import get_stress, get_strain
from enginalgos.materials import MATERIALS

# User-defined Variables
# Young's Modulus
material = input("Enter Material: ").lower()
try:
    youngs_modulus = MATERIALS[material]
except KeyError:
    print(f"Error: '{material}' is not in our database.")
    exit()
# Force
force = input("Enter Force (N): ")
try:
    force = float(force)
except ValueError:
    print(f"Error: {force}N is not valid.")
    exit()
# Area
area = input("Enter Area (m^2): ")
try:
    area = float(area)
except ValueError:
    print(f"Error: {area}m^2 is not valid.")
    exit()
# Calculations
stress = get_stress(force, area)
strain = get_strain(stress, youngs_modulus)

# Printed Outputs
print("Output:")
print("-" * 20)
print(f"Stress: {stress / 1e6:.2f} MPa")
print(f"Strain :{strain:.6f}")
print("-" * 20)
