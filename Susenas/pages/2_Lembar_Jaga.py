import streamlit as st
import pandas as pd
import os

#Nama Halaman
st.header("**Lembar Jaga Susenas-Seruti :pencil:**")
st.caption("Halaman ini digunakan untuk melakukan entri Lembar Jaga, melakukan **deteksi anomali** dan melakukan *review* terhadap hasil entri tersebut, serta menampilkan ringkasan deskriptif terkait data terkini :sunglasses:")

#List Alokasi Petugas dan Variabel Jaga
list_pml = pd.read_excel("database_ssn.xlsx",  sheet_name="PML")
list_ppl = pd.read_excel("database_ssn.xlsx",  sheet_name="PPL")
list_nks = pd.read_excel("database_ssn.xlsx",  sheet_name="NKS")
list_nus = range(1,11,1)
df_var = pd.read_excel("database_ssn.xlsx",  sheet_name="VAR")
list_var = df_var["Variabel"].to_list()

#File Respons Data Masukan
csv_file_path = "data_input_response.csv"
data = pd.DataFrame(columns= list_var)
if os.path.exists(csv_file_path):
    data = pd.read_csv(csv_file_path)

#Dictionary Variabel Jaga
form_values = {}
for var in list_var:
    form_values[var] = None

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Entri Lembar Jaga", "Deteksi Anomali", "Review Lembar Jaga", "Dataframe Terkini", "Progres Pemeriksaan"])

with tab1:
    #Form Pengisian Lembar Jaga
    with st.form("user_input_form", enter_to_submit= False, clear_on_submit= True):
        st.write("Masukkan Isian sesuai Lembar Jaga:")
        st.write("")
        
        #Identitas Petugas dan Wilayah Tugas
        st.write("Identitas Petugas dan Wilayah Tugas:")    
        form_values["Nama PML"] = st.selectbox("Nama PML", list_pml, index=None, placeholder= "Pilih salah satu")        
        form_values["Nama PPL"] = st.selectbox("Nama PPL", list_ppl, index=None, placeholder= "Pilih salah satu")
        form_values["NKS"] = st.selectbox("NKS", list_nks, index=None, placeholder= "Pilih salah satu")
        form_values["Nomor Urut Sampel"] = st.selectbox("Nomor Urut Sampel", list_nus, index=None, placeholder= "Pilih salah satu")

        #Blok III
        st.write("------------------------------------------------------------------------------------")
        st.write("Banyaknya ART dan Jumlah Komoditas yang Terisi")
        form_values["Jumlah ART"] = st.number_input("Jumlah ART (R.301)", min_value= 0)
        form_values["Jumlah Komoditas Makanan"] = st.number_input("Jumlah Komoditas Bahan Makanan, Bahan Minuman, dan Rokok yang Terisi (R.304)", min_value= 0)
        form_values["Jumlah Komoditas Non Makanan"] = st.number_input("Jumlah Komoditas Barang-barang Bukan Makanan yang Terisi (R.305)", min_value= 0)

        #Blok IV.1
        st.write("------------------------------------------------------------------------------------")
        st.write("Kewajaran Konsumsi Beras, Gula, dan Garam")
        form_values["Jumlah Beras dalam Kg"] = st.number_input("Jumlah Beras dalam Kg (R.IV.1.1)", min_value= 0)
        form_values["Jumlah Konsumsi Gula dalam Ons"] = st.number_input("Jumlah Konsumsi Gula Pasir dalam Ons (R.IV.1.160)", min_value= 0)
        form_values["Jumlah Konsumsi Garam dalam Gram"] = st.number_input("Jumlah Konsumsi Garam dalam Gram (R.IV.1.168)", min_value= 0)

        #Biaya yang seharusnya dikeluarkan jika mempunyai ART berusia dibawah 1 Tahun
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai ART berusia dibawah 1 Tahun")
        form_values["Jumlah ART dibawah 10 Tahun"   ] = st.number_input("Jumlah ART dibawah 10 Tahun", min_value= 0)
        form_values["Jumlah ART dibawah 1 Tahun"] = st.number_input("Jumlah ART dibawah 1 tahun", min_value= 0)
        form_values["Biaya Melahirkan"] = st.number_input("Biaya Melahirkan (Blok IV.2 R248-254) salah satu terisi", min_value=0)
        form_values["Biaya Periksa Kehamilan"] = st.number_input("Biaya Periksa Kehamilan (Blok IV.2 R259)", min_value=0)
        form_values["Biaya Imunisasi"] = st.number_input("Biaya Imunisasi", min_value= 0)
        form_values["Biaya Pakaian Bayi"] = st.number_input("Biaya Pakaian Bayi", min_value= 0)
        form_values["Biaya Minyak Telon"] = st.number_input("Biaya Minyak Telon", min_value= 0)

        #Biaya yang seharusnya dikeluarkan jika mempunyai ART yang masih bersekolah/baru masuk sekolah
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai ART yang masih bersekolah/baru masuk sekolah")
        form_values["Jumlah ART yang masih sekolah"] = st.number_input("Jumlah ART yang masih sekolah", min_value= 0)
        form_values["Jumlah ART yang baru bersekolah"] = st.number_input("Jumlah ART yang baru bersekolah/masuk pada tahun ajaran baru", min_value= 0)
        form_values["Sumbangan Pembangunan Sekolah"] = st.number_input("Sumbangan Pembangunan Sekolah", min_value= 0)
        form_values["Uang Sekolah dan Iuran Komite"] = st.number_input("Uang Sekolah dan Iuran Komite", min_value= 0)
        form_values["Iuran Sekolah Lainnya"] = st.number_input("Iuran Sekolah Lainnya", min_value= 0)
        form_values["Biaya Buku Pelajaran"] = st.number_input("Biaya Buku Pelajaran", min_value= 0)
        form_values["Alat-alat Tulis"] = st.number_input("Alat-alat Tulis", min_value= 0)
        form_values["Uang Kursus di Luar Sekolah"] = st.number_input("Uang Kursus di Luar Sekolah", min_value= 0)
        
        #Biaya yang seharusnya dikeluarkan jika mempunyai ART berusia diatas 60 Tahun
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai ART berusia diatas 60 Tahun")
        form_values["Jumlah ART diatas 60 Tahun"] = st.number_input("Jumlah ART diatas 60 Tahun", min_value= 0)
        form_values["Biaya Pemeliharaan Kesehatan Lainnya"] = st.number_input("Biaya Pemeliharaan Kesehatan Lainnya", min_value= 0)
        
        #Biaya yang seharusnya dikeluarkan jika mempunyai ART Wanita Kawin Usia 15 - 54 Tahun
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai ART Wanita Kawin Usia 15 - 54 Tahun")
        form_values["Jumlah ART Wanita Kawin Usia 15-54 Tahun"] = st.number_input("Jumlah ART Wanita Kawin Usia 15-54 Tahun", min_value= 0)
        form_values["Pengeluaran Keluarga Berencana"] = st.number_input("Pengeluaran Keluarga Berencana", min_value= 0)
        
        #Biaya yang seharusnya dikeluarkan jika mempunyai kendaraan bermotor
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai kendaraan bermotor")
        form_values["Kepemilikan Kendaraan Bermotor"] = st.number_input("Kepemilikan Kendaraan Bermotor", min_value= 0)
        form_values["Pengeluaran Bensin atau Solar dalam Liter"] = st.number_input("Pengeluaran Bensin atau Solar dalam Liter", min_value= 0)
        form_values["Pengeluaran Bensin atau Solar dalam Rupiah"] = st.number_input("Pengeluaran Bensin atau Solar dalam Rupiah", min_value= 0)
        form_values["Pengeluaran Minyak Pelumas dalam Liter"] = st.number_input("Pengeluaran Minyak Pelumas dalam Liter", min_value= 0)
        form_values["Pengeluaran Minyak Pelumas dalam Rupiah"] = st.number_input("Pengeluaran Minyak Pelumas dalam Rupiah", min_value= 0)
        form_values["Pengeluaran Perbaikan dan Pemeliharaan Kendaraan Bermotor"] = st.number_input("Pengeluaran Perbaikan dan Pemeliharaan Kendaraan Bermotor", min_value= 0)
        form_values["Pengeluaran Biaya Transportasi Lainnya"] = st.number_input("Pengeluaran Biaya Transportasi Lainnya", min_value= 0)
        form_values["Pengeluaran Pajak Kendaraan Bermotor"] = st.number_input("Pengeluaran Pajak Kendaraan Bermotor", min_value= 0)
        
        #Biaya yang seharusnya dikeluarkan jika tidak mempunyai kendaraan bermotor
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika tidak mempunyai kendaraan bermotor")
        form_values["Pengeluaran Transportasi Darat"] = st.number_input("Pengeluaran Transportasi Darat", min_value= 0)
        
        #Penerimaan Bantuan Pemerintah
        st.write("------------------------------------------------------------------------------------")
        st.write("Penerimaan Bantuan Pemerintah")
        form_values["Penerimaan Bantuan Pemerintah"] = st.selectbox("Penerimaan Bantuan Pemerintah", ["Ya", "Tidak"], index= None, placeholder= "Pilih salah satu")
        form_values["Bantuan Pemerintah dalam bentuk uang"] = st.number_input("Bantuan Pemerintah dalam bentuk uang", min_value= 0)
        form_values["Bantuan Pemerintah dalam bentuk barang"] = st.number_input("Bantuan Pemerintah dalam bentuk barang", min_value= 0)
        
        #Biaya yang WAJIB dikeluarkan oleh rumah tangga
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang WAJIB dikeluarkan oleh rumah tangga")
        form_values["Pemeliharaan Rumah dan Perbaikan Ringan"] = st.number_input("Pemeliharaan Rumah dan Perbaikan Ringan", min_value= 0)
        form_values["Pengeluaran untuk Listrik dalam kWh"] = st.number_input("Pengeluaran untuk Listrik dalam kWh", min_value= 0)
        form_values["Pengeluaran LPG dalam Kg"] = st.number_input("Pengeluaran LPG dalam Kg", min_value= 0)
        form_values["Pengeluaran LPG dalam Rupiah"] = st.number_input("Pengeluaran LPG dalam Rupiah", min_value= 0)
        form_values["Pengeluaran Kebutuhan Lainnya untuk Rumah"] = st.number_input("Pengeluaran Kebutuhan Lainnya untuk Rumah", min_value= 0)
        form_values["Sabun Mandi, Pasta Gigi, Sikat Gigi, dan Sampo"] = st.number_input("Sabun Mandi, Pasta Gigi, Sikat Gigi, dan Sampo", min_value= 0)
        form_values["Barang Kecantikan dan Pembalut Wanita"] = st.number_input("Barang Kecantikan dan Pembalut Wanita", min_value= 0)
        form_values["Perawatan Kulit, Muka, Kuku, Rambut"] = st.number_input("Perawatan Kulit, Muka, Kuku, Rambut", min_value= 0)
        form_values["Sabun Cuci"] = st.number_input("Sabun Cuci", min_value= 0)
        form_values["Bahan Pemeliharaan Pakaian"] = st.number_input("Bahan Pemeliharaan Pakaian", min_value= 0)
        form_values["Barang Lainnya"] = st.number_input("Barang Lainnya", min_value= 0)
        form_values["Pulsa HP"] = st.number_input("Pulsa HP", min_value= 0)
        form_values["Biaya Internet atau Warnet"] = st.number_input("Biaya Internet atau Warnet", min_value= 0)
        form_values["Jasa Lembaga Keuangan"] = st.number_input("Jasa Lembaga Keuangan", min_value= 0)
        form_values["Jasa Lainnya"] = st.number_input("Jasa Lainnya", min_value= 0)
        form_values["Pengeluaran Pajak PBB"] = st.number_input("Pengeluaran Pajak PBB", min_value= 0)
        form_values["Pengeluaran untuk Asuransi Kesehatan"] = st.number_input("Pengeluaran untuk Asuransi Kesehatan", min_value= 0)

        #Kondisi saat Tombol Submit ditekan
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            id_values = {}
            for i in form_values:
                if i != "Nomor Urut Sampel":
                    id_values[i] = form_values[i]
                else:
                    break

            if not all(id_values.values()):
                st.warning("Pastikan semua isian identitas petugas telah terisi!")
            else:
                data = pd.concat([data, pd.DataFrame([form_values])], ignore_index=True)
                data = data.drop_duplicates(subset= ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel"], keep= "last")
                data["NKS"] = data["NKS"].apply(str)
                data.to_csv(csv_file_path, index=False)
                st.success("Jawabanmu berhasil dikirim, kamu bisa lakukan review pada menu Review Lembar Jaga ya!")

with tab2:
    #Import dataframe hasil masukan
    response_data = pd.read_csv("data_input_response.csv")

    #Import List Kode Anomali
    kode_anomali = pd.read_excel("database_ssn.xlsx", sheet_name="Anomali")
    kode_anomali = kode_anomali["Kode Anomali"].to_list()

    #Anomali dan Rumah Tangga yang terkait
    st.subheader("Daftar Anomali dan Hasil Pemeriksaan secara Umum")
    st.write("---")

    #Jumlah Komoditas Makanan kurang dari 13
    st.write(kode_anomali[0])
    st.write(response_data.loc[response_data["Jumlah Komoditas Makanan"] < 13, ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah Komoditas Makanan"]])

    #Jumlah Komoditas Non Makanan kurang dari 19
    st.write(kode_anomali[1])
    st.write(response_data.loc[response_data["Jumlah Komoditas Non Makanan"] < 19, ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah Komoditas Non Makanan"]])

    #Jumlah Konsumsi Beras Kg/Kapita kurang dari 1.8 atau lebih dari sama dengan 2.8
    st.write(kode_anomali[2])
    st.write(response_data.loc[(response_data["Jumlah Beras dalam Kg"]/response_data["Jumlah ART"] < 1.8) | (response_data["Jumlah Beras dalam Kg"]/response_data["Jumlah ART"] >= 2.8), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART", "Jumlah Beras dalam Kg"] ])

    #Jumlah Konsumsi Gula Ons/Kapita > 2.5
    st.write(kode_anomali[3])
    st.write(response_data.loc[(response_data["Jumlah Konsumsi Gula dalam Ons"]/response_data["Jumlah ART"] > 2.5), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART", "Jumlah Konsumsi Gula dalam Ons"] ])

    #Jumlah Konsumsi Garam Gram/Kapita > 28
    st.write(kode_anomali[4])
    st.write(response_data.loc[(response_data["Jumlah Konsumsi Garam dalam Gram"]/response_data["Jumlah ART"] > 28), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART", "Jumlah Konsumsi Garam dalam Gram"] ])

with tab3:
    #Import dataframe hasil masukan
    hasil_input = pd.read_csv("data_input_response.csv")

    #Dictionary filtering variable
    filter_var = {}

    #Filtering dataframe yang ingin direview
    with st.form("user_input_review", enter_to_submit= False):
        filter_var["Nama PML"] = st.selectbox("Nama PML", list_pml, index=None, placeholder= "Pilih salah satu")        
        filter_var["Nama PPL"] = st.selectbox("Nama PPL", list_ppl, index=None, placeholder= "Pilih salah satu")
        filter_var["NKS"] = st.selectbox("NKS", list_nks, index=None, placeholder= "Pilih salah satu")
        filter_var["Nomor Urut Sampel"] = st.selectbox("Nomor Urut Sampel", list_nus, index=None, placeholder= "Pilih salah satu")

        #Kondisi Review button ditekan
        review_button = st.form_submit_button("Review")

    if review_button:
        review_temp = hasil_input.loc[(hasil_input["Nama PML"]==filter_var["Nama PML"]) &
                                    (hasil_input["Nama PPL"]==filter_var["Nama PPL"]) &
                                    (hasil_input["NKS"]==filter_var["NKS"]) &
                                    (hasil_input["Nomor Urut Sampel"]==filter_var["Nomor Urut Sampel"])
                                    ]
        st.write("Data yang tersimpan :")
        st.write(review_temp)
        with st.container(height= 500, border= True):
            st.write("## Pastikan isian dokumen sudah diperbaiki dan dientri ulang pada menu Entri Lembar Jaga setelah diperbaiki!")
            st.write("------------------")
            st.write("Hasil pemeriksaan untuk rumah tangga ini adalah sebagai berikut:")

            #Rule Validasi Pemeriksaan
            if review_temp["Jumlah Komoditas Makanan"].values < 13 :
                st.markdown(f"- {kode_anomali[0]}. Konfirmasi ulang ke petugas!")
            
            if review_temp["Jumlah Komoditas Non Makanan"].values < 19 :
                st.markdown(f"- {kode_anomali[1]}. Konfirmasi ulang ke petugas!")
            
            if review_temp["Jumlah Beras dalam Kg"].values/review_temp["Jumlah ART"].values < 10 :
                st.markdown(f"- {kode_anomali[2]}. Konfirmasi ulang ke petugas!")
            
            if review_temp["Jumlah Konsumsi Gula dalam Ons"].values/review_temp["Jumlah ART"].values < 2.8 :
                st.markdown(f"- {kode_anomali[3]}. Konfirmasi ulang ke petugas!")
            
            if review_temp["Jumlah Konsumsi Garam dalam Gram"].values/review_temp["Jumlah ART"].values < 28 :
                st.markdown(f"- {kode_anomali[4]}. Konfirmasi ulang ke petugas!")



with tab4:
    #Metriks Dataframe
    data_input = pd.read_csv("data_input_response.csv")
    st.subheader("Ringkasan Deskriptif :bar_chart:")

    #Kolom Metrik

    col1, col2, col3 = st.columns(3)
    col1a, col2a = st.columns(2)

    #Metrik
    with col1:
        st.metric(label="Total Sampel yang Diperiksa", value=f"{len(data_input)} Ruta")

    with col2:
        st.metric(label="Rata-rata Jumlah ART", value=f"{data_input["Jumlah ART"].mean():,.0f} Orang")

    with col3:
        st.metric(label="Rata-rata Konsumsi Beras", value=f"{data_input["Jumlah Beras dalam Kg"].mean():,.2f} Kg")

    with col1a:
        st.metric(label="Rata-rata Konsumsi Komoditas Makanan", value=f"{data_input["Jumlah Komoditas Makanan"].mean():,.0f} Jenis")

    with col2a:
        st.metric(label="Rata-rata Konsumsi Komoditas Non Makanan", value=f"{data_input["Jumlah Komoditas Non Makanan"].mean():,.0f} Jenis")

    st.write("---")
    st.subheader("Data Terkini:")
    st.dataframe(data_input)

with tab5:
    st.title("Progres Pemeriksaan Dokumen :bar_chart:")
    st.write("---")
    
    progres_pml = data_input.groupby(by = ["Nama PML", "NKS"]).NKS.value_counts()
    st.write("Jumlah Sampel yang Sudah Diperiksa :", progres_pml)

    st.write("---")
    sum_nks_df = data_input.groupby(by="Nama PML").NKS.count().sort_values(ascending=False).reset_index()
    st.bar_chart(data=sum_nks_df.sort_values(by="NKS", ascending=True), x="Nama PML", y="NKS", x_label= "Pemeriksa", y_label= "Jumlah Sampel")