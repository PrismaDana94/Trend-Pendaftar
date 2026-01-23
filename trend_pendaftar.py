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

