import unittest
from unittest.mock import patch
from src import nvloc
from pathlib import Path
from io import StringIO


class testNvloc(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_nvloc(self, mock_print):
        present_folder = Path.cwd()
        path_to_test = Path.joinpath(present_folder,"tests", "ressources","nvloc", "test.java")
        nvloc.nvloc(path_to_test)
        self.assertEqual(mock_print.getvalue().strip().replace("\n", ""), "10")


if __name__ == '__main__':
    unittest.main()
