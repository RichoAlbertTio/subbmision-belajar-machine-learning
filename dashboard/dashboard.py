# Import library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Konfigurasi layout Streamlit
st.set_page_config(
    page_title="Analisis Data - Bike Sharing",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar untuk navigasi
with st.sidebar:
    st.title("Menu")
    menu = st.radio("Pilih Halaman:", ["Analisis Data", "Biodata Pengguna"])

# Fungsi utama untuk membaca dan memproses data
@st.cache
def load_data():
    # Ganti path dengan lokasi file Anda
    file_path_day = 'data/day.csv'  
    file_path_hour = 'data/hour.csv'  
    data_day = pd.read_csv(file_path_day)
    data_hour = pd.read_csv(file_path_hour)

    # Konversi kolom tanggal ke format datetime
    data_hour['dteday'] = pd.to_datetime(data_hour['dteday'])
    data_day['dteday'] = pd.to_datetime(data_day['dteday'])
    return data_day, data_hour

data_day, data_hour = load_data()

# Analisis Data
if menu == "Analisis Data":
    st.title("📊 Analisis Data")
    
    # Pertanyaan 1
    st.subheader("1. Pengaruh Waktu terhadap Jumlah Penyewaan Sepeda")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', data=data_hour.groupby('hr').mean().reset_index(), ax=ax1)
    ax1.set_title("Pengaruh Jam terhadap Jumlah Penyewaan Sepeda", fontsize=16)
    ax1.set_xlabel("Jam", fontsize=12)
    ax1.set_ylabel("Rata-rata Penyewaan Sepeda", fontsize=12)
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig1)

    # Pertanyaan 2
    st.subheader("2. Perbandingan Pola Penyewaan Sepeda pada Hari Kerja dan Akhir Pekan")
    avg_rental_by_workingday = data_hour.groupby('workingday')['cnt'].mean()
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    colors = ['#FF6F61', '#6BAED6']
    ax2.bar(avg_rental_by_workingday.index, avg_rental_by_workingday.values, color=colors)
    ax2.set_xticks([0, 1])
    ax2.set_xticklabels(['Akhir Pekan', 'Hari Kerja'], fontsize=12)
    ax2.set_title("Perbandingan Penyewaan Sepeda (Hari Kerja vs Akhir Pekan)", fontsize=16)
    ax2.set_xlabel("Tipe Hari", fontsize=12)
    ax2.set_ylabel("Rata-rata Penyewaan Sepeda", fontsize=12)
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig2)

    # Kesimpulan
    st.subheader("Kesimpulan:")
    st.write("""
    **1. Pengaruh Waktu terhadap Jumlah Penyewaan Sepeda:** Aktivitas penyewaan meningkat tajam pada pagi dan sore hari.  
    **2. Hari Kerja vs Akhir Pekan:** Hari kerja didominasi pengguna terdaftar, akhir pekan oleh pengguna kasual.
    """)

# Biodata Pengguna
elif menu == "Biodata Pengguna":
    st.title("👤 Biodata Pengguna")
    st.markdown("### Informasi Pribadi")
    st.write("**Nama:** Richo Albert Tio")
    st.write("**Jurusan:** Teknik Informatika")
    st.write("**Asal:** Kapuas")
    st.write("**Hobi:** Bermain, belajar teknologi, dan eksplorasi hal baru")
    st.info("Semangat belajar dan terus berkembang! 🌟")
