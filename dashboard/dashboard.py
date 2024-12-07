# Import library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os


# Baca dataset
file_path_day = 'data/day.csv'  # Ganti dengan path sebenarnya ke file CSV Anda
file_path_hour = 'data/hour.csv'  # Ganti dengan path sebenarnya ke file CSV Anda
data_day = pd.read_csv(file_path_day)
data_hour = pd.read_csv(file_path_hour)


# Konversi kolom tanggal ke format datetime
data_hour['dteday'] = pd.to_datetime(data_hour['dteday'])
data_day['dteday'] = pd.to_datetime(data_day['dteday'])

# Menampilkan judul aplikasi
st.title('🚲 Bike Sharing Analysis by Richo ')

# **Pertanyaan 1: Pengaruh Waktu terhadap Jumlah Penyewaan Sepeda**
st.header('1. Pengaruh Waktu terhadap Jumlah Penyewaan Sepeda')

# Visualisasi
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=data_hour.groupby('hr').mean().reset_index(), ax=ax1)
ax1.set_title('Pengaruh Jam terhadap Jumlah Penyewaan Sepeda', fontsize=16)
ax1.set_xlabel('Jam', fontsize=12)
ax1.set_ylabel('Rata-rata Penyewaan Sepeda', fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Tampilkan grafik di Streamlit
st.pyplot(fig1)

# **Pertanyaan 2: Perbandingan Pola Penyewaan Sepeda pada Hari Kerja dan Akhir Pekan**
st.header('2. Perbandingan Pola Penyewaan Sepeda pada Hari Kerja dan Akhir Pekan')

# Visualisasi
avg_rental_by_workingday = data_hour.groupby('workingday')['cnt'].mean()
fig2, ax2 = plt.subplots(figsize=(8, 5))
colors = ['#FF6F61', '#6BAED6']
ax2.bar(avg_rental_by_workingday.index, avg_rental_by_workingday.values, color=colors)
ax2.set_xticks([0, 1])
ax2.set_xticklabels(['Akhir Pekan', 'Hari Kerja'], fontsize=12)
ax2.set_title('Perbandingan Penyewaan Sepeda (Hari Kerja vs Akhir Pekan)', fontsize=16)
ax2.set_xlabel('Tipe Hari', fontsize=12)
ax2.set_ylabel('Rata-rata Penyewaan Sepeda', fontsize=12)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Tampilkan grafik di Streamlit
st.pyplot(fig2)

# **Pertanyaan 3: Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda**
st.header('3. Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')

# Korelasi antara fitur cuaca dan penyewaan sepeda
corr_features = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']
corr_matrix = data_day[corr_features].corr()

# Heatmap korelasi
fig3, ax3 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax3)
ax3.set_title('Korelasi Variabel Cuaca dengan Total Penyewaan Sepeda', fontsize=16)

# Tampilkan heatmap di Streamlit
st.pyplot(fig3)

# **Pertanyaan 4: Pola Penyewaan Sepeda Berdasarkan Hari dalam Seminggu**
st.header('4. Pola Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')

# Visualisasi
avg_rental_by_weekday = data_hour.groupby('weekday')['cnt'].mean()
fig4, ax4 = plt.subplots(figsize=(8, 6))
ax4.bar(avg_rental_by_weekday.index, avg_rental_by_weekday.values, color='#4CAF50')
ax4.set_xticks([0, 1, 2, 3, 4, 5, 6])
ax4.set_xticklabels(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'], fontsize=10)
ax4.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Hari', fontsize=14)
ax4.set_xlabel('Hari dalam Seminggu', fontsize=12)
ax4.set_ylabel('Rata-rata Penyewaan Sepeda', fontsize=12)
ax4.grid(axis='y', linestyle='--', alpha=0.7)

# Tampilkan grafik di Streamlit
st.pyplot(fig4)

# **Pertanyaan 5: Hubungan antara Pengguna Terdaftar (Registered) dan Kasual (Casual)**
st.header('5. Hubungan antara Pengguna Terdaftar (Registered) dan Kasual (Casual)')

# Visualisasi scatter plot
fig5, ax5 = plt.subplots(figsize=(8, 6))
sc = ax5.scatter(data_hour['casual'], data_hour['registered'], alpha=0.6, c=data_hour['cnt'], cmap='viridis')
plt.colorbar(sc, ax=ax5, label='Total Penyewaan')
ax5.set_title('Hubungan Jumlah Penyewaan Pengguna Terdaftar vs Kasual', fontsize=14)
ax5.set_xlabel('Penyewaan Pengguna Kasual', fontsize=12)
ax5.set_ylabel('Penyewaan Pengguna Terdaftar', fontsize=12)
ax5.grid(linestyle='--', alpha=0.7)

# Tampilkan scatter plot di Streamlit
st.pyplot(fig5)

# **Pertanyaan 6: Pengaruh Workingday terhadap Penyewaan Sepeda**
st.header('6. Pengaruh Workingday terhadap Penyewaan Sepeda')

# Visualisasi bar plot
avg_rental_workingday = data_hour.groupby('workingday')[['casual', 'registered']].mean()
fig6, ax6 = plt.subplots(figsize=(8, 6))
avg_rental_workingday.plot(kind='bar', ax=ax6, color=['#FFC107', '#2196F3'])
ax6.set_xticks([0, 1])
ax6.set_xticklabels(['Akhir Pekan', 'Hari Kerja'], rotation=0, fontsize=12)
ax6.set_title('Pengaruh Hari Kerja terhadap Penyewaan Kasual dan Terdaftar', fontsize=14)
ax6.set_xlabel('Kategori Hari', fontsize=12)
ax6.set_ylabel('Rata-rata Penyewaan', fontsize=12)
ax6.legend(['Kasual', 'Terdaftar'])
ax6.grid(axis='y', linestyle='--', alpha=0.7)

# Tampilkan grafik di Streamlit
st.pyplot(fig6)

# Menampilkan kesimpulan
st.subheader("Kesimpulan:")
st.write("""
# 1. Pengaruh Waktu terhadap Jumlah Penyewaan Sepeda
**Kesimpulan**: Penyewaan sepeda menunjukkan pola yang jelas terkait waktu. Aktivitas penyewaan meningkat tajam pada pagi hari (sekitar pukul 08:00) dan sore hari (sekitar pukul 17:00), yang kemungkinan besar disebabkan oleh perjalanan kerja atau sekolah. Hal ini menunjukkan bahwa sepeda digunakan sebagai moda transportasi pada jam sibuk.

# 2. Perbandingan Pola Penyewaan Sepeda pada Hari Kerja dan Akhir Pekan
**Kesimpulan**: Jumlah penyewaan sepeda relatif seimbang antara hari kerja dan akhir pekan, tetapi pola penggunaannya mungkin berbeda. Hari kerja lebih didominasi oleh pengguna terdaftar, sedangkan akhir pekan lebih banyak digunakan oleh pengguna kasual untuk rekreasi.

# 3. Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda
**Kesimpulan**: Dari heatmap korelasi, terlihat bahwa faktor seperti temperatur (temp) memiliki korelasi positif terhadap jumlah penyewaan sepeda. Sebaliknya, kelembapan (hum) dan kecepatan angin (windspeed) memiliki korelasi negatif. Artinya, cuaca yang nyaman (suhu sedang, kelembapan rendah, dan angin tidak terlalu kencang) mendorong lebih banyak penyewaan sepeda.

# 4. Pola Penyewaan Sepeda Berdasarkan Hari dalam Seminggu
**Kesimpulan**: Penyewaan sepeda cenderung merata sepanjang minggu, tetapi sedikit menurun pada hari kerja tertentu (seperti Senin). Akhir pekan mungkin menunjukkan sedikit kenaikan, terutama untuk pengguna kasual.

# 5. Hubungan antara Pengguna Terdaftar (Registered) dan Kasual (Casual)
**Kesimpulan**: Ada perbedaan yang jelas antara pola penggunaan sepeda oleh pengguna terdaftar dan kasual. Pengguna terdaftar cenderung lebih konsisten setiap hari, terutama pada jam sibuk hari kerja. Pengguna kasual lebih banyak pada akhir pekan atau hari-hari libur, menunjukkan orientasi rekreasi.

# 6. Pengaruh Workingday terhadap Penyewaan Sepeda
**Kesimpulan**: Jumlah pengguna terdaftar lebih tinggi pada hari kerja, sedangkan pengguna kasual lebih banyak pada akhir pekan.
""")
