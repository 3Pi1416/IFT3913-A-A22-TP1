import unittest
from src import lcsec
from pathlib import Path

from src.JavaMetric import read_java_metric_from_csv


class Testlcsec(unittest.TestCase):
    def test_lcsec(self):
        present_folder = Path.cwd()
        path_to_test_csv = Path.joinpath(present_folder, "ressources", "lcsec", "test_csv.csv")
        path_of_test_java = Path.joinpath(present_folder, "ressources", "jls")
        data_from_csv = read_java_metric_from_csv(path_to_test_csv)
        test = lcsec.get_csec_values(path_of_test_java, data_from_csv)
        self.assertEqual(test[0].lcsec, 2)
        self.assertEqual(test[1].lcsec, 1)


if __name__ == '__main__':
    unittest.main()
