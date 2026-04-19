# test_nodeloom.py
"""
Tests for NodeLoom module.
"""

import unittest
from nodeloom import NodeLoom

class TestNodeLoom(unittest.TestCase):
    """Test cases for NodeLoom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeLoom()
        self.assertIsInstance(instance, NodeLoom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
