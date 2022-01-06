"""
Henry Udenze
letterFreq.py
letterFreq is a function that takes in our wordData dictionary and returns a string of all the letters of the words
that occurred in that dictionary in descending order of their frequency.
"""


from wordData import *


def letterFreq(table):
    """

    :param table: Word to List of yearcounts dictionary
    :return: string of characters in descending order of frequency
    """
    table1={}
    lst=[]
    for key in table:
        occur=totalOccurrences(key,table)
        for letter in key:

            if letter in table1:
                table1[letter]+=occur

            elif letter not in table1:
                table1[letter]= occur
    for ke in table1:
        lst.append(ke)

    def rvAL(key):
        return table1[key]
    lst2 =sorted(lst,key=rvAL)
    letters=""
    for bi in lst2:
        letters=bi + letters
    Alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in Alph:
        if i not in letters:
            letters=letters + i

    return letters





def main():
    """
    Prompts user for input file
    Calls letterFreq function
    :return:None
    """
    filename=input("Enter word file: ")
    print("Letters sorted by decreasing frequency is: " +(letterFreq(readWordFile(filename))))
    print (readWordFile(filename))

if __name__ == '__main__':
    main()
