from flask import Flask #import library Flask
app = Flask(__name__) #membuat objek

#membuat rute home pemjumlahan dan pengurangan
@app.route('/')
def home():
    return '<a href="/penjumlahan">Penjumlahan</a> <a href="/pengurangan">Pengurangan</a>'

### Buatlah halaman untuk menjumlahkan 2 nilai dari variable
@app.route('/penjumlahan')
def jumlah_nilai():
    a = 3
    b = 5

    # Hitung hasil penjumlahan
    hasil = a + b

    # Tampilkan hasil penjumlahan
    return f'Hasil penjumlahan {a} + {b} adalah {hasil}'

### Buatlah halaman untuk mengurangi 2 nilai dari variable
@app.route('/pengurangan')
def pengurangan_nilai():
    a = 13
    b = 6

    # Hitung hasil pengurangan
    hasil = a - b

    # Tampilkan hasil pengurangan
    return f'Hasil pengurangan {a} - {b} adalah {hasil}'

#menjalankan aplikasi flask
if __name__ == '__main__':
    app.run()
    
#Running on http://127.0.0.1:5000
#1. Aplikasi Flask  berjalan pada alamat http://127.0.0.1:5000.
#2. 127.0.0.1 adalah alamat IP loopback, yang merujuk ke komputer.
#3. 5000 adalah port yang digunakan oleh server Flask.
