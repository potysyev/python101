class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass_calculation(self, thickness):  # толщина в сантиметрах
        asphalt_density = 2500  # масса одного кубометра асфальтобетонной смеси в кг
        return self._lenght * self._width * (thickness / 100) * asphalt_density / 1000  # результат в тоннах


rd = Road(5000, 20)
print(rd.mass_calculation(5))
