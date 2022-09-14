from src import jls
import StringIO
import unittest
import os
import sys

class TestJsl(unittest.TestCase):

    def test_print_CSV_Line(args):
        present_folder = os.getcwd()
        path_to_test = os.path.join(
            present_folder, "ressources", "folderForJls", "file1.java")
        #redirect print to assert it 
        captured_print = StringIO.StringIO()
        sys.stdout = captured_print 
        jls.print_CSV_Line(path_to_test, present_folder)
        sys.stdout = sys.__stdout__ 



if __name__ == '__main__':
    unittest.main()
