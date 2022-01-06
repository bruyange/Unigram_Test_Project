"""
Henry Udenze
CS-141
The wordLength program file is one which is supposed to take in a dictionary with keys of words and values of a list of year count objects that are attributed to each word.
"""

from wordData import *
from boxAndWhisker import *

def Calc(Vallst,Val,i):
    """Helper function to calculate Median,1st quartile and 3rd quartile
    Vallst: List of tuples of wordlengths and their number of occurences.
    Val: The particular value to be used for this calculation. MidValue for median, the total/4 for the 1st quartile and the total*3/4 for the 3rd Quartile Value
    i: Tracker Value. Always starts at 0"""
    Val=(Val)-Vallst[i][1]
    if Val>0:
        return Calc(Vallst,Val,i+1)
    elif Val<=0:
            return Vallst[i][0]



def summaryFromWords(words, year):
    """Takes in initial dictionary of words and yearcount objects and also takes in a year of consideration
    It then returns a tuple of the 5 number summary of the data"""
    table4={}  #Dictionary of year as key and value as a list of all the words printed in that year
    table5={}  #Dictionary of the word as the key and value as the number of times it occured in the particular user inputted year
    table6={}  #Dictionary of the word lengths (e.g 1, 2,3 or 16) as the key and value as the number of times words of the respective lengths appeared in the user inputted year
    for word in words:
        for i in words[word]:
            lst=[]
            if year==i.year:
                if i.year in table4:
                    table4[i.year].append(word)
                elif i.year not in table4:
                    lst.append(word)
                    table4[i.year]=lst
    for a in words:
        for b in words[a]:
            if year==b.year:
                if a in table5:
                    table5[a]+=b.count
            elif a not in table5:
                    table5[a]=b.count

    for i in table4[year]:
        count=len(i)
        if count in table6:
            y=table5[i]
            table6[count]+=y
        elif count not in table6:
            y=table5[i]
            table6[count] = y



    Vallst=list(table6.items())
    Vallst.sort()
    TotalVal=0
    for i in Vallst:
        TotalVal+=i[1]
    MidVal=TotalVal//2
    min=Vallst[0][0]
    max=Vallst[-1][0]
    Q1Value=TotalVal//4
    Q3Value=(TotalVal//4)*3
    median=Calc(Vallst,MidVal,0)
    q1=Calc(Vallst,Q1Value,0)
    q3=Calc(Vallst,Q3Value,0)
    Answer= (min,q1,median,q3,max)
    return Answer


def main():
    """
    Runs wordLength and summaryfromWords function to return the 5 word summary
    :return:
    """

    filename=input("Input filename to check:  ")
    table=readWordFile(filename)
    year=int(input('Enter Year to check: '))
    stuff=summaryFromWords(table,year)
    print("minimum: " + str(stuff[0]))
    print("1st quartile: " + str(stuff[1]))
    print("median: " + str(stuff[2]))
    print("3rd quartile: " + str(stuff[3]))
    print("maximum: " + str(stuff[4]))

    boxAndWhisker(int(stuff[0]), int(stuff[1]), int(stuff[2]), int(stuff[3]), int(stuff[4]))

if __name__ == '__main__':
    main()