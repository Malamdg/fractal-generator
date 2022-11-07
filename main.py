from src.Paving import Paving


def main():
    n = 8
    Paving(complexity=10, number_of_recursions=n)
    Paving(complexity=10, number_of_recursions=n, is_symmetrical=True)


if __name__ == '__main__':
    main()
