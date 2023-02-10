#!/usr/bin/env python3
"""
Test Base model class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test test_to_dict"""
    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm2.id, str)

if __name__ == "__main__":
    unittest.main()
