import unittest
from unittest.mock import patch
import nvloc
from pathlib import Path
from io import StringIO


class testNvloc(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def nvloc_test_(self, mock_print):
        path_test = Path("C:\\Users\\XHugo\\git\\IFT3913-A-A22-TP1\\tests\\test_nvloc.py")
        nvloc.nvloc(path_test)
        self.assertEqual(mock_print.getvalue(), "10")


if __name__ == '__main__':
    unittest.main()
