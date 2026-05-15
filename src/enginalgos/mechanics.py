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
