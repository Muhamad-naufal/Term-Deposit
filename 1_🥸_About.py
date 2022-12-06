import streamlit as st
from PIL import Image
import os
from pycaret.regression import setup, compare_models, pull, save_model, load_model
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import pandas as pd
import joblib

st.set_page_config(
    page_title="About",
    page_icon="🙌",
)

st.title("Welcome To Our App")
st.write("""
Deposito berjangka adalah deposito yang memiliki jangka waktu tertentu, 
jangka waktu deposito berjangka adalah mulai satu hingga 24 bulan sesuai 
dengan kesepakatan dengan bank. Bank dalam mempromosikan dan menjangkau 
nasabah untuk menjual produk deposito berjangkanya perlu mengeluarkan 
pengeluaran yang besar dan terkesan tidak efektif karena tidak tepat 
sasaran. Kelompok kami memberikan solusi untuk membantu bank dalam 
mengidentifikasi nasabah atau calon nasabah mana yang memiliki kemungkinan 
terbesar akan berlangganan deposito berjangka, sehingga bank dapat lebih 
efektif dalam memasarkan produk deposito berjangka karena sudah terdapat 
target yang jelas.
""")
st.subheader("Manfaat dari project ini adalah:")
st.write("""
1. Membantu para pegawai bank pada bagian perbankan dalam menentukan nasabah mana
   yang harus diprioritaskan dalam pemasaran program deposito berjangka\n
2. Membantu para user mengetahui proses modeling yang dilakukan para programmer\n
3. Membantu para user dalam proses pembuatan projek AI\,
""")