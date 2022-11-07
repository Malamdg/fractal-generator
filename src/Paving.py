from src.Mosaic import Mosaic
from src.ImageGenerator import ImageGenerator
from src.Factories import Factory


class Paving:
    def __init__(self, complexity: int, number_of_recursions: int, is_symmetrical=False):
        self.complexity = complexity
        self.n = number_of_recursions
        self.isSymmetrical = is_symmetrical
        self.mosaic = Mosaic(complexity=self.complexity, is_symmetrical=self.isSymmetrical)
        self.pattern = self.mosaic.pattern
        self.f = Factory()
        self.generate_paving()

    def generate_paving(self):
        filename = "paving_" + str(self.n) + ".png"
        if self.isSymmetrical:
            filename = "symmetrical_" + filename
        if self.n == 0:
            generator = ImageGenerator(pixel_map=self.pattern.root_pattern)
        elif self.n == 1:
            generator = ImageGenerator(pixel_map=self.mosaic.mosaic)
        else:
            pixel_map = self.mosaic.mosaic
            for i in range(self.n-1):
                pixel_map = self.f.do_recursive_iteration(pixel_map)
            generator = ImageGenerator(pixel_map=pixel_map)

        generator.generate(filename)
