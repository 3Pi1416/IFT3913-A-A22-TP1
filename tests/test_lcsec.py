import unittest
from src import lcsec
from pathlib import Path


class Testlcsec(unittest.TestCase):
    def test_lcsec(self):
        present_folder = Path.cwd()
        path_to_test_csv = Path.joinpath(present_folder, "ressources", "lcsec", "test_csv.csv")
        test = lcsec.



if __name__ == '__main__':
    unittest.main()
