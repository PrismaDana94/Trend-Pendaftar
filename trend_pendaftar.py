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

df["Tanggal Gabungan"] = pd.to_datetime(df["Tanggal Gabungan"])

# ======================
# FILTER PERIODE
# ======================
st.sidebar.header("🔎 Filter Periode")

periode = st.sidebar.radio(
    "Pilih Periode Pendaftaran",
    ["Semua", "Sebelum Juli 2024", "Sesudah Juli 2024"]
)

if periode == "Sebelum Juli 2024":
    df = df[df["Tanggal Gabungan"] < "2024-07-01"]
elif periode == "Sesudah Juli 2024":
    df = df[df["Tanggal Gabungan"] >= "2024-07-01"]


# ======================
# JUDUL
# ======================
st.title("📊 Dashboard Pendaftar Internship Program")

st.write("Total Data:", df.shape[0])

# ======================
# TREN PENDAFTAR BULANAN
# ======================
st.header("📈 Tren Pendaftar Bulanan")

# urutan bulan
urutan_bulan = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

df["Month_name"] = pd.Categorical(
    df["Month_name"],
    categories=urutan_bulan,
    ordered=True
)

# hitung jumlah pendaftar per bulan
trend = (
    df.groupby(["Year", "Month_name"])
    .size()
    .reset_index(name="Jumlah Pendaftar")
)

trend = trend.sort_values(["Year", "Month_name"])

# label Jan 2024
trend["Bulan"] = trend["Month_name"].astype(str) + " " + trend["Year"].astype(str)

# ======================
# GRAFIK
# ======================
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(trend["Bulan"], trend["Jumlah Pendaftar"], marker="o")

# angka di titik
for x, y in zip(trend["Bulan"], trend["Jumlah Pendaftar"]):
    ax.text(x, y, str(y), ha="center", va="bottom", fontsize=8)

ax.set_title("Tren Pendaftar Bulanan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Pendaftar")

plt.xticks(rotation=45)
st.pyplot(fig)

# ======================
# CHANNEL PENDAFTARAN
# ======================
st.header("📣 Channel Pendaftaran")

channel = df["Channel"].value_counts().reset_index()
channel.columns = ["Channel", "Jumlah Pendaftar"]

fig, ax = plt.subplots(figsize=(8,4))
bars = ax.bar(channel["Channel"], channel["Jumlah Pendaftar"])

# angka di atas bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha="center",
        va="bottom",
        fontsize=9
    )

ax.set_title("Distribusi Channel Pendaftaran")
ax.set_xlabel("Channel")
ax.set_ylabel("Jumlah Pendaftar")

plt.xticks(rotation=45)
st.pyplot(fig)

# ======================
# PROFIL PENDAFTAR - USIA
# ======================
st.header("👤 Profil Pendaftar - Usia")

usia = df["Umur"].value_counts().sort_index().reset_index()
usia.columns = ["Umur", "Jumlah Pendaftar"]

fig, ax = plt.subplots(figsize=(10,4))
bars = ax.bar(usia["Umur"], usia["Jumlah Pendaftar"])

# angka di atas bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha="center",
        va="bottom",
        fontsize=8
    )

ax.set_title("Distribusi Usia Pendaftar")
ax.set_xlabel("Usia")
ax.set_ylabel("Jumlah Pendaftar")

st.pyplot(fig)

# insight usia terbanyak
usia_terbanyak = df["Umur"].mode()[0]

st.caption(f"🔎 Usia terbanyak pendaftar adalah **{usia_terbanyak} tahun**.")

# ======================
# PROFIL PENDAFTAR - DOMISILI
# ======================
st.header("🏠 Domisili Pendaftar")

domisili = df["Region"].value_counts().reset_index()
domisili.columns = ["Region", "Jumlah Pendaftar"]

fig, ax = plt.subplots(figsize=(6,4))
bars = ax.bar(domisili["Region"], domisili["Jumlah Pendaftar"])

# angka di atas bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha="center",
        va="bottom",
        fontsize=9
    )

ax.set_title("Distribusi Domisili Pendaftar")
ax.set_xlabel("Region")
ax.set_ylabel("Jumlah Pendaftar")

st.pyplot(fig)

# ======================
# TOP 10 KOTA PENDAFTAR
# ======================
st.header("🏙️ Top 10 Kota Pendaftar")

top_kota = (
    df["Kota"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_kota.columns = ["Kota", "Jumlah Pendaftar"]

fig, ax = plt.subplots(figsize=(8,4))
bars = ax.bar(top_kota["Kota"], top_kota["Jumlah Pendaftar"])

# angka di atas bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha="center",
        va="bottom",
        fontsize=9
    )

ax.set_title("Top 10 Kota dengan Pendaftar Terbanyak")
ax.set_xlabel("Kota")
ax.set_ylabel("Jumlah Pendaftar")

plt.xticks(rotation=45)
st.pyplot(fig)

# ======================
# TOP 10 MINAT PROGRAM
# ======================
st.header("🎓 Top 10 Minat Program")

top_program = (
    df["Product"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_program.columns = ["Program", "Jumlah Pendaftar"]

fig, ax = plt.subplots(figsize=(10,4))
bars = ax.bar(top_program["Program"], top_program["Jumlah Pendaftar"])

# angka di atas bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha="center",
        va="bottom",
        fontsize=9
    )

ax.set_title("Top 10 Minat Program")
ax.set_xlabel("Program")
ax.set_ylabel("Jumlah Pendaftar")

plt.xticks(rotation=45)
st.pyplot(fig)

# ======================
# INSIGHT UTAMA
# ======================
st.header("💡 Insight Utama")

st.info("""
📈 **Tren Pendaftaran Meningkat**  
Jumlah pendaftar meningkat signifikan sejak pertengahan 2024 dan stabil pada periode berikutnya.

📣 **Channel Paling Efektif**  
Meta Ads dan Referral menjadi sumber pendaftar terbesar.

👤 **Profil Pendaftar Dominan**  
Mayoritas pendaftar berusia 22–27 tahun (early career & career switcher).

🏠 **Ekspansi Wilayah**  
Pendaftar Non-Jabodetabek tumbuh lebih tinggi dibanding Jabodetabek.

🎓 **Minat Program**  
Program Data Science dan bidang digital masih menjadi minat utama peserta.
""")

# ======================
# REKOMENDASI
# ======================
st.header("🎯 Rekomendasi")

st.success("""
🎯 **Optimalkan Channel Utama**  
Fokuskan anggaran pada Meta Ads dan Referral yang terbukti paling efektif.

🤝 **Perkuat Referral Alumni**  
Dorong akuisisi organik melalui program referral yang lebih terstruktur.

📘 **Strategi Program Unggulan**  
Pertahankan Data Science sebagai program utama dan kembangkan jalur lanjutan.

🎯 **Segmentasi Target Marketing**  
Fokuskan komunikasi pada usia 22–27 tahun dengan pesan upskilling & career switching.

🌍 **Perluas Jangkauan Wilayah**  
Tingkatkan kampanye digital berbasis lokasi untuk kota Non-Jabodetabek potensial.
""")


