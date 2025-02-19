import streamlit as st
import pandas as pd
import os

#Judul Halaman
st.title("Alat Hitung Susenas 2025 :computer:")

tab1, tab2 = st.tabs(["Konversi Satuan", "Alat Imputasi"])


import pandas as pd

#Load Database

rh_file_path = "arunika_app/rentang_harga.csv"
listrik_path = "arunika_app/imputasi_listrik.csv"
kb_path = "arunika_app/imputasi_kb.csv"
imunisasi_path = "arunika_app/imputasi_imunisasi.csv"
bpjs_path = "arunika_app/imputasi_bpjs.csv"
rh_database = pd.read_csv(rh_file_path, sep=";")
listrik_df = pd.read_csv(listrik_path, sep=";")
kb_df = pd.read_csv(kb_path, sep=";")
imunisasi_df = pd.read_csv(imunisasi_path, sep=";")
bpjs_df = pd.read_csv(bpjs_path, sep=";")

#list_kelompok_komoditas = rh_database["nama_kelompok_komoditas"].to_list()
#list_komoditas = rh_database["nama_komoditas"].to_list()

with tab1:

    st.subheader("Alat Konversi Satuan")
    st.caption("Silakan gunakan alat ini untuk mengonversi dari satuan lokal ke satuan standar. Perlu perhatian, untuk desimal menggunakan titik bukan koma, contoh: satu setengah dimasukkan menjadi 1.5 bukan 1,5! Sedangkan untuk ribuan menggunakan koma, sehingga hati-hati saat memasukkan nilai harga hasil konversi alat ini ke kuesioner.")

    col1, col2, col3 = st.columns(3)

    with col1:
        kelompok_komoditas = st.selectbox("Kelompok Komoditas", rh_database["nama_kelompok_komoditas"].unique())
    with col2:
        komoditas = st.selectbox("Nama Komoditas", rh_database[rh_database["nama_kelompok_komoditas"]== kelompok_komoditas]["nama_komoditas"].unique())
    with col3:
        satuan = st.selectbox("Satuan", rh_database[rh_database["nama_komoditas"]==komoditas]["satuan_lokal"].unique())


    baris_terpilih = rh_database.loc[(rh_database["nama_kelompok_komoditas"]==kelompok_komoditas)&
                                 (rh_database["nama_komoditas"]==komoditas)&
                                 (rh_database["satuan_lokal"]==satuan)]

    pengali_konv = baris_terpilih["konversi_satuan"].iloc[0]
    satuan_std = baris_terpilih["satuan_standar"].iloc[0]
    harga_bawah = baris_terpilih["harga_minimal"].iloc[0]
    harga_atas = baris_terpilih["harga_maksimal"].iloc[0]

    volume = st.number_input("Masukkan Banyaknya", min_value=0.00)

    hasil_konversi = round((volume * pengali_konv),2)
    st.metric("Hasil Konversi", value=f"{hasil_konversi:,.2f} {satuan_std}", border=True)

    harga_bawah_konv = harga_bawah * hasil_konversi
    harga_atas_konv = harga_atas * hasil_konversi
    st.caption(f"Rentang Harga dari Komoditas - {komoditas} - adalah dari Rp. {harga_bawah:,.0f} hingga Rp. {harga_atas:,.0f} per {satuan_std}.")
    st.markdown(f"##### -> Isikan harga di kuesioner pada rentang Rp. {harga_bawah_konv:,.0f} hingga Rp. {harga_atas_konv:,.0f} untuk komoditas - {komoditas} -.")

with tab2:
    with st.expander("Alat Imputasi Listrik"):

        daya_terpasang = st.selectbox("Daya Terpasang", listrik_df["daya_terpasang"].unique())

        listrik_terpilih = listrik_df[(listrik_df["daya_terpasang"]==daya_terpasang)]

        harga_diskon = listrik_terpilih["harga_per_kwh"].iloc[0]
        harga_normal = listrik_terpilih["harga_normal"].iloc[0]
        biaya_maks_diskon = listrik_terpilih["biaya_maks_diskon"].iloc[0]
        kwh_maks_diskon = listrik_terpilih["batas_maks_kwh"].iloc[0]

        biaya_listrik = st.number_input("Masukkan Biaya Listrik Sebulan", min_value=0)

        if biaya_listrik > biaya_maks_diskon :
            biaya_normal = biaya_listrik - biaya_maks_diskon
            kwh_normal = round((biaya_normal / harga_normal),2)
            listrik_kwh = kwh_normal + kwh_maks_diskon
        else:
            listrik_kwh = round((biaya_listrik / harga_diskon),2)
        
        st.metric("Pemakaian Listrik dalam kWh Sebulan Terakhir", value=f"{listrik_kwh:,.1f} kWh", border=True)
        
    
    with st.expander("Daftar Harga Keluarga Berencana (KB)"):

        jenis_kb = st.selectbox("Jenis KB", kb_df["jenis_kb"].unique())

        kb_terpilih = kb_df[(kb_df["jenis_kb"]==jenis_kb)]

        harga_kb = kb_terpilih["harga_kb"].iloc[0]

        st.metric("Pengeluaran untuk Keluarga Berencana", value=f"Rp. {harga_kb:,.0f}", border=True)

    with st.expander("Alat Imputasi Imunisasi"):

        st.caption("Pilih jenis imunisasi yang didapatkan bayi selama 1 (satu) tahun terakhir :")
        
        list_jenis_imunisasi = imunisasi_df["jenis_imunisasi"].to_list()
        null_df = [0] * 22

        biaya_1, biaya_2, biaya_3, biaya_4, biaya_5, biaya_6, biaya_7, biaya_8, biaya_9, biaya_10, biaya_11, biaya_12, biaya_13, biaya_14, biaya_15, biaya_16, biaya_17, biaya_18, biaya_19, biaya_20, biaya_21, biaya_22 = null_df

        col1, col2, col3 = st.columns(3)

        with col1:
            opt_1 = st.checkbox(list_jenis_imunisasi[0])
            opt_2 = st.checkbox(list_jenis_imunisasi[1])
            opt_3 = st.checkbox(list_jenis_imunisasi[2])
            opt_4 = st.checkbox(list_jenis_imunisasi[3])
            opt_5 = st.checkbox(list_jenis_imunisasi[4])
            opt_6 = st.checkbox(list_jenis_imunisasi[5])
            opt_7 = st.checkbox(list_jenis_imunisasi[6])
            opt_8 = st.checkbox(list_jenis_imunisasi[7])

        with col2:
            opt_9 = st.checkbox(list_jenis_imunisasi[8])
            opt_10 = st.checkbox(list_jenis_imunisasi[9])
            opt_11 = st.checkbox(list_jenis_imunisasi[10])
            opt_12 = st.checkbox(list_jenis_imunisasi[11])
            opt_13 = st.checkbox(list_jenis_imunisasi[12])
            opt_14 = st.checkbox(list_jenis_imunisasi[13])
            opt_15 = st.checkbox(list_jenis_imunisasi[14])
            opt_16 = st.checkbox(list_jenis_imunisasi[15])
            
        with col3:    
            opt_17 = st.checkbox(list_jenis_imunisasi[16])
            opt_18 = st.checkbox(list_jenis_imunisasi[17])
            opt_19 = st.checkbox(list_jenis_imunisasi[18])
            opt_20 = st.checkbox(list_jenis_imunisasi[19])
            opt_21 = st.checkbox(list_jenis_imunisasi[20])
            opt_22 = st.checkbox(list_jenis_imunisasi[21])
        

        if opt_1:
            terpilih_1 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[0])]
            biaya_1 = terpilih_1["harga_imunisasi"].iloc[0]
        if opt_2:
            terpilih_2 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[1])]
            biaya_2 = terpilih_2["harga_imunisasi"].iloc[0]
        if opt_3:
            terpilih_3 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[2])]
            biaya_3 = terpilih_3["harga_imunisasi"].iloc[0]
        if opt_4:
            terpilih_4 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[3])]
            biaya_4 = terpilih_4["harga_imunisasi"].iloc[0]
        if opt_5:
            terpilih_5 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[4])]
            biaya_5 = terpilih_5["harga_imunisasi"].iloc[0]
        if opt_6:
            terpilih_6 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[5])]
            biaya_6 = terpilih_6["harga_imunisasi"].iloc[0]
        if opt_7:
            terpilih_7 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[6])]
            biaya_7 = terpilih_7["harga_imunisasi"].iloc[0]
        if opt_8:
            terpilih_8 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[7])]
            biaya_8 = terpilih_8["harga_imunisasi"].iloc[0]
        if opt_9:
            terpilih_9 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[8])]
            biaya_9 = terpilih_9["harga_imunisasi"].iloc[0]
        if opt_10:
            terpilih_10 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[9])]
            biaya_10 = terpilih_10["harga_imunisasi"].iloc[0]
        if opt_11:
            terpilih_11 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[10])]
            biaya_11 = terpilih_11["harga_imunisasi"].iloc[0]
        if opt_12:
            terpilih_12 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[11])]
            biaya_12 = terpilih_12["harga_imunisasi"].iloc[0]
        if opt_13:
            terpilih_13 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[12])]
            biaya_13 = terpilih_13["harga_imunisasi"].iloc[0]
        if opt_14:
            terpilih_14 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[13])]
            biaya_14 = terpilih_14["harga_imunisasi"].iloc[0]
        if opt_15:
            terpilih_15 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[14])]
            biaya_15 = terpilih_15["harga_imunisasi"].iloc[0]
        if opt_16:
            terpilih_16 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[15])]
            biaya_16 = terpilih_16["harga_imunisasi"].iloc[0]
        if opt_17:
            terpilih_17 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[16])]
            biaya_17 = terpilih_17["harga_imunisasi"].iloc[0]
        if opt_18:
            terpilih_18 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[17])]
            biaya_18 = terpilih_18["harga_imunisasi"].iloc[0]
        if opt_19:
            terpilih_19 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[18])]
            biaya_19 = terpilih_19["harga_imunisasi"].iloc[0]
        if opt_20:
            terpilih_20 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[19])]
            biaya_20 = terpilih_20["harga_imunisasi"].iloc[0]
        if opt_21:
            terpilih_21 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[20])]
            biaya_21 = terpilih_21["harga_imunisasi"].iloc[0]
        if opt_22:
            terpilih_22 = imunisasi_df[(imunisasi_df["jenis_imunisasi"]==list_jenis_imunisasi[21])]
            biaya_22 = terpilih_22["harga_imunisasi"].iloc[0]
        
            
        total_biaya = biaya_1 + biaya_2 + biaya_3 + biaya_4 + biaya_5 + biaya_6 + biaya_7 + biaya_8 + biaya_9 + biaya_10 + biaya_11 + biaya_12 + biaya_13 + biaya_14 + biaya_15 + biaya_16 + biaya_17 + biaya_18 + biaya_19 + biaya_20 + biaya_21 + biaya_22
        
        st.metric("Pengeluaran Imunisasi Setahun Terakhir", value=f"Rp. {total_biaya:,}", border=True)

    with st.expander("Imputasi Premi Asuransi"):

        jenis_bpjs = st.selectbox("Jenis BPJS", bpjs_df["jenis_bpjs"].unique())

        if jenis_bpjs == "NON PBI PNS" :
            bpjs_terpilih = bpjs_df[(bpjs_df["jenis_bpjs"]==jenis_bpjs)]
            premi_bpjs_pns = bpjs_terpilih["premi_bpjs"].iloc[0]
            gaji_pokok = st.number_input("Gaji Pokok Sebulan", min_value=0)
            total_premi = premi_bpjs_pns * gaji_pokok
        else:
            bpjs_terpilih = bpjs_df[(bpjs_df["jenis_bpjs"]==jenis_bpjs)]
            premi_bpjs = bpjs_terpilih["premi_bpjs"].iloc[0]
            art_penerima_bpjs = st.number_input("Jumlah ART Penerima BPJS", min_value=0)
            total_premi = premi_bpjs * art_penerima_bpjs

        st.metric("Pengeluaran untuk Keluarga Berencana", value=f"Rp. {total_premi:,}", border=True)