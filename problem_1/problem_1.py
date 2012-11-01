import unittest


class TestSumMultiples(unittest.TestCase):
    ''' Problem 1 - 05 October 2001
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.'''
    def setUp(self):
        self.result = sum_multiples(10)

    def test_sum(self):
        self.assertEqual(self.result, 23)


def sum_multiples(limit):
    sum = 0
    for number in xrange(1, limit):
        multiple_3 = (number % 3)
        multiple_5 = (number % 5)
        if multiple_3 == 0 and multiple_5 == 0:
            sum += number
        elif multiple_3 == 0:
            sum += number
        elif multiple_5 == 0:
            sum += number
    return sum

if __name__ == '__main__':
    ''' Find the sum of all the multiples of 3 or 5 below 1000.'''
    print(sum_multiples(1000))
