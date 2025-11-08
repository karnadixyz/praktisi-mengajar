def luas_lingkaran(r):
    """
    Menghitung luas lingkaran.

    Parameters:
    jari_jari (float): Jari-jari lingkaran.

    Returns:
    float: Luas lingkaran.
    """
    pi = 3.14
    luas = pi * r ** 2
    return luas

def main():
    print("Program Menghitung Luas Lingkaran")
    try:
        r = float(input("Masukkan jari-jari lingkaran (cm): "))
        
        luas = luas_lingkaran(r)
        print(f"Luas lingkaran dengan jari-jari {r} cm adalah {luas} cm²")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        
if __name__ == "__main__":
    main()