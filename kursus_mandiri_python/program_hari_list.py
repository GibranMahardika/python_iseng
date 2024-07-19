import sys

def main():
    hari = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']

    no = int(input('Memasukkan nomor hari [1..7]: '))

    if no < 1 or no > 7:
        print('Nilai yang dimasukkan salah.')
        sys.exit()

    print(hari[no-1])

if __name__ == '__main__':
    main()