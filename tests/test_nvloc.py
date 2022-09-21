import unittest
from src import nvloc
from pathlib import Path


class testNvloc(unittest.TestCase):
    def test_nvloc(self):
        present_folder = Path.cwd()
        path_to_test = Path.joinpath(present_folder, "ressources", "nvloc", "test.java")
        test = nvloc.nvloc(path_to_test)
        self.assertEqual(test, 10)


if __name__ == '__main__':
    unittest.main()
