from src import jls
import unittest
from pathlib import Path

from src.JavaMetric import JavaMetric


class TestJsl(unittest.TestCase):
    def test_print_csv_line(self):
        present_folder = Path.cwd()
        path_to_test = Path.joinpath(present_folder, "ressources", "jls", "file1.java")
        java_metric_receive = jls.add_csv_line(path_to_test, present_folder)
        path_to_get = path_to_test.relative_to(present_folder)
        java_metric_test = JavaMetric(path=path_to_get, package="ressources.jls", java_class="file1")
        self.assertEqual(java_metric_test, java_metric_receive)

    def test_jls(self):
        present_folder = Path.cwd()
        path_to_test = Path.joinpath(present_folder, "ressources", "jls")
        java_metric_list = jls.java_list(path_to_test,present_folder)
        # Windows and linux
        self.assertEqual(len(java_metric_list), 3)


if __name__ == '__main__':
    unittest.main()
