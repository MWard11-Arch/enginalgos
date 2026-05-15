from enginalgos.structures import AxialBar

bar1 = AxialBar("steel", 10000, 0.01, 2)
bar2 = AxialBar("gold", 200000, 0.027, 4.13)

print(f"Steel Deformation: {bar1.get_deformation():.6f} m")
print(f"Gold Deformation: {bar2.get_deformation():.6f} m")
