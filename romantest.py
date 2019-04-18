import roman0 as r0
import roman1 as r1
import roman2 as r2
import roman3 as r3
import roman4 as r4
import unittest

class KnownValue(unittest.TestCase):
    knowValues = ((1,'I'),
                  (2,'II'),
                  (3, 'III'),
                  (4, 'IV'),
                  (5, 'V'),
                  (6, 'VI'),
                  (7, 'VII'),
                  (8, 'VIII'),
                  (9, 'IX'),
                  (10, 'X'),
                  (50, 'L'),
                  (100, 'C'),
                  (500, 'D'),
                  (1000, 'M'),
                  (31, 'XXXI'),
                  (148, 'CXLVIII'),
                  (294, 'CCXCIV'),
                  (312, 'CCCXII'),
                  (421,'CDXXI'),
                  (528,'DXXVIII'),
                  (621,'DCXXI'),
                  (782,'DCCLXXXII'),
                  (870,'DCCCLXX'),
                  (941,'CMXLI'),
                  (1043,'MXLIII'),
                  (1110,'MCX'),
                  (1226,'MCCXXVI'),
                  (1301,'MCCCI'),
                  (1485,'MCDLXXXV'),
                  (1509,'MDIX'),
                  (1607,'MDCVII'),
                  (1754,'MDCCLIV'),
                  (1832,'MDCCCXXXII'),
                  (1993,'MCMXCIII'),
                  (2074,'MMLXXIV'),
                  (2152,'MMCLII'),
                  (2212,'MMCCXII'),
                  (2343,'MMCCCXLIII'),
                  (2499,'MMCDXCIX'),
                  (2574, 'MMDLXXIV'),
                  (2646, 'MMDCXLVI'),
                  (2723, 'MMDCCXXIII'),
                  (2892, 'MMDCCCXCII'),
                  (2975, 'MMCMLXXV'),
                  (3051, 'MMMLI'),
                  (3185, 'MMMCLXXXV'),
                  (3250, 'MMMCCL'),
                  (3313, 'MMMCCCXIII'),
                  (3408, 'MMMCDVIII'),
                  (3501, 'MMMDI'),
                  (3610, 'MMMDCX'),
                  (3743, 'MMMDCCXLIII'),
                  (3844, 'MMMDCCCXLIV'),
                  (3888, 'MMMDCCCLXXXVIII'),
                  (3940, 'MMMCMXL'),
                  (3999, 'MMMCMXCIX'))

    def testToRomanKnownValue(self):
        for integer, numeral in self.knowValues:
            result = r0.toRoman(integer)
            self.assertEqual(numeral,result)

    def testFromRomanKnownValues(self):
        for integer, numeral in self.knowValues:
            result = r0.fromRoman(numeral)
            self.assertEqual(integer,result)


if __name__ == "__main__":
    number = [1,5,10,50,100,500,1000]
    alpha = ['I','V','X','L','C','D','M']
    temp = ''
    for i in range(3999):
        print(r0.toRoman(i))
        temp = r0.toRoman(i)
        print(r0.fromRoman(temp))
    print('-------------------------')
    for i in range(3999):
        print(r1.toRoman(i))
        temp = r1.toRoman(i)
        print(r1.fromRoman(temp))
    print('-------------------------')
    for i in range(3999):
        print(r2.toRoman(i))
        temp = r2.toRoman(i)
        print(r2.fromRoman(temp))
    print('-------------------------')
    for i in range(3999):
        print(r3.toRoman(i))
        temp = r3.toRoman(i)
        print(r3.fromRoman(temp))
    print('-------------------------')
    for i in range(3999):
        print(r4.toRoman(i))
        temp = r4.toRoman(i)
        print(r4.fromRoman(temp))