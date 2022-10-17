import unittest
import M2B3

class TestClass(unittest.TestCase):
    def test_US04(self):
        self.assertNotEquals(M2B3("Hi"), "good", "Should be...")
