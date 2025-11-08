def hitung_luas_segitiga(alas, tinggi):
    """
    Menghitung luas segitiga.

    Parameters:
    alas (float): Panjang alas segitiga.
    tinggi (float): Tinggi segitiga.

    Returns:
    float: Luas segitiga.
    """
    luas = 2 * alas * tinggi
    return luas

def main():
    print("Program Menghitung Luas Segitiga")
    try:
        alas = float(input("Masukkan panjang alas segitiga (cm): "))
        tinggi = float(input("Masukkan tinggi segitiga (cm): "))
        
        luas = hitung_luas_segitiga(alas, tinggi)
        print(f"Luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah {luas} cm²")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
    
if __name__ == "__main__":
    main()