def line():
    print('____________________________________________________')

def Float_Int():
    print("\tFLOAT & INT:")

    x = 3

    print(type(x))
    print(x)
    print(x + 1)
    print(x - 1)
    print(x * 2)
    print(x ** 2)

    x += 1
    print(x)

    x *= 2
    print(x)
    print(x, x + 5, x * 2, x ** 2)
    print(x % 5, x / 5, x // 5)

    print()
    line()

def Boolean():
    print("\tBOOLEAN:")

    t = True
    f = False

    print(type(t))
    print(t and f)
    print(t or f)
    print(not t)
    print(t != f)

    print()
    line()

def String():
    print("\tString:")

    hello = 'Hello'
    world = 'world'
    print(hello)
    print(world)

    hw = hello + world
    print(hw)

    hw12 = '%s %s %d' % (hello, world, 12)
    print(hw12)

    s = 'hello'
    print(s.upper())
    print(s.capitalize())
    print(s.replace('l', 'lle'))
    print(s.find('el'))
    print(' world '.strip())

    print()
    line()

def List():
    print("\tList:")

    xs = [3, 2, 1]
    print(xs, xs[2])
    print(xs[-1])
    xs[2] = 'foo'
    print(xs)
    x = xs.pop()
    print(x, xs)

    nums = list(range(5))
    print(nums)
    print(nums[2:4])
    print(nums[2:])
    print(nums[:2])
    print(nums[:])
    print(nums[:-1])
    nums[2:4] = [8, 9]
    print(nums)
    
    print()
    line()

def Dictionary():
    print('\t DICTIONARY:')

    d = {'cat': 'cute', 'dog': 'furry'}
    print(d['cat'])
    print('cat' in d)
    d['fish'] = 'wet'
    print(d['fish'])
    print(d.get('rat'))
    print(d.get('monkey', 'N/A'))

    print()
    line()

def Set():
    print('\t SET:')

    animals = {'cat', 'dog'}
    print('cat' in animals)
    print('fish' in animals)
    animals.add('fish')
    print('fish' in animals)
    print(len(animals))
    animals.add('cat')
    print(len(animals))
    animals.remove('cat')
    print(len(animals))

    print()
    line()

def Tuple():
    print('\t TUPLE:')

    t = (5, 6)
    print(type(t))

    a, b, = t
    print(a, b)

    t2 = t + (7, 8)
    print(t2, t2[0])
    #t2[0] = 4

    print()
    line()


def main():
    line()
    Float_Int()
    Boolean()
    String()
    List()
    Dictionary()
    Set()
    Tuple()

if __name__ == '__main__':
    main()