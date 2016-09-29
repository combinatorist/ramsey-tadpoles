import unittest
import pdb

import tpol_prf as tp

tp.tpol_prf(5, 6, 31)


class RamseyTadpolesTest(unittest.TestCase):
    def test010_coprime(self):
        self.assertTrue(tp.coprime(2, 3))
        self.assertTrue(tp.coprime(3, 2))
        self.assertTrue(tp.coprime(30, 49))
        self.assertFalse(tp.coprime(30, 50))
        self.assertFalse(tp.coprime(50, 30))
        self.assertFalse(tp.coprime(3, 30))

if __name__ == '__main__':
        pdb.set_trace()
        unittest.main()
