"""
Henry Udenze
CS-141
boxAndWhisker.py
boxAndWhisker is a program that takes in a 5 numbered tuple and draws a box and whisker plot according to the summary
"""




import turtle as tt

def boxAndWhisker(small, q1, med, q3, large):
    """this function draws the plot
    small=minimum value
    q1=1st quartile value
    med=Median Value
    q3=Third quartile value
    large=max value
    """

    initialize()
    tt.down()
    tt.left(90)
    tt.forward((q1-small)*2)
    tt.right(90)
    tt.forward(15)
    tt.back(30)
    tt.forward(15)
    tt.right(90)
    tt.forward((q1-small)*2)
    tt.left(90)
    tt.forward(40)
    tt.right(90)
    tt.forward((med-q1)*2)
    tt.back((med-q1)*2)
    tt.right(90)
    tt.forward(80)
    tt.left(90)
    tt.forward((med-q1)*2)
    tt.left(90)
    tt.forward(80)
    tt.right(90)
    tt.forward((q3-med)*2)
    tt.right(90)
    tt.forward(80)
    tt.right(90)
    tt.forward((q3-med)*2)
    tt.right(180)
    tt.forward((q3-med)*2)
    tt.left(90)
    tt.forward(40)
    tt.right(90)
    tt.forward((large-q3)*2)
    tt.left(90)
    tt.forward(15)
    tt.back(30)



    tt.done()

def initialize():
    """initializes the turtle cursor to be facing up"""
    tt.up()
    tt.left(90)



def main():
    """Asks user for input and calls boxAndWhisker function"""

    small=int(input("Enter the minimum: "))
    q1=int(input("Enter the first quartile: "))
    med=int(input("Enter the median: "))
    q3 = int(input("Enter the third quartile: "))
    large=int(input("Enter the maximum: "))


    boxAndWhisker(small, q1, med, q3, large)

if __name__ == '__main__':
    main()



