def buat_vector():
    vector_awal = []
    vector = []
    vector_kolom = []
    jmlh_elemen = int(input("Masukkan jumlah elemen: "))
    for i in range(jmlh_elemen):
        el = int(input(f'Masukkan elemen ke-{i+1}: '))
        vector_awal.append(el)
        vector_kolom.append(el)
        vector.append(vector_kolom)
        vector_kolom = []
    print(vector)
    print("=" * 50)
    pil = input("Apakah ingin men-Transpose vectornya? (y/n): ").lower()
    if pil == "y":
        for i in range(jmlh_elemen):
            print(vector[i])
            i += 1
    
def buat_matrix():
    matrix = []
    matrix_tambah = []
    jmlh_baris = int(input("Masukkan jumlah baris: "))
    jmlh_kolom = int(input("Masukkan jumlah kolom: "))
    for i in range(jmlh_baris):
        for j in range(jmlh_kolom):
            nilai_baris = int(input(f'Masukkan baris ke-{i+1}, kolom ke-{j+1}: '))
            matrix_tambah.append(nilai_baris)
        matrix.append(matrix_tambah)
        matrix_tambah = []
        print(matrix)
    print("=" * 50)
    for p in range(jmlh_baris):
        print(matrix[p])
        p += 1
    pil = input("Apakah ingin men-Transpose matrixnya? (y/n): ").lower()
    if pil == "y":
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for r in result:
            print(r)
        
def main():
    run = True
    while run:
        print("1. Buat vector")
        print("2. Buat matrix")
        pil = int(input("Masukkan pilihan menu (0 untuk keluar): "))
        if pil == 1:
            buat_vector()
            n = input("Apakah ingin lanjut? (y/n): ").lower()
            if n == "y":
                run = True
                print()
            else:
                run = False
        elif pil == 2:
            buat_matrix()
            n = input("Apakah ingin lanjut? (y/n): ").lower()
            if n == "y":
                run = True
                print()
            else:
                run = False
        elif pil == 0:
            run = False
    
    
if __name__ == "__main__":
    main()