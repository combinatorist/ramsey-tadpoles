import unittest

import ramsey_tadpoles as tp

tp.proof(5, 6, 31)


class RamseyTadpolesTest(unittest.TestCase):
    def test010_coprime(self):
        self.assertTrue(tp.coprime(2, 3))
        self.assertTrue(tp.coprime(3, 2))
        self.assertTrue(tp.coprime(30, 49))
        self.assertFalse(tp.coprime(30, 50))
        self.assertFalse(tp.coprime(50, 30))
        self.assertFalse(tp.coprime(3, 30))

    def test020_modpows(self):
        self.assertEqual(tp.modpows(2, 3), [2, 1])
        self.assertEqual(tp.modpows(30, 49), [30, 18, 1])
        self.assertEqual(tp.modpows(30, 50), [30, 0])

    def test030_oddpows(self):
        self.assertEqual(tp.oddpows([30, 18, 1], 10, 49), [6, 33, 10])

    def test040_modinverses(self):
        self.assertEqual(tp.modinverses([30, 18, 1], 49), [19, 31, 48])

    def test050_proof(self):
        self.assertEqual(tp.proof(3, 10, 49)[:3], (False,) * 3)
        self.assertEqual(tp.proof(2, 2, 9)[:3], (True,) * 3)

if __name__ == '__main__':
        unittest.main()
