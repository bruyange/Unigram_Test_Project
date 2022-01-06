"""
Test functions for the statistics module.
file: testStatistics.py
author: Arthur Nunes-Harwitt
"""

from wordData import readWordFile

from wordLength import summaryFromWords

def test(computed, expected):
    """
    test: (NatNum or Float)^5 (NatNum or Float)^5 -> Boolean
    effect: when computed is not equal to expected generate message
    """
    if computed == expected:
        return True
    else:
        print('Got: ', computed, ', but expected', expected)
        return False

def testFileName(filename, year, expected):
    """
    testFileName: String NatNum (NatNum or Float)^5 -> Boolean
    """
    return test(summaryFromWords(readWordFile(filename), year), expected)

def testAll():
    """
    testAll: Void -> NoneType
    """
    passed = True

    passed = testFileName('very_short.txt', 2007, (7,7,7,7,8)) and passed

    passed = testFileName('a.txt', 1901, (1,2,3,4,16)) and passed
    passed = testFileName('a.txt', 2001, (1,2,3,5,16)) and passed

    if passed:
        print('Passed all tests.')


if __name__ == '__main__':
    testAll()

