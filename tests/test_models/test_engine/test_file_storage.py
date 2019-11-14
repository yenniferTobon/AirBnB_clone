#!/usr/bin/python3
"""Module to make tests"""
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8
import uuid
import models
import os


class Test_FileStorage(unittest.TestCase):
    """ Class to test
    """

    def setUp(self):
        """Function that execute before of each test function
        """
        self.obj_storage = FileStorage()

    def test_createFileStorage(self):
        """Test that is instance
        """
        self.assertIsInstance(self.obj_storage, FileStorage)

    def test_function_new(self):
        obj_BM = BaseModel()
        self.obj_storage.new(obj_BM)
        key = obj_BM.__class__.__name__+"."+obj_BM.id
        self.assertEqual(self.obj_storage.all()[key], obj_BM)

    def test_docString(self):
        """Test if function and class have docString
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_pep8_file_storage(self):
        """ Test for PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_path_file(self):
        """Test path_file
        """
        self.assertTrue(os.path.exists(
            self.obj_storage._FileStorage__file_path))

    def test_save_content(self):
        """Test to compare the saved in json file with to_dic()
        """
        obj_BM = BaseModel()
        self.obj_storage.new(obj_BM)
        self.obj_storage.save()
        self.obj_storage.reload()
        key = obj_BM.__class__.__name__+"."+obj_BM.id
        self.assertDictEqual(
            self.obj_storage.all()[key].to_dict(), obj_BM.to_dict())

if __name__ == "__main__":
    unittest.main()
