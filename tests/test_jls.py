from src import jls
from io import StringIO
from unittest.mock import patch
import unittest
import os
import sys
from pathlib import Path


class TestJsl(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_csv_line(self, mock_print):
        present_folder = Path.cwd()
        path_to_test = Path.joinpath(present_folder, "ressources", "jls", "file1.java")
        jls.print_csv_line(path_to_test, present_folder)
        path_to_get = path_to_test.relative_to(present_folder)
        #Windows and linux
        self.assertEqual(mock_print.getvalue().strip().replace("\n", ""),
                         f"./{path_to_get.as_posix()}, ressources.jls, file1")

    @patch('sys.stdout', new_callable=StringIO)
    def test_jls(self, mock_print):
        present_folder = Path.cwd()
        path_to_test = Path.joinpath(present_folder, "tests", "ressources","jls")
        jls.java_list(path_to_test)
        #Windows and linux
        self.assertEqual(mock_print.getvalue().strip().replace(
            "\n", ""), "./folder2/file1.java, folder2, file1./folder2/folder1/file2.java, folder2.folder1, file2./folder2/folder1/file3.java, folder2.folder1, file3")


if __name__ == '__main__':
    unittest.main()
