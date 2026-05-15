# Define formulas
def get_stress(force: float, area: float) -> float:
    """
    Calculates Axial Stress

    Args:
        force: Force in Newtons (N).
        area: Area in Square Meters (m^2).

    Returns:
        Stress in Pascals (Pa).
    """
    if area <= 0:
        raise ValueError("Area must be greater than zero.")
    return force / area


def get_strain(stress: float, youngs_modulus: float):
    """
    Calculates Axial Strain

    Args:
        stress: Stress in Pa
        youngs_modulus: Young's Modulus in Pa
    """
    return stress / youngs_modulus


def format_stress(stress_pa: float) -> str:
    """
    Converts Stress in Pa to a readable string with units (Pa, kPa, MPa).
    """
    if stress_pa >= 1e6:
        # Convert to MPa
        return f"{stress_pa / 1e6:.2f} MPa"
    elif stress_pa >= 1e3:
        # Convert to kPa
        return f"{stress_pa / 1e3:.2f} kPa"
    else:
        return f"{stress_pa:.2f} Pa"
