import binsearch as bs
import unittest

class pre_condition_test(unittest.TestCase):
    def testdataListIsNotList(self):
        self.assertRaises(bs.NotIntegerError,bs.binsearch,2,2)
    def testdataListIsNotInteger(self):
        test = ['a',0.5]
        for x in test:
            self.assertRaises(bs.NotIntegerError,bs.binsearch,[x,2,3],2)
    def testkeyIsNotInteger(self):
        test = ['a',0.5]
        for x in test:
            self.assertRaises(bs.NotIntegerError,bs.binsearch,[1,2,3,4,5],x)

class KnownValue(unittest.TestCase):
    knowValues = (([0, 1, 2, 3, 4, 5], 3, 3),
                  ([0, 1, 2, 3, 4, 5], 0, 0),
                  ([0, 1, 2, 3, 4, 5], 4, 4),
                  ([0, 1, 2, 3, 4, 5], 5, 5),
                  ([0, 1, 2, 3, 4, 5], 1, 1),
                  ([0, 1, 2, 3, 4, 5], 2, 2),
                  ([0, 1, 2, 3, 4, 6], 6, 5),
                  (5, 2, 1),
                  ([0, 2,53,364,1235,23523], 23523, 5))

    def testBinsearchKnownValues(self):
        for _list, key, index in self.knowValues:
            result = bs.binsearch(_list,key)
            self.assertEqual(index,result)

class Failre(unittest.TestCase):
    def testBinsearchKnownValues(self):
        for _list, key, index in self.knowValues:
            result = bs.binsearch(_list,key)
            self.assertEqual(index,result)
   
    def notList(self):
        for _list, key, index in self.knowValues:
            self.assertRaises(bs.InvalidArgument, bs.binsearch, _list,key )
            
class Sanity(unittest.TestCase):   
    def inRange(self):
         for _list, key, index in(([0, 1, 2, 3, 4, 5], 3, 3),
                  ([0, 1, 2, 3, 4, 5], 0, 0),
                  ([0, 1, 2, 3, 4, 5], 4, 4),
                  ([0, 1, 2, 3, 4, 5], 5, 5),
                  ([0, 1, 2, 3, 4, 5], 1, 1),
                  ([0, 1, 2, 3, 4, 5], 2, 2),
                  ([0, 1, 2, 3, 4, 6], 6, 5),
                  ([0, 1, 4, 7, 9, 10], 4, 2),
                  ([0, 2,53,364,1235,23523], 2, 1),
                  ([0, 2,53,364,1235,23523], 23523, 5)):
            result = bs.binsearch(_list,key)
            self.assertIn(result,_list)

    def EqualFalse(self):
        for _list, key, index in (([0, 1, 2, 3, 4, 5], 3, 3),
                  ([0, 1, 2, 3, 4, 5], 0, 0),
                  ([0, 1, 2, 3, 4, 5], 4, 4),
                  ([0, 1, 2, 3, 4, 5], 5, 5),
                  ([0, 1, 2, 3, 4, 5], 1, 1),
                  ([0, 1, 2, 3, 4, 5], 2, 2),
                  ([0, 1, 2, 3, 4, 6], 6, 5),
                  ([0, 1, 4, 7, 9, 10], 4, 2),
                  ([0, 2,53,364,1235,23523], 2, 1),
                  ([0, 2,53,364,1235,23523], 23523, 5)):
            result = bs.binsearch(_list,key)
            self.assertEqual(index,result)
    
    def NoneFalse(self):
        for _list, key, index in (([0, 1, 2, 3, 4, 5], 3, 3),
                  ([0, 1, 2, 3, 4, 5], 0, 0),
                  ([0, 1, 2, 3, 4, 5], 4, 4),
                  ([0, 1, 2, 3, 4, 5], 5, 5),
                  ([0, 1, 2, 3, 4, 5], 1, 1),
                  ([0, 1, 2, 3, 4, 5], 2, 2),
                  ([0, 1, 2, 3, 4, 6], 6, 5),
                  ([0, 1, 4, 7, 9, 10], 11, None),
                  ([0, 2,53,364,1235,23523], 2, 1),
                  ([0, 2,53,364,1235,23523], 23523, 5)):
            result = bs.binsearch(_list,key)
            if key not in _list:
                self.assertEqual(key,result)
        
        



if __name__ == '__main__':
    unittest.main()