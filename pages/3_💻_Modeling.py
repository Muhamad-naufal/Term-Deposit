import streamlit as st
import os
import time
from pandas_profiling import ProfileReport
from pycaret.regression import setup, compare_models, pull, save_model, load_model
from streamlit_pandas_profiling import st_profile_report
import pandas as pd

def save_upload(uploadfile):
    with open(os.path.join("data_simpan", uploadfile.name),"wb") as f:
        f.write(uploadfile.getbuffer())
    return st.success("Berhasil Meload Dataset")

# Upload Dataset
st.title("Proses Modeling")
st.markdown("**Upload Dataset**")
file = st.file_uploader("Upload")
if file:
    df = pd.read_csv(file, index_col=None, encoding="utf-8", delimiter=',', quotechar='"')
    df.to_csv('sourcecode.csv', index=None)
    st.text("Isi Data")
    st.dataframe(df)
    save_upload(file)
    st.text("Proses Data Exploration")
    profile_df = ProfileReport(df)
    st_profile_report(profile_df)

    st.text("Membuat Model")
    pilih = st.selectbox('Silahkan Pilih Kolom', df.columns)
    if st.button('Modeling'): 
        setup(df, target=pilih, silent=True)
        setup_df = pull()
        best_model = compare_models()
        compare_df = pull()
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        st.dataframe(compare_df)
        save_model(best_model, './hasil_model/best_model')

        st.text("Download Model")
        with open('./hasil_model/best_model.pkl', 'rb') as f: 
            st.download_button('Download Model', f, file_name="best_model.pkl")