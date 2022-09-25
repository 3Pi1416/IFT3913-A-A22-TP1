import unittest
from src import egon
from pathlib import Path


class TestEgon(unittest.TestCase):
    def test_egon(self):
        present_folder = Path.cwd()
        path_to_test = Path.joinpath(present_folder, "ressources", "egon")
        god_class_list = egon.calculate_egon(path_to_test, 20)
        self.assertEqual(len(god_class_list),1)
        self.assertEqual(god_class_list[0].java_class,"egon")
        return


if __name__ == '__main__':
    unittest.main()
