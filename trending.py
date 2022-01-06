"""
Henry Udenze
CS-141
trending is a program file that takes in our dictionary returned in wordData, a user inputted start year and end year and
returns a list containing a WordTrend entry for each word for which qualifying data exists.
The list is sorted in decreasing trend value.
"""

from wordData import *

def trending(words, startYr, endYr):
    """

    :param words: initial dictionary from wordData
    :param startYr: User inputted start year for search
    :param endYr: User inputted end year for search
    :return:lst(list of WordTrend objects)
    """
    lst=[]

    for key in words:
        s=0
        e=0
        for i in words[key]:
            if i.year==startYr:
                if i.count>=1000:
                    s+=i.count
            elif i.year==endYr:
                if i.count>=1000:
                    e+=i.count
        if s!=0 and e!=0:
            WT=WordTrend(str(key),float(e/s))
            lst.append(WT)
    lst.sort(key=lambda y:y.trend, reverse=True)
    return lst


def main():
    """
    Runs trending function
    :return:Top 10 trending and Bottom trending words
    """
    filename=input("enter:")
    first=readWordFile(filename)
    stYr=int(input("enter start"))
    enYr=int(input("enter end"))
    lst=(trending(first,stYr,enYr))
    print("The top 10 trending words from " + str(stYr) + " to " + str(enYr) + " are : ")
    if len(lst)>=10:
        for x in lst[:10]:
            print(x.word)
    elif len(lst)<10:
        for x in lst:
            print(x.word)



    print("\n")
    print("The bottom 10 trending words from " + str(stYr) + " to " + str(enYr) + " are : ")
    lst1=[]
    if len(lst)>=10:
        for x in lst[(len(lst)-10):]:
            lst1.append(x.word)
    elif len(lst)<10:
        for x in lst:
            lst1.append(x.word)
        #print(x.word)
    for i in reversed(lst1):
        print(i)


if __name__ == '__main__':
    main()



