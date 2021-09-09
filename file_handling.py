f = open('test.txt', 'w')
f.write('hej')
f.close()

with open ('test.txt', 'r') as f:
    print(f.read())
