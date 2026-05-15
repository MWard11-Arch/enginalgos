from enginalgos.structures import AxialBar
from enginalgos.mechanics import format_stress
from enginalgos.materials import MATERIALS
from enginalgos.tensors import get_principal_stresses
import numpy as np


def main():
    while True:
        print("\n--- Engineering Algorithms ---")
        print("1. Axial Member Analysis")
        print("2. Tensor Analysis")
        print("3. Exit")

        choice = input("Select an option: ")
        if choice == "1":
            material = input("Enter Material: ").lower()
            try:
                MATERIALS[material]
            except KeyError:
                print(f"Error: '{material}' is not in our database.")
                continue

            force = input("Enter Axial Force (N): ")
            try:
                force = float(force)
            except ValueError:
                print(f"Error: {force} N is not valid.")
                continue

            area = input("Enter Area (m^2): ")
            try:
                area = float(area)
            except ValueError:
                print(f"Error: {area} m^2 is not valid.")
                continue

            length = input("Enter Length (m): ")
            try:
                length = float(length)
            except ValueError:
                print(f"Error: {length} m is not valid.")

            bar = AxialBar(material, force, area, length)
            bar_stress = float(bar.get_stress())
            bar_strain = float(bar.get_strain())
            bar_deformation = float(bar.get_deformation())

            print(f"Stress: {format_stress(bar_stress)}")
            print(f"Strain: {bar_strain:.3e}")
            print(f"Deformation: {bar_deformation:.3e}")

        elif choice == "2":
            sigma_x = input("Enter Sigma(x): ")
            try:
                sigma_x = float(sigma_x)
            except ValueError:
                print(f"Error: {sigma_x} is not valid.")
                continue

            sigma_y = input("Enter Sigma(y): ")
            try:
                sigma_y = float(sigma_y)
            except ValueError:
                print(f"Error: {sigma_y} is not valid.")
                continue

            tau_xy = input("Enter tau(xy): ")
            try:
                tau_xy = float(tau_xy)
            except ValueError:
                print(f"Error: {tau_xy} is not valid.")
                continue

            matrix = np.array([[sigma_x, tau_xy], [tau_xy, sigma_y]])
            principal_stresses = get_principal_stresses(matrix)
            for s in principal_stresses:
                print(f"Principal Stress: {s}")

        elif choice == "3":
            print("Shutting down...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
