from src.ImageGenerator import ImageGenerator
from src.Pattern import Pattern
from src.Factories import Factory


class Mosaic:
    def __init__(self, complexity: int, is_symmetrical=False):
        self.complexity = complexity
        self.isSymmetrical = is_symmetrical
        self.pattern = self.generate_pattern()
        self.factory = Factory()
        self.mosaic = self.generate_mosaic()
        self.generate_image()

    def __str__(self):
        string = ""
        for line in self.mosaic:
            for el in line:
                string += str(el) + "  "
            string += "\n"
        return string

    def generate_pattern(self):
        return Pattern(self.complexity, self.isSymmetrical)

    def generate_mosaic(self):
        return self.factory.do_recursive_iteration(self.pattern.root_pattern)

    def generate_image(self):
        filename = "mosaic.png"
        if self.isSymmetrical:
            filename = "symmetrical_" + filename

        generator = ImageGenerator(self.mosaic)
        generator.generate(filename)
