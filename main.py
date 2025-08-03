# Program pengecekan nilai siswa

# data
data_siswa = {
    "nama" : "Fikri",
    "mtk" : 90.0,
    "ipa" : 89.0,
    "ips" : 80.0,
}

# function
def nilai():
    nilai_angka = [v for v in data_siswa.values() if isinstance(v, (int, float))]
    total = sum(nilai_angka)
    rata2 = total // len(nilai_angka)
    print(f"Rata-rata nilai: {rata2}")

nilai()