"""
Henry Udenze
CS-141
printedWords.py
printedWords is a program file that takes in our dictionary returned in wordData and returns the number of words printed in a user specified year.
It also makes use of simple plot to plot a graph that has this information
"""
from wordData import *
import simplePlot
def printedWords(table):
    """Ths function takes in our first dictionary and returns a list containing a YearCount entry for each year for which data exists. The list
is sorted in ascending order of year. """
    table2={}
    for x in table:

        for i in table[x]:

            if i.year in table2:
                table2[i.year]+=i.count
            elif i.year not in table2:
                table2[i.year]=i.count
    lst=[]

    for key in table2:
        YC=YearCount(key,table2[key])
        lst.append(YC)
    def rvAL(key):
        """Helper function for sorting"""
        return key.year
    yearList =sorted(lst,key=rvAL)
    return yearList
def wordsForYear(year,yearList):
    """
    Inputs:
        year: an integer representing the year being queried.
        yearList: a list of YearCount objects.

    Output:
        An integer count representing the total number of printed words for that year.
        If there is no entry in yearList for the requested year, the function returns 0.
    """
    totalCount=0
    for i in yearList:
        if year==i.year:
            totalCount+=i.count
    return totalCount



def main():
    """
    Prompts for user to input filename and year
    Draws plot of information found
    :return:None
    """
    filename=input("Enter word file: ")
    year=input("Enter year: ")
    wordsByYearList=printedWords(readWordFile(filename))
    print("Total word printed in " + str(year) + " is :"+ str(wordsForYear(int(year),wordsByYearList)))
    labels = "Year", "Total Words"
    plot = simplePlot.plot2D("Number of printed words over time", labels)
    for yc in wordsByYearList:
        point = yc.year, yc.count
        plot.addPoint(point)
    plot.display()
if __name__ == '__main__':
    main()


