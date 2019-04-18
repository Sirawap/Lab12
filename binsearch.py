class BinsearchError(Exception): pass
class OutOfRangeError(BinsearchError): pass
class NotIntegerError(BinsearchError): pass
class InvalidRomanNumeralError(BinsearchError): pass

def binsearch(dataList, key):
    first = 0
    count = len(dataList)
    while 0 < count:
        step = int(count / 2)
        mid = first + step

        if dataList[mid] > key:
            mid += 1
            first = mid
            count -= step + 1
        else:
            count = step

    return first

print(binsearch([1,2,3,4,5],3))
