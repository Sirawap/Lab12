import roman0 as r0
import roman1 as r1
import roman2 as r2
import roman3 as r3
import roman4 as r4
import unitest

class KnownValue(unittest.TestCase):
    knowValues = ((1,'I'),
                  (2,'II'))
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