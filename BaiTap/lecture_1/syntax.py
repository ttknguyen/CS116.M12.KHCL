def line():
    print('____________________________________________________')

def conditional_syntax():
    line()
    print('\tCONDITIONAL SYNTAX:')

    temp = 60
    if temp > 100:
        print("REALLY HOT")
    elif temp > 85:
        print("HOT")
    elif temp > 60:
        print("COMFORTABLE")
    else:
        print('COLD')
    
    print()
    line()

def loop_on_List():
    print('\tLOOP ON LIST:')

    animals = ['cat', 'dog', 'monkey']
    for item in animals:
        print(item)
    for index, item in enumerate(animals):
        print("#%d: %s" % (index, item))


    print()
    line()

def loop_on_dict():
    print('\tLOOP ON DICTIONARY:')

    d = {'fish': 0, 'cat': 4, 'spider': 8}
    print(d['spider'])
    print(d.keys())
    print(d.values())
    
    for animal, legs, in d.items():
        print("A %s has %d legs" % (animal, legs))

    print()
    line()

def function():
    print('\tFUNCTION:')
    def sign(x):
        if(x > 0):
            return 'positive'
        elif (x < 0):
            return 'negative'
        else:
            return 'zero'
    
    def f(a, b = 2, c = 3):
        print('a =', a)
        print('b =', b)
        print('c =', c)

    print('Function 1:')
    for x in [0, 5, -1]:
        print("Input: %d, Output: %s" % (x, sign(x)))
    print()
    print('Function 2:')
    f(3, -1, 1.5)
    f(1)
    f(1, 2)
    f(a=0.5, c=4)

    print()
    line()
    
class Greeter():
    def __init__(self, name):
        self.name = name
    
    def greet(self, loud=False):
        if (loud):
            print("HELLO, %s" % (self.name))
        else:
            print("hello, %s" % (self.name))




def main():
    conditional_syntax()
    loop_on_List()
    loop_on_dict()
    function()

    g = Greeter("TTKN")
    g.greet()
    g.greet(loud=True)
    
if __name__ == '__main__':
    main()