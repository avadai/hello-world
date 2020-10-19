f = input("Enter the file name: ")
with open(f, 'r') as f:
        print('{a:^10}{b:^10}{c:^10}'.format(a='   Last Name\t', b='Hourly Wage\t', c='Hours Worked\t'))
        print('------------------------------------')
        for i, line in enumerate(f, start=1):
                print('{}> {}'.format(i, line.strip()))
