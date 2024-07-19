def main():
    a = int(input('Masukkan nilai a: '))
    b = int(input('Masukkan nilai b: '))

    temp = a
    while a >= b: a -= b

    print('\n%d mod %d = %d' % (temp, b, a))

if __name__ == '__main__':
    main()