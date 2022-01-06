"""
Project: Unigrams
Task One: Letter Frequencies

This is a test program that students can use to verify that they are
able to compute the correct letter frequency string using the unigram file
'a.txt'.  It implicitly tests that the file is read correctly, and also
explicitly tests that the totalOccurrences function is correctly
counting the occurrences of words.

Author: Sean Strout (sps@cs.rit.edu)
Author: Aaron Deever atd@cs.rit.edu
Language: Python 3
"""

import letterFreq   # letterFreq
import wordData     # readFile, totalOccurrences

def testA():
    WORD_OCCURRENCES = {'airplane' : 2487028,
                        'alien' : 5400198,
                        'accept' : 26299474}

    LETTER_FREQ_STRING = 'andetsrliocupgmybhvfwkxqjz'
    

    print('Testing with a.txt...\n')
    words = wordData.readWordFile('a.txt')

    # test totalOccurrences
    for word in WORD_OCCURRENCES:
        print('Total occurrences of', word + ':',
              'OK' if wordData.totalOccurrences(word, words) == WORD_OCCURRENCES[word] \
                else 'GOT: ' + str(wordData.totalOccurrences(word, words)) +
                     ', EXPECTED: ' + str(WORD_OCCURRENCES[word]))

    freqString = letterFreq.letterFreq(words)
    if freqString == LETTER_FREQ_STRING:
        print('\nFrequency ordering of letters OK')
    else:
        print('Frequency ordering of letters incorrect.') 
        print('GOT: ' + freqString)
        print('EXPECTED: ' + LETTER_FREQ_STRING)

if __name__ == '__main__':
    testA()
