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

st.header("📈 Tren Pendaftar Bulanan")

trend = (
    df.groupby("period")
    .size()
    .reset_index(name="Jumlah Pendaftar")
)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(trend["period"], trend["Jumlah Pendaftar"], marker="o")

# angka di tiap titik
for x, y in zip(trend["period"], trend["Jumlah Pendaftar"]):
    ax.text(x, y, str(y), ha="center", va="bottom", fontsize=8)

ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Pendaftar")
ax.set_title("Tren Pendaftar Bulanan")

plt.xticks(rotation=45)
st.pyplot(fig)
