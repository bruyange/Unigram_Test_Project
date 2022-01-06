"""
Henry Udenze
wordData.py
This program file reads in a filename and makes a dictionary whereby each word is the key and the 2 numerical values are
used to form a year count object and are the values for the key
"""



from rit_lib import *
class YearCount(struct):
    """Defines yearcount class"""
    _slots = ((int,'year'),(int,'count'))

class WordTrend(struct):
    """defines wordTrend class"""
    _slots=((str,'word'),(float,'trend'))

def readWordFile(fileName):
    """reads in file and builds dictionary"""
    table=dict()
    file=open(str(fileName))
    YCLst=[]
    oldLine=[]
    for lines in file:
        lines=lines.strip()
        lines=lines.split(',')


        if len(lines)==1 and len(oldLine)==2:
            keys=lines[0]
            table[keys] = YCLst
            YCLst = []

        if len(lines) == 1:
            keys = lines[0]
            table[keys]=YCLst
        elif len(lines) == 2:
            YCLst.append(YearCount(int(lines[0]), int(lines[1])))

            oldLine = lines

    file.close()

    return table





def totalOccurrences(word,table):
    """calculates total occurrence user input words
    word=word to calculate occurrence for
    table=dictionary made from readWordFile
    """
    if word in table:
        totalOccur=0
        for i in table[word]:
            totalOccur+=i.count
        return totalOccur
    else:
        return 0


def main():
    filename=input("Hello, :) Please enter the name of the file to be analysed : ")
    word=str(input("Please input your word to count: "))
    table=readWordFile(filename)
    print(table)
    val=totalOccurrences(word,table)
    print("The total number of occurences of "+str(word) +" is "+ str(val))


if __name__ == '__main__':
    main()