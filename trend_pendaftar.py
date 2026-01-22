import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======================
# SETTING HALAMAN
# ======================
st.set_page_config(
    page_title="Dashboard Pendaftar Internship",
    layout="wide"
)

# ======================
# LOAD DATA
# ======================
df = pd.read_csv("data_pendaftar_clean.csv")

# ======================
# JUDUL
# ======================
st.title("Dashboard Pendaftar Internship Program")
st.markdown("Analisis tren pendaftaran, profil peserta, dan minat program")

st.divider()

# ======================
# 📊 OVERVIEW
# ======================
st.header("📊 Overview")

total_pendaftar = df.shape[0]
periode_awal = df["Tanggal Gabungan"].min()
periode_akhir = df["Tanggal Gabungan"].max()

col1, col2 = st.columns(2)
col1.metric("Total Pendaftar", total_pendaftar)
col2.metric("Periode Data", f"{periode_awal} sampai {periode_akhir}")

st.divider()

# ======================
# 📈 TREN PENDAFTAR
# ======================
st.header("📈 Tren Pendaftar Bulanan")

trend = (
    df.groupby("Month")
    .size()
    .reset_index(name="Jumlah Pendaftar")
)

fig, ax = plt.subplots()
ax.plot(trend["Month"], trend["Jumlah Pendaftar"], marker="o")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Pendaftar")
ax.set_title("Tren Pendaftar Bulanan")

st.pyplot(fig)

st.divider()

# ======================
# 📣 CHANNEL PENDAFTARAN
# ======================
st.header("📣 Channel Pendaftaran")

channel = df["Channel Pendaftaran"].value_counts()

fig2, ax2 = plt.subplots()
channel.plot(kind="bar", ax=ax2)
ax2.set_title("Jumlah Pendaftar per Channel")
ax2.set_xlabel("Channel")
ax2.set_ylabel("Jumlah Pendaftar")

st.pyplot(fig2)

st.divider()

# ======================
# 👤 PROFIL PENDAFTAR
# ======================
st.header("👤 Profil Pendaftar")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribusi Usia")
    usia = df["Umur"].value_counts().sort_index()
    st.bar_chart(usia)

with col2:
    st.subheader("Domisili Teratas")
    domisili = df["Kota"].value_counts().head(10)
    st.bar_chart(domisili)

st.divider()

# ======================
# 🎓 MINAT PROGRAM
# ======================
st.header("🎓 Minat Program")

program = df["Product"].value_counts().head(10)
st.bar_chart(program)

st.divider()

# ======================
# 💡 INSIGHT UTAMA
# ======================
st.header("💡 Insight Utama")

st.markdown("""
- Jumlah pendaftar meningkat signifikan setelah pertengahan 2024  
- Mayoritas peserta berada pada rentang usia 22–27 tahun  
- Data Science menjadi program dengan minat tertinggi  
- Meta Ads dan Referral merupakan channel pendaftaran utama  
- Pendaftar mulai meluas ke wilayah Non-Jabodetabek  
""")
