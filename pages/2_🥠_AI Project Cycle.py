import streamlit as st

st.title("AI Project Cycle")
st.header("Pengertian AI Project Cycle")
st.image("assets/AI.png")
st.write("""
    Siklus Proyek AI atau AI Project Cycle adalah siklus/urutan pada pembuatan program AI 
    yang menentukan setiap langkah yang harus diambil seseorang untuk menentukan masalah yang akan diangkat,
    data apa saja yang akan dipakai dalam projek, bagaimana cara membersihkan atau meng-explore data,
    bagaimana cara membuat model yang tepat untuk projek, bagaimana hasil yang didapatkan, dan bagaimana
    orang lain dapat mengakses projek yang sudah dibuat.
""")

st.write("""
    Pada AI Project Cycle terdapat beberapa langkah yang harus dilakukan, yaitu :
    1. Problem Scoping
    2. Data Acquisiton
    3. Data Exploration
    4. Modeling
    5. Evaluation
    6. Deployment
""")

st.subheader("Problem Scoping")
st.write("""
    Problem Scoping adalah langkah dimana programmer atau si pembuat project harus menentukan masalah apa yang 
    harus diselesaikan. Pada kasus ini, kami mengambil studi kasus pada marketing perbankan pada deposito berjangka.
    Pada langkah ini juga, terdapat beberapa pertanyaan yang harus dijawab, yaitu :
    1. WHO  : Para pegawai perbankan di bidang marketing.
    2. WHAT : Sulitnya mencari nasabah yang kira - kira ingin mengikuti program deposito berjangka karena terlalu
              banyaknya data yang didapatkan.
    3. WHERE: Di lingkungan perbankan bidang marketing.
    4. WHY  : Solusi yang ditawarkan adalah dengan memprediksi siapa saja yang kira" akan mengikuti program deposito
              berjangka dengan menginputkan beberapa variable yang diperlukan dalam proses prediksi.
""")

st.subheader("Data Acquisition")
st.write("""
    Data Acquisition adalah proses pada pembuatan AI yang berkaitan dengan dataset. Project ini menggunakan dataset
    yang didapaykan dari website www.kaggle.com yang berarti dataset tersebut adalah data publik dan dapat digunakan
    siapa saja.
""")
st.image("assets/dataa.jpeg")
st.write("""
    Gambar diatas adalah tampilan dataset dalam website kaggle
    """)
st.image("assets/datae.jpeg")
st.write("""
    Gambar diatas adalah isi dari dataset pada proses coding
""")

st.subheader("Data Exploration")
st.write("""
    Data Exploration adalah proses pada pembuatan AI yang juga berkaitan dengan dataset. Bedanya, pada proses ini
    data diexplorasi dengan aritmatika sederhana untuk mempermudah mengetahui struktur dan meringkas data pengamatan
""")
st.image("assets/date.jpeg")
st.write("""
    Gambar diatas adalah code dala, mengubah variable string menjadi int agar mudah diamati dan mesin dapat membaca
    dengan tepat
""")

st.subheader("Modeling")
st.write("""
    Modeling adalah proses pada pembuatan AI yang juga berkaitan dengan dataset. Bedanya, pada proses ini
    data diexplorasi dengan aritmatika sederhana untuk mempermudah mengetahui struktur dan meringkas data pengamatan.
    Pada Project ini, juga menggunakan beberapa algoritma yaitu :
""")
st.image("assets/Random.jpeg")
st.write("""
    Algoritma Random Forest
""")
st.image("assets/decision.jpeg")
st.write("""
    Algoritma Decision Tree
""")
st.image("assets/logistik.jpeg")
st.write("""
    Algoritma Logistic Regression
""")
st.image("assets/neigbor.jpeg")
st.write("""
    Algoritma K-Nearest Neighbor
""")
st.image("assets/svm.jpeg")
st.write("""
    Algoritma Support Vector Machine
""")

st.subheader("Evaluasi")
st.write("""
    Hasil Akurasi dari masing - masing Algoritma adalah
""")
st.image("assets/eval.jpeg")
st.image("assets/eval2.jpeg")
st.write("""
    Dan akhirnya, pada project ini, kami menggunakan Algoritma Random Forest karena cocok dengan projek yang diibuat 
    dan memiliki akurasi saat training sebesar 82 persen dan saat testing adalah sebesar 77 persen.
""")

st.subheader("Deployment")
st.write("""
    Project ini akan di deploy atau dipublikasikan di sebuah website yang sudah dipersiapkan sebelumnya dengan tampilan 
    user interface seperti dibawah ini :
""")