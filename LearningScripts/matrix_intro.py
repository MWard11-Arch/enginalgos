import numpy as np  # numpy.* turns into np.*

# 3x3 Stress Tensor matrix
# [[sigmax, tauxy, tauxz],
#  [tauyz, sigmay, tauyz],
# [tauzx, tauzy, sigmaz]]
stress_tensor = np.array([[150.0, 40.0, 0.0], [40.0, 80.0, 0.0], [0.0, 0.0, 60.0]])

print("Stress Tensor (MPa):")
print(stress_tensor)

# Calculate Principal Stresses (Eigenvalues)
# max stresses the material feels
principal_stresses = np.linalg.eigvals(stress_tensor)

print("\nPrincipal Stresses (MPa):")
for s in principal_stresses:
    print(f"-{s:.2f}MPa")
