"""
Project: Unigrams
Task Three: Word Trends

This is a test program that students can use to verify that they are
able to compute the correct word trending results using the
file 'a.txt'

Author: Sean Strout (sps@cs.rit.edu)
Author: Aaron Deever atd@cs.rit.edu
Language: Python 3
"""

__author__ = 'sps'

import wordData     # readWordFile
import trending     # trending

def testA():
    """
    Test function for 'a.txt'.
    :return: None
    :rtype: NoneType
    """

    # expected results
    # each tuple contains startYr/endYr/index/word
    # index 0 is the highest trending word, -1 is lowest
    TRENDS = ((1927, 1931, 0, 'av'),
              (1927, 1931, -1, 'acetate'),
              (1950, 1952, 0, 'antibiotics'),
              (1950, 1952, -1, 'atque'),
              (1966, 1975, 0, 'algorithms'),
              (1966, 1975, -3, 'aeroplanes'),
              (1981, 2008, 1, 'authentication'),
              (1981, 2008, -2, 'antisera'))


    print('Testing with a.txt...\n')
    words = wordData.readWordFile('a.txt')

    for idx in range(len(TRENDS)):
        print("testing: ",TRENDS[idx][0], "to", TRENDS[idx][1])
        trendList = trending.trending(words, TRENDS[idx][0], TRENDS[idx][1])
        if(trendList[TRENDS[idx][2]].word == TRENDS[idx][3]):
            print("OK!")
        else:
            print("got:",trendList[TRENDS[idx][2]].word)
            print("expected: ", TRENDS[idx][3])

if __name__ == '__main__':
    testA()

