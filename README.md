# 🚲 Bike Sharing Analysis Project
Project Akhir Belajar Analisis Data dengan Python | Dicoding
## ⌨️ Setup Environment - Shell/Terminal
- mkdir Submission
- cd Submission
- pipenv install
- pipenv shell
- pip install -r requirements.txt

## 🏃 Run Streamlit-app
- cd Dashboard
- streamlit run dashboard.py

## 🗒️ Analisis Data dengan Python
**Mendefinisikan pertanyaan bisnis**
Pertanyaan 1: Bagaimana pengaruh waktu terhadap jumlah penyewaan sepeda?
Pertanyaan 2: Bagaimana perbandingan pola penyewaan sepeda pada hari kerja dan akhir pekan?
Pertanyaan 3: Apa pengaruh cuaca terhadap jumlah penyewaan sepeda?
Pertanyaan 4: Bagaimana pola penyewaan sepeda berdasarkan hari dalam seminggu (weekday)?
Pertanyaan 5: Bagaimana hubungan antara jumlah penyewaan pengguna terdaftar (registered) dan pengguna kasual (casual)?
Pertanyaan 6: Bagaimana pengaruh workingday terhadap penyewaan sepeda untuk pengguna kasual dan terdaftar?


**📖 Kesimpulan yang didapat**
1. Pengaruh Waktu terhadap Jumlah Penyewaan Sepeda
Kesimpulan: Penyewaan sepeda menunjukkan pola yang jelas terkait waktu. Aktivitas penyewaan meningkat tajam pada pagi hari (sekitar pukul 08:00) dan sore hari (sekitar pukul 17:00), yang kemungkinan besar disebabkan oleh perjalanan kerja atau sekolah. Hal ini menunjukkan bahwa sepeda digunakan sebagai moda transportasi pada jam sibuk.

2. Perbandingan Pola Penyewaan Sepeda pada Hari Kerja dan Akhir Pekan
Kesimpulan: Jumlah penyewaan sepeda relatif seimbang antara hari kerja dan akhir pekan, tetapi pola penggunaannya mungkin berbeda. Hari kerja lebih didominasi oleh pengguna terdaftar, sedangkan akhir pekan lebih banyak digunakan oleh pengguna kasual untuk rekreasi.

3. Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda
Kesimpulan: Dari heatmap korelasi, terlihat bahwa faktor seperti temperatur (temp) memiliki korelasi positif terhadap jumlah penyewaan sepeda. Sebaliknya, kelembapan (hum) dan kecepatan angin (windspeed) memiliki korelasi negatif. Artinya, cuaca yang nyaman (suhu sedang, kelembapan rendah, dan angin tidak terlalu kencang) mendorong lebih banyak penyewaan sepeda.

4. Pola Penyewaan Sepeda Berdasarkan Hari dalam Seminggu
Kesimpulan: Penyewaan sepeda cenderung merata sepanjang minggu, tetapi sedikit menurun pada hari kerja tertentu (seperti Senin). Akhir pekan mungkin menunjukkan sedikit kenaikan, terutama untuk pengguna kasual.

5. Hubungan antara Pengguna Terdaftar (Registered) dan Kasual (Casual)
Kesimpulan: Ada perbedaan yang jelas antara pola penggunaan sepeda oleh pengguna terdaftar dan kasual. Pengguna terdaftar cenderung lebih konsisten setiap hari, terutama pada jam sibuk hari kerja. Pengguna kasual lebih banyak pada akhir pekan atau hari-hari libur, menunjukkan orientasi rekreasi.

6. Pengaruh Workingday terhadap Penyewaan Sepeda
Kesimpulan: Hari kerja (workingday) memiliki pengaruh besar terhadap pola penyewaan. Pengguna terdaftar mendominasi pada hari kerja, sementara pengguna kasual lebih aktif pada hari libur. Ini mengindikasikan bahwa pengguna terdaftar lebih menggunakan sepeda untuk keperluan fungsional, sedangkan pengguna kasual lebih untuk rekreasi.

Streamlit Dashboard Analisis Data Bike Sharing Dataset by Richo Albert Tio bisa diakses di => 