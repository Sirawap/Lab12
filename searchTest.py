import binsearch as bs
import unittest

class KnownValue(unittest.TestCase):
    knowValues = (([0, 1, 2, 3, 4, 5], 3, 4),
                  ([0, 1, 2, 3, 4, 5], 0, 1),
                  ([0, 1, 2, 3, 4, 5], 4, 5),
                  ([0, 1, 2, 3, 4, 5], 5, 6),
                  ([0, 1, 2, 3, 4, 5], 1, 2),
                  ([0, 1, 2, 3, 4, 5], 2, 3),
                  ([0, 1, 2, 3, 4, 6], 6, 6),
                  ([0, 1, 4, 7, 9, 10], 4, 2),
                  ([0, 2,53,364,1235,23523], 2, 2),
                  ([0, 2,53,364,1235,23523], 23523, 6))

    def testBinsearchKnownValues(self):
        for _list, key, index in self.knowValues:
            result = bs.binsearch(_list,key)
            self.assertEqual(index,result)

if __name__ == '__main__':
    unittest.main()