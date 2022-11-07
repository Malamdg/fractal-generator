class Factory:

    @staticmethod
    def flip_vertically(root_pattern):
        flipped_pattern = []
        for line in root_pattern:
            flipped_line = line[::-1]
            flipped_pattern.append(flipped_line)
        return flipped_pattern

    @staticmethod
    def flip_horizontally(root_pattern):
        return [root_pattern[i] for i in range(len(root_pattern)-1, -1, -1)]

    @staticmethod
    def merge_lines(pattern_1, pattern_2):
        return [pattern_1[i] + pattern_2[i] for i in range(len(pattern_1))]

    def do_recursive_iteration(self, root_pattern):
        top_left_pattern = root_pattern.copy()
        top_right_pattern = self.flip_vertically(top_left_pattern)
        bottom_right_pattern = self.flip_horizontally(top_right_pattern)
        bottom_left_pattern = self.flip_horizontally(top_left_pattern)
        top_pattern = self.merge_lines(top_left_pattern, top_right_pattern)
        bottom_pattern = self.merge_lines(bottom_left_pattern, bottom_right_pattern)
        return top_pattern + bottom_pattern
