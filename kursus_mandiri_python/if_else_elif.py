def main():
    no = int(input('Masukkan nomor hari [1..7]: '))

    if no == 1:
        print('Minggu')
    elif no == 2:
        print('Senin')
    elif no == 3:
        print('Selasa')
    elif no == 4:
        print('Rabu')
    elif no == 5:
        print('Kamis')
    elif no == 6:
        print('Jumat')
    elif no == 7:
        print('Sabtu')
    else:
        print('Nilai yang dimasukkan salah.')

if __name__=='__main__':
    main()