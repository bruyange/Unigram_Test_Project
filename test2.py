import collections



YearCount=collections.namedtuple('YearCount','Year Count')





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
            YCLst.append(YearCount(Year=int(lines[0]),Count=int(lines[1])))
            oldLine=lines
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
            totalOccur+=i.Count
        return totalOccur
    else:
        return 0



def main():
    file=input("Enter filename to be checked: ")
    x=(readWordFile(file))
    print(x)
    print(totalOccurrences('airport',x))

main()