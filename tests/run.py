import pathlib
import unittest


TESTS_PATH = pathlib.Path(__file__).parent.absolute()


def main():
    loader = unittest.TestLoader()
    suite = loader.discover(TESTS_PATH)

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
