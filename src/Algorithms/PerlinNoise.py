# ||============================================================================||
# || SOURCE : https://fr.wikipedia.org/wiki/Bruit_de_Perlin section Pseudo-Code ||
# ||============================================================================||

# Interpolation between a0 and a1
# w => weight between 0.0 and 1.0
def lerp(a0: float, a1: float, w: float):
    return (1.0-w)*a0 + w*a1


def dotGradient(ix: int, iy: int, x: float, y: float):
    return


def generate_noise(array: list):
    for line in array:
        for el in line:
            el = 1
