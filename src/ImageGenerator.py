import png


class ImageGenerator:
    
    def __init__(self, pixel_map):
        self.pixel_map = pixel_map

    def generate(self, filename):
        filename = "image/" + filename
        rgb_array = []

        for line in self.pixel_map:
            rgb_line = []
            for el in line:
                rgb_line = rgb_line + self.int_to_rgb(el)
            rgb_array.append(rgb_line)
        f = open(filename, 'wb')
        w = png.Writer(int(len(rgb_array[0]) / 3), len(rgb_array), greyscale=False)
        w.write(f, rgb_array)
        f.close()
        return

    @staticmethod
    def int_to_rgb(n):
        if n == 1:
            return [0, 0, 0]
        if n == 0:
            return [255, 255, 255]
