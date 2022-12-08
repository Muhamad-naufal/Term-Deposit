import streamlit as st
import joblib
from PIL import Image

model=joblib.load("./model/model1")
def Predict(age,contact,duration,education,pdays,poutcome,previous):
    #Labels untuk Education
        if education == "illiterate" or education == "basic.4y" or education == "basic.6y" or education == "basic.9y":
            x = 0
        elif education == "high.school" or education == "unknown":
            x = 1
        elif education == "professional.course":
            x = 2
        else:
            x = 3
        # Labels untuk contacts
        if contact == "cellular":
            x1 = 0
        else:
            x1 = 1
        # Labels untuk poutcome
        if poutcome=="nonexistent":
            x2 = 0
        elif poutcome == "failure":
            x2 = 1
        else:
            x2 = 2
        pred = model.predict([[age,x1,duration,x,pdays,x2,previous]])
        return(pred[0])

def start1():
        img1 = Image.open("assets/deposit.png")
        img1 = img1.resize((500, 300))
        st.image(img1, use_column_width=False)
        html_temp = """
            <div style="background-color:blue;padding:5px">
            <h2 style="color:white;text-align:center;">Term Deposit Prediction</h2>
            </div>
            """
        st.markdown(html_temp, unsafe_allow_html=True)
        age = st.number_input("Umur")
        contact= st.radio("Kontak",("cellular","telephone"))
        duration = st.number_input("Masukkan durasi saat berkomunikasi dalam detik")
        education = st.radio("Pilih Pendidikan ",('basic.9y', 'university.degree', 'basic.4y', 'high.school',
        'professional.course', 'unknown', 'basic.6y', 'illiterate'))
        pdays = st.number_input("Jumlah hari yang berlalu setelah klien terakhir dihubungi dari kampanye sebelumnya")
        poutcome=st.radio("Hasil dari kampanye pemasaran sebelumnya",('failure','nonexistent','success'))
        previous=st.number_input("Jumlah kontak yang dilakukan sebelum kampanye ini dan untuk klien ini")
        if st.button("Prediksi"):
            result = Predict(age,contact,duration,education,pdays,poutcome,previous)
            if result == 1:
                st.success("Kemungkinana Besar, nasabah akan mengikuti deposito berjangka")
            else:
                st.success("Kemungkinana Besar, nasabah tidak akan mengikuti deposito berjangka")

start1()