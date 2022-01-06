"""
Project: Unigrams
Task Two: Number of Printed Words

This is a test program that students can use to verify that they are
able to compute the correct total number of printed words
based on the input file 'z.txt'.

Author: Sean Strout (sps@cs.rit.edu)
Author: Aaron Deever atd@cs.rit.edu
Language: Python 3
"""

__author__ = 'sps'

import wordData     # readWordFile
import printedWords     # printedWords, wordsForYear

def testZ():
    """
    Test function for 'z.txt'.
    :return: None
    :rtype: NoneType
    """

    # Expected results from z.txt
    WORDS = ((1900,136049), (1931,155940), (1964,581610), (2008,2450556))

    # read in the words
    print('Testing with z.txt...')
    words = wordData.readWordFile('z.txt')

    # get the list of words for each year
    wordsByYearList = printedWords.printedWords(words)

    for idx in range(len(WORDS)):
        print("Testing year", WORDS[idx][0])
        got = printedWords.wordsForYear(WORDS[idx][0], wordsByYearList)
        if(got == WORDS[idx][1]):
            print("OK")
        else:
            print("GOT:",got,"EXPECTED:",WORDS[idx][1])
            
if __name__ == '__main__':
    testZ()
