import client
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.client = client.Deezer()

    def test_user(self):
        u = self.client.user(id=13710817)
        self.assertTrue(u is not None)
        self.assertTrue(u['name'] == 'benjaminbonny')

if __name__ == '__main__':
    unittest.main()
