import streamlit as st

hide_github_icon = """
<style>
#button.st-emotion-cache-15wzwg4
{
visibility: hidden;
}
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)


st.set_page_config(
    page_title="A.RU.NI.KA :sunrise:",
    layout= "wide",
    initial_sidebar_state= "collapsed"
)

#Beranda
st.title("A.RU.NI.KA :sunrise:")
st.caption("Aplikasi Reviu Susenas-Seruti dan Kalkulasinya (versi beta)")
st.write("---")

homepage_desc_1 = """
Pada September 2024, Lembar Pemeriksaan Susenas 2024 (LEPAS-2024) dikembangkan untuk menjaga rincian-rincian pertanyaan yang sering kali terlewatkan
saat pendataan lapangan. Dengan segala keterbatasannya LEPAS-2024 cukup memberikan dampak yang baik dalam mencegah data yang anomali. Sehingga pada
tahun 2025 ini, LEPAS-2024 dimodifikasi sedemikian rupa sehingga terciptalah aplikasi web yang lebih terbarukan yang diberi nama A.RU.NI.KA :sunrise:.
"""

homepage_desc_2 = """
A.RU.NI.KA :sunrise: dalam bahasa Sanskerta berarti 'seberkas cahaya matahari setelah terbit di pagi hari', harapan kami adalah aplikasi ini dapat berdayaguna dalam
menjaga kualitas pendataan Susenas-Seruti 2025 sehingga data yang dihasilkan dapat bermanfaat untuk khalayak ramai.
"""

homepage_desc_3 = """
A.RU.NI.KA :sunrise: singkatan dari Aplikasi Reviu
Susenas-Seruti dan Kalkulasinya. Aplikasi ini dikembangkan oleh Siratul Firdaus, S.Tr.Stat (Statistisi Ahli Pertama)
berkolaborasi dengan Intan Yusniasary, S.Tr.Stat (Instruktur Nasional Susenas dan Seruti 2025). Aplikasi ini menyuguhkan dua fitur utama,
yaitu Lembar Jaga dan Alat Hitung dimana Lembar Jaga disediakan untuk Pemeriksa sedangkan Alat Hitung disediakan untuk Pendata.
"""

homepage_desc_4 = """
Fitur Lembar Jaga memiliki menu-menu berupa Entri Lembar Jaga, Deteksi Anomali, Reviu Lembar Jaga, dan Dataframe Terkini. Sedangkan Fitur Alat Hitung
memiliki menu-menu berupa Alat Hitung, Konverter, dan Imputasi. Semua fitur-fitur yang ada pada A.RU.NI.KA :sunrise: ini akan terus dikembangkan demi kualitas Susenas-Seruti 2025 yang lebih baik.
"""

homepage_desc_5 = """
Salam hangat dari kami.
"""
st.write(homepage_desc_1)
st.write(homepage_desc_2)
st.write(homepage_desc_3)
st.write(homepage_desc_4)
st.write(homepage_desc_5)
