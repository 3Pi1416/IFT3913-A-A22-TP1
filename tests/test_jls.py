from src import jls
import unittest
from pathlib import Path

from src.javaMetric import javaMetric


class TestJsl(unittest.TestCase):
    def test_print_csv_line(self):
        present_folder = Path.cwd()
        path_to_test = Path.joinpath(present_folder, "ressources", "jls", "file1.java")
        java_metric_receive = jls.add_csv_line(path_to_test, present_folder)
        path_to_get = path_to_test.relative_to(present_folder)
        java_metric_test = javaMetric(path=f"./{path_to_get.as_posix()}", package="ressources.jls", java_class="file1")
        self.assertEqual(java_metric_test, java_metric_receive)

    def test_jls(self, mock_print):
        present_folder = Path.cwd()
        path_to_test = Path.joinpath(present_folder, "tests", "ressources", "jls")
        jls.java_list()
        # Windows and linux
        self.assertEqual(mock_print.getvalue().strip().replace(
            "\n", ""),
            "./folder2/file1.java, folder2, file1./folder2/folder1/file2.java, folder2.folder1, file2./folder2/folder1/file3.java, folder2.folder1, file3")


if __name__ == '__main__':
    unittest.main()
