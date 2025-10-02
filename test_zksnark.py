# test_zksnark.py
"""
Tests for ZKSnark module.
"""

import unittest
from zksnark import ZKSnark

class TestZKSnark(unittest.TestCase):
    """Test cases for ZKSnark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZKSnark()
        self.assertIsInstance(instance, ZKSnark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZKSnark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
