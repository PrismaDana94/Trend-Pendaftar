import streamlit as st
import pandas as pd

# Judul Dashboard
st.title("Dashboard Pendaftar Internship Program")

# Load data
df = pd.read_csv("data_pendaftar_clean.csv")

# Info awal
st.write("Jumlah Data:", df.shape[0])
st.write("Jumlah Kolom:", df.shape[1])

# Tampilkan data
st.subheader("Preview Data")
st.dataframe(df.head())
