from enginalgos.materials import MATERIALS


class AxialBar:
    def __init__(self, material_name, force, area, length):
        self.material = material_name
        self.youngs_modulus = MATERIALS[material_name]
        self.force = force
        self.area = area
        self.length = length

    def get_stress(self):
        return self.force / self.area

    def get_strain(self):
        stress = self.get_stress()
        return stress / self.youngs_modulus

    def get_deformation(self):
        return (self.force * self.length) / (self.area * self.youngs_modulus)
