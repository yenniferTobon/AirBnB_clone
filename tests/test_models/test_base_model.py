#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class Test_BaseModel(unittest.TestCase):

    def setUp(self):
        self.obj = BaseModel() 

    def test_createBaseModel(self):
        self.assertIsInstance(self.obj, BaseModel)

    def test_Id_Is_String(self):
        self.assertEqual(type(self.obj.id), str)

   # def test_doctrins(self):
   #     self.assertIsNotNone(BaseModel.__doc__)

   # def test_pep8_base_model(self):
   #     """ Test for PEP8 ok. """
   #     pep8style = pep8.StyleGuide(quiet=True)
   #     result = pep8style.check_files(['models/base_model.py'])
   #     self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_id_uuid_v4(self):
        """Test version 4 of UUID"""
        test__version = uuid.UUID(self.obj.id).version
        self.assertEqual(test__version, 4, "Error: Different version")

   # def test_created_at_Is_datatime(self):
   #     self.assertIs(self.obj_BM.created_at, datetime.datetime)

if __name__ == "__main__":
    unittest.main()
