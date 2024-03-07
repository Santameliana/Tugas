import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from babel.numbers import format_currency
sns.set_style('dark')
import numpy as np

# judul page
st.set_page_config(page_title="Air Quality from Guanyuan Analysis by Santa_meliana")


# dataset
data = pd.read_csv('all_data.csv')

# judul dashboard
st.title('Proyek analisis data Air Quality Guanyuan Station')

# deskripsi
st.write('Dashboard ini menyediakan cara interaktif untuk mengeksplorasi data kualitas udara dari tahun ke tahun dan apa perbaikannya. Juga mengatahui perubahan hujan dan kecepatan udara di Guanyuan berdasarkan hari dan tanggal berapakah polusi udara di Guanyuan paling sedikit.')

# tentang saya
st.markdown("""
### Tentang saya
- **Nama**: Santa Meliana
- **Email**: 6162001230@student.unpar.ac.id
- **ID Dicoding**: M232D4KX1529
""")


# Adding a sidebar for interactive inputs
st.sidebar.header('User Input Features')
st.sidebar.date_input
# Convert the 'date_time' column to datetime
data['date_time'] = pd.to_datetime(data['date_time'])
datetime_columns = ["date_time"]
data.sort_values(by="date_time", inplace=True)
data.reset_index(inplace=True)

min_date = data["date_time"].min()
max_date = data["date_time"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

# Display start and end date inputs in the sidebar
start_date = st.sidebar.date_input(
    label='Start Date',
    min_value=min_date,
    max_value=max_date,
    value=min_date
)

end_date = st.sidebar.date_input(
    label='End Date',
    min_value=min_date,
    max_value=max_date,
    value=max_date
)

#set header pada dashboard
st.header('Air Quality in Guanyuan :sparkles:')

#data yang telah difilter simpan dalam main_df
main_df = data[(data["date_time"] >= str(start_date)) & 
                (data["date_time"] <= str(end_date))]

# Filter data based on the selected year, month, and day

groupByYear = data.groupby("year").mean(numeric_only=True)
years = groupByYear.index.to_numpy()
st.title("Air Quality Analysis")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years, groupByYear["PM2.5"].values, label="PM2.5")
ax.plot(years, groupByYear["PM10"].values, label="PM10")
ax.plot(years, groupByYear["SO2"].values, label="SO2")
ax.plot(years, groupByYear["NO2"].values, label="NO2")
ax.plot(years, groupByYear["O3"].values, label="O3")
ax.set_title("Kualitas Udara di Guanyuan Berdasarkan Tahun")
ax.legend()
st.pyplot(fig)

st.write('Karena kualitas udara terlalu tinggi, akan dipisahkan grafiknya, sebagai berikut.')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years, groupByYear["CO"].values, label="CO")
ax.set_xlabel("Tahun")
ax.set_ylabel("Konsentrasi (mikrogram/m3)")
ax.set_title("Kualitas Udara di Guanyuan Berdasarkan Tahun")
ax.legend()
st.pyplot(fig)



# Visualisasi tren perubahan hujan dan kecepatan udara berdasarkan hari
# Assuming you have 'year', 'month', 'day' columns
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day']])

groupByDay = data.groupby("day").mean(numeric_only=True)
days = groupByDay.index.to_numpy()

st.subheader('perubahan hujan dan kecepatan udara di Guanyuan berdasarkan hari')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(days, groupByDay["RAIN"].values, label="Hujan")
ax.plot(days, groupByDay["WSPM"].values, label="Kecepatan Udara")
ax.set_title("Trend of Rain and Wind Speed By Day")
ax.set_xlabel("Day/Date")
ax.set_ylabel("Scale")
ax.legend()
st.pyplot(fig)