import collections
def fizzbuzz():
    for x in range(1,101):
        if x%5==0 and x%3==0:
            x="Fizbuzz"
        elif x%5==0:
            x="Buzz"
        elif x%3==0:
            x="Fizz"
        print(x)

fizzbuzz()


Person=collections.namedtuple('Person', 'name age gender')
bob=Person(name='Bob',age=50,gender='Male')
print()
print(bob.age)
