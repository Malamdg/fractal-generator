import numpy.random as rd
from src.ImageGenerator import ImageGenerator
from src.Algorithms.PatternSmoothening import smoothen


class Pattern:
    def __init__(self, complexity: int, is_symmetrical=False):
        self.size = 6
        self.complexity = complexity % 10
        self.isSymmetrical = is_symmetrical
        self.root_pattern = self.generate_root()
        smoothen(self.root_pattern)
        self.generate_image()

    def __str__(self):
        string = ""
        for line in self.root_pattern:
            for el in line:
                string += str(el) + "  "
            string += "\n"

        return string

    def generate_root_pattern(self):
        # Basic size of base_pattern
        base_pattern = [[0 for _ in range(self.size)] for _ in range(self.size)]

        # Complexity modulates the pattern global noise
        p = 1/2
        q = 1 - p

        for i in range(self.size):
            for j in range(self.size):
                base_pattern[i][j] = rd.choice([0, 1], p=[p, q])
        return base_pattern

    def generate_symmetrical_root_pattern(self):
        # Basic size of base_pattern
        base_pattern = [[0 for _ in range(self.size)] for _ in range(self.size)]

        # Complexity modulates the pattern global noise
        p = 1 / 2
        q = 1 - p

        for i in range(self.size):
            for j in range(i, self.size):
                base_pattern[i][j] = rd.choice([0, 1], p=[p, q])
                base_pattern[j][i] = base_pattern[i][j]

        return base_pattern

    def generate_root(self):
        return self.generate_symmetrical_root_pattern() if self.isSymmetrical else self.generate_root_pattern()

    def generate_image(self):
        filename = "pattern.png"
        if self.isSymmetrical:
            filename = "symmetrical_" + filename

        generator = ImageGenerator(self.root_pattern)
        generator.generate(filename)
