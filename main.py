'''
long comment
'''
def hello_world(): #this will print


    print('hello world')


def hello_anything(string):
    print('hello ' + string)


if __name__ == '__main__':
    hello_world()

    input = input('what should I say hello to?')

    hello_anything(input)