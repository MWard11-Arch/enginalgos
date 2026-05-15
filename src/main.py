from enginalgos.mechanics import get_stress, get_strain


def main():
    force = 50e3
    area = 20e-3
    youngs_modulus = 200e9

    stress = get_stress(force, area)
    strain = get_strain(stress, youngs_modulus)

    print(f"Stress: {stress / 1e6:.2f} MPa")
    print(f"Strain: {strain:.6f}")


if __name__ == "__main__":
    main()
