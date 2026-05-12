# List of variables
FList = [12000, 15000, 11000, 18000]
A = 0.005

print("Point-by-Point Analysis:")

# Force to Stress
for F in FList:
    sigma = F / A
    print(f"  > Force {F}N -> Stress: {sigma / 1e6:.2f}MPa")

# Averages
SigmaF = sum(FList)
FAmt = len(FList)
FMean = SigmaF / FAmt
sigmaMean = FMean / A

print("-" * 30)
print(f"Average Stress: {sigmaMean / 1e6:.2f}MPa")
print("-" * 30)
