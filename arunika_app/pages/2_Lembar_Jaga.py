import streamlit as st
import pandas as pd
import os

#Nama Halaman
st.header("**Lembar Jaga Susenas-Seruti :pencil:**")
st.caption("Halaman ini digunakan untuk melakukan entri Lembar Jaga, melakukan **deteksi anomali** dan melakukan *review* terhadap hasil entri tersebut, serta menampilkan ringkasan deskriptif terkait data terkini :sunglasses:")

#List Alokasi Petugas dan Variabel Jaga
list_pml = pd.read_csv("arunika_app/List_PML.csv", sep="\t")
list_ppl = pd.read_csv("arunika_app/List_PPL.csv", sep="\t")
list_nks = pd.read_csv("arunika_app/List_NKS.csv", sep="\t")
list_nus = range(1,11,1)
df_var = pd.read_csv("arunika_app/List_VAR.csv", sep="\t")
list_var = df_var["Variabel"].to_list()
df_var_wajib = pd.read_csv("arunika_app/List_Wajib.csv", sep="\t")
list_var_wajib = df_var_wajib["Variabel"].to_list()

#File Respons Data Masukan
csv_file_path = "arunika_app/data_input_response.csv"
data = pd.DataFrame(columns= list_var)
if os.path.exists(csv_file_path):
    data = pd.read_csv(csv_file_path)

#Dictionary Variabel Jaga
form_values = {}
for var in list_var:
    form_values[var] = None

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Entri Lembar Jaga", "Perbaikan Data", "Review Lembar Jaga", "Deteksi Anomali", "Dataframe Terkini", "Progres Pemeriksaan"])

with tab1:
    #Form Pengisian Lembar Jaga
    with st.form("user_input_form", enter_to_submit= False, clear_on_submit= True):
        st.write("Masukkan Isian sesuai Lembar Jaga:")
        st.caption("Untuk desimal menggunakan titik bukan koma")
        st.write("")

        form_values["Sudah Selesai"] = st.selectbox("Apakah Ruta ini Sudah Selesai?", options=["Sudah", "Belum"], index=None, placeholder="Pilih salah satu")
        
        #Identitas Petugas dan Wilayah Tugas
        st.write("------------------------------------------------------------------------------------")
        st.write("Identitas Petugas dan Wilayah Tugas:")    
        form_values["Nama PML"] = st.selectbox("Nama PML", list_pml, index=None, placeholder= "Pilih salah satu")        
        form_values["Nama PPL"] = st.selectbox("Nama PPL", list_ppl, index=None, placeholder= "Pilih salah satu")
        form_values["NKS"] = st.selectbox("NKS", list_nks, index=None, placeholder= "Pilih salah satu")
        form_values["Nomor Urut Sampel"] = st.selectbox("Nomor Urut Sampel", list_nus, index=None, placeholder= "Pilih salah satu")

        #Dokumen VSEN25.K
        st.write("------------------------------------------------------------------------------------")
        st.write("Dokumen VSEN25.K")
        form_values["Jumlah ART Wanita Kawin Usia 10-54 Tahun"] = st.number_input("R.305 Jumlah ART Wanita Kawin Usia 10-54 Tahun", min_value= 0)
        form_values["Jumlah ART diatas 60 Tahun"] = st.number_input("R.407 Jumlah ART diatas 60 Tahun", min_value= 0)
        form_values["Jumlah ART dibawah 10 Tahun"] = st.number_input("R.407 Jumlah ART dibawah 10 Tahun", min_value= 0)
        form_values["Jumlah ART dibawah 5 Tahun"] = st.number_input("R.407 Jumlah ART dibawah 5 Tahun", min_value=0)      
        form_values["Jumlah ART dibawah 1 Tahun"] = st.number_input("R.407 Jumlah ART dibawah 1 Tahun", min_value= 0)
        form_values["Tidak Mempunyai NIK"] = st.selectbox("R.505 Apakah ada ART yang tidak memiliki NIK atau berkode 5?", ["Ada", "Tidak ada"], placeholder="Pilih salah satu")
        form_values["Jumlah ART yang masih sekolah"] = st.number_input("R.605 berkode 1 atau R.611 berkode 2 Jumlah ART yang masih sekolah", min_value= 0)
        form_values["Buta Huruf"] = st.selectbox("R.608 kode 5 DAN R.609 kode 5 DAN R.610 kode 5 Apakah ada ART yang Buta Huruf?", ["Ada", "Tidak ada"], placeholder="Pilih salah satu")
        form_values["Luas Lantai Rumah"] = st.number_input("R.1604 Berapa Luas Lantai Bangunan Tempat Tinggal", min_value= 0)
        form_values["Kepemilikan Kendaraan Bermotor"] = st.selectbox("R.1801 H/J/K ada yang berkode 1 Apakah Rumah Tangga ini memiliki kendaraan bermotor?", ["Ada", "Tidak ada"], placeholder="Pilih salah satu")
        form_values["Penerimaan Bantuan Pemerintah"] = st.selectbox("R.1101 berkode A atau Blok XX ada yang berkode Ya untuk Penerimaan Bantuan Pemerintah?", ["Ada", "Tidak ada"], placeholder= "Pilih salah satu")

        ##Dokumen VSEN25.KP
        #Blok III
        st.write("------------------------------------------------------------------------------------")
        st.write("Dokumen VSEN25.KP")
        st.write("------------------------------------------------------------------------------------")
        st.write("Banyaknya ART dan Jumlah Komoditas yang Terisi")
        form_values["Jumlah ART"] = st.number_input("R.301 Banyaknya Anggota Rumah Tangga (ART)", min_value= 0)
        form_values["Jumlah Komoditas Makanan"] = st.number_input("R.304 Jumlah Komoditas Bahan Makanan, Bahan Minuman, dan Rokok yang Terisi", min_value= 0)
        form_values["Jumlah Komoditas Non Makanan"] = st.number_input("R.305 Jumlah Komoditas Barang-barang Bukan Makanan yang Terisi", min_value= 0)

        #Blok IV.1
        st.write("------------------------------------------------------------------------------------")
        st.write("Blok IV.1. Kewajaran Konsumsi Beras, Gula, dan Garam")
        form_values["Jumlah Beras dalam Kg"] = st.number_input("Blok IV.1 R.2 Jumlah Beras dalam Kg", min_value= 0.00)
        form_values["Jumlah Konsumsi Gula dalam Ons"] = st.number_input("Blok IV.1 R.160 Jumlah Konsumsi Gula Pasir dalam Ons", min_value= 0.00)
        form_values["Jumlah Konsumsi Garam dalam Gram"] = st.number_input("Blok IV.1 R.168 Jumlah Konsumsi Garam dalam Gram", min_value= 0.00)

        #Biaya yang seharusnya dikeluarkan jika mempunyai kendaraan bermotor
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai kendaraan bermotor")
        form_values["Pengeluaran Bensin dalam Liter"] = st.number_input("Blok IV.2 R.243 Pengeluaran Bensin atau Solar dalam Liter", min_value= 0.0)
        form_values["Pengeluaran Bensin dalam Rupiah"] = st.number_input("Blok IV.2 R.244 Pengeluaran Bensin atau Solar dalam Rupiah", min_value= 0)
        form_values["Pengeluaran Solar dalam Liter"] = st.number_input("Blok IV.2 R.245 Pengeluaran Bensin atau Solar dalam Liter", min_value= 0.0)
        form_values["Pengeluaran Solar dalam Rupiah"] = st.number_input("Blok IV.2 R.246 Pengeluaran Bensin atau Solar dalam Rupiah", min_value= 0)
        form_values["Pengeluaran Minyak Pelumas dalam Liter"] = st.number_input("Blok IV.2 R.249 Pengeluaran Minyak Pelumas dalam Liter", min_value= 0.0)
        form_values["Pengeluaran Minyak Pelumas dalam Rupiah"] = st.number_input("Blok IV.2 R.250 Pengeluaran Minyak Pelumas dalam Rupiah", min_value= 0)
        form_values["Pengeluaran Perbaikan dan Pemeliharaan Kendaraan Bermotor"] = st.number_input("Blok IV.2 R.251 Pengeluaran Perbaikan dan Pemeliharaan Kendaraan Bermotor", min_value= 0)
        form_values["Pengeluaran Biaya Transportasi Lainnya"] = st.number_input("Blok IV.2 R.301 Biaya Transportasi Lainnya (termasuk uang parkir dan karcis tol)", min_value= 0)
        form_values["Pengeluaran Pajak Kendaraan Bermotor"] = st.number_input("Blok IV.2 R.336 Pengeluaran Pajak Kendaraan Bermotor", min_value= 0)

        #Biaya yang seharusnya dikeluarkan jika mempunyai ART berusia dibawah 1 Tahun
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai ART berusia dibawah 1 Tahun")
        form_values["Biaya Melahirkan"] = st.number_input("Blok IV.2 R.276-R.282 Biaya Melahirkan (salah satu terisi)", min_value=0)
        form_values["Biaya Periksa Kehamilan"] = st.number_input("Blok IV.2 R.287 Biaya Periksa Kehamilan", min_value=0)
        form_values["Biaya Imunisasi"] = st.number_input("Blok IV.2 R.288 Biaya Imunisasi", min_value= 0)
        form_values["Biaya Pakaian Bayi"] = st.number_input("Blok IV.2 R.310 Biaya Pakaian Bayi (Termasuk popok bayi berbahan kain)", min_value= 0)
        form_values["Kereta Bayi"] = st.number_input("Blok IV.2 R.333 Biaya Kereta Bayi/Stroller)", min_value= 0)

        #Biaya yang seharusnya dikeluarkan jika mempunyai ART berusia dibawah 5 Tahun
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai ART berusia dibawah 5 Tahun")
        form_values["Mainan Anak"] = st.number_input("Blok IV.2 R.328 Pembelian Mainan Anak (Termasuk Sepeda Roda Tiga)", min_value=0)

        #Biaya yang seharusnya dikeluarkan jika mempunyai ART Wanita Kawin Usia 10 - 54 Tahun
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai ART Wanita Kawin Usia 10 - 54 Tahun")
        form_values["Barang Kecantikan dan Pembalut Wanita"] = st.number_input("Blok IV.2 R.270 Barang Kecantikan dan Pembalut Wanita", min_value= 0)
        form_values["Pengeluaran Keluarga Berencana"] = st.number_input("Blok IV.2 R.290 Pengeluaran Keluarga Berencana", min_value= 0)
        
        #Biaya yang seharusnya dikeluarkan jika mempunyai ART berusia diatas 60 Tahun dan/atau mempunyai ART berusia dibawah 1 Tahun
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai ART berusia diatas 60 Tahun dan/atau mempunyai ART berusia dibawah 1 Tahun")
        form_values["Biaya Pemeliharaan Kesehatan Lainnya"] = st.number_input("Blok IV.2 R.291 Biaya Pemeliharaan Kesehatan Lainnya", min_value= 0)

        #Biaya yang seharusnya dikeluarkan jika mempunyai ART yang masih bersekolah/baru masuk sekolah
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika mempunyai ART yang masih bersekolah/baru masuk sekolah")
        form_values["Sumbangan Pembangunan Sekolah"] = st.number_input("Blok IV.2 R.292 Sumbangan Pembangunan Sekolah", min_value= 0)
        form_values["Uang Sekolah dan Iuran Komite"] = st.number_input("Blok IV.2 R.293 Uang Sekolah dan Iuran Komite", min_value= 0)
        form_values["Iuran Sekolah Lainnya"] = st.number_input("Blok IV.2 R.294 Iuran Sekolah Lainnya", min_value= 0)
        form_values["Biaya Buku Pelajaran"] = st.number_input("Blok IV.2 R.295 Biaya Buku Pelajaran", min_value= 0)
        form_values["Alat-alat Tulis"] = st.number_input("Blok IV.2 R.296 Alat-alat Tulis", min_value= 0)
        form_values["Uang Kursus di Luar Sekolah"] = st.number_input("Blok IV.2 R.297 Uang Kursus di Luar Sekolah", min_value= 0)
        
        #Biaya yang seharusnya dikeluarkan jika tidak mempunyai kendaraan bermotor
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang seharusnya dikeluarkan jika tidak mempunyai kendaraan bermotor")
        form_values["Pengeluaran Transportasi Darat"] = st.number_input("Blok IV.2 R.298 Pengeluaran Transportasi Darat (termasuk ojek, taksi, minibus, bus, sewa mobil)", min_value= 0)
        
        #Penerimaan Bantuan Pemerintah
        st.write("------------------------------------------------------------------------------------")
        st.write("Penerimaan Bantuan Pemerintah")
        form_values["Bantuan Pemerintah dalam bentuk uang"] = st.number_input("Blok VE R.2 Kolom 2 Bantuan Pemerintah dalam bentuk uang", min_value= 0)
        form_values["Bantuan Pemerintah dalam bentuk barang"] = st.number_input("Blok VE R.2 Kolom 3 Bantuan Pemerintah dalam bentuk barang", min_value= 0)
        
        #Biaya yang WAJIB dikeluarkan oleh rumah tangga
        st.write("------------------------------------------------------------------------------------")
        st.write("Biaya yang WAJIB dikeluarkan oleh rumah tangga")
        form_values["Pemeliharaan Rumah dan Perbaikan Ringan"] = st.number_input("Blok IV.2 R.232 Pemeliharaan Rumah dan Perbaikan Ringan", min_value= 0)
        form_values["Pengeluaran untuk Listrik dalam kWh"] = st.number_input("Blok IV.2 R.233 Pengeluaran untuk Listrik dalam kWh", min_value= 0.0)
        form_values["Pengeluaran untuk Listrik dalam Rupiah"] = st.number_input("Blok IV.2 R.234 Pengeluaran untuk Listrik dalam Rupiah", min_value= 0)
        form_values["Pengeluaran LPG dalam Kg"] = st.number_input("Blok IV.2 R.252 Pengeluaran LPG dalam Kg", min_value= 0.0)
        form_values["Pengeluaran LPG dalam Rupiah"] = st.number_input("Blok IV.2 R.253 Pengeluaran LPG dalam Rupiah", min_value= 0)
        form_values["Pengeluaran Kebutuhan Lainnya untuk Rumah"] = st.number_input("Blok IV.2 R.262 Pengeluaran Kebutuhan Lainnya untuk Rumah (termasuk cairan pembersih lantai, pewangi ruangan, obat nyamuk, bola lampu, dll)", min_value= 0)
        form_values["Pulsa HP"] = st.number_input("Blok IV.2 R.264 Pulsa HP", min_value= 0)
        form_values["Biaya Internet atau Warnet"] = st.number_input("Blok IV.2 R.266 Biaya Internet", min_value= 0)
        form_values["Sabun Mandi, Pasta Gigi, Sikat Gigi, dan Sampo"] = st.number_input("Blok IV.2 R.269 Sabun Mandi, Pasta Gigi, Sikat Gigi, dan Sampo", min_value= 0)
        form_values["Perawatan Kulit, Muka, Kuku, Rambut"] = st.number_input("Blok IV.2 R.271 Perawatan Kulit, Muka, Kuku, Rambut", min_value= 0)
        form_values["Sabun Cuci"] = st.number_input("Blok IV.2 R.272 Sabun Cuci", min_value= 0)
        form_values["Bahan Pemeliharaan Pakaian"] = st.number_input("Blok IV.2 R.273 Bahan Pemeliharaan Pakaian", min_value= 0)
        form_values["Biaya Barang Lainnya"] = st.number_input("Blok IV.2 R.275 Barang Lainnya (Termasuk Tisu, Kantong Plastik, cotton bud, Pampers, Minyak Telon, dll)", min_value= 0)
        form_values["Jasa Lembaga Keuangan"] = st.number_input("Blok IV.2 R.305 Jasa Lembaga Keuangan (termasuk biaya transfer)", min_value= 0)
        form_values["Jasa Lainnya"] = st.number_input("Blok IV.2 R.306 Jasa Lainnya (termasuk biaya pembuatan KTP, SIM, Akta Kelahiran, fotokopi , jasa penitipan bayi)", min_value= 0)
        form_values["Pengeluaran Pajak PBB"] = st.number_input("Blok IV.2 R.335 Pengeluaran Pajak PBB", min_value= 0)
        form_values["Pengeluaran untuk Asuransi Kesehatan"] = st.number_input("Blok IV.2 R.338 Pengeluaran untuk Asuransi Kesehatan", min_value= 0)

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

    #Opsi CSV Upload
    with st.form("Upload Template CSV", enter_to_submit= False, clear_on_submit= True):
        file_csv_upload = st.file_uploader("Upload Template CSV yang Sudah Diisi Disini...")

        upload_button = st.form_submit_button("Upload")

        if upload_button:
            if file_csv_upload is not None :
                temp_file = pd.read_csv(file_csv_upload, sep=";")
                append_data = pd.concat([data, temp_file], ignore_index=True, join="inner")
                append_data = append_data.drop_duplicates(subset= ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel"], keep= "last")
                append_data.to_csv(csv_file_path, index=False)
                st.success("Dataframe berhasil diperbarui, kamu bisa lakukan review pada menu Review Lembar Jaga ya!")
            else:
                st.warning("Masukkan terlebih dahulu Template CSV sebelum klik Upload!")
    
    st.write("---")
    st.write("Data Terkini :")
    data_terkini = pd.read_csv("arunika_app/data_input_response.csv")
    st.dataframe(data_terkini, hide_index=True)

with tab2:
    data_edit = pd.read_csv(csv_file_path)

    st.subheader("Perbaikan Data")
    st.caption("1. Halaman ini khusus untuk Pemeriksa!")
    st.caption("2. Masukkan Kode Akses Pemeriksa dengan benar. Maka akses kotak filter Nomor Kode Sampel akan terbuka.")
    st.caption("3. Lakukan perbaikan pada kolom yang bersesuaian. Perhatian! Saat melakukan perbaikan terkadang perlu dua kali input, mohon untuk diperiksa kembali setelah diperbaiki.")

    with st.form("Kode Akses Pemeriksa", enter_to_submit= False, clear_on_submit= False):
        userID_key = st.text_input("Masukkan UserID", key="username")
        password_key = st.text_input("Masukkan Password", key="password")

        login_button = st.form_submit_button("Login")
    
    closed_access = True
    if login_button:
        if userID_key == "admin_arunika" and password_key == "lakukanperbaikan":
            closed_access = False
            st.success("Silakan lakukan perbaikan data!")
        else:
            st.warning("UserID dan/atau Password salah!")
    
    query = st.text_input("Masukkan Nomor Kode Sampel (NKS) :", disabled=closed_access)

    if query:
        mask = data_terkini.map(lambda x: query in str(x)).any(axis=1)
        data_edit = st.data_editor(data_terkini[mask], column_config={
            "Tidak Mempunyai NIK" : st.column_config.SelectboxColumn(options=["Ada", "Tidak ada"]),
            "Buta Huruf" : st.column_config.SelectboxColumn(options=["Ada", "Tidak ada"]),
            "Kepemilikan Kendaraan Bermotor" : st.column_config.SelectboxColumn(options=["Ada", "Tidak ada"]),
            "Penerimaan Bantuan Pemerintah" : st.column_config.SelectboxColumn(options=["Ada", "Tidak ada"])
            },                     
            hide_index=True)
        hasil_perbaikan = pd.concat([data_terkini, data_edit], ignore_index=True)
        data_perbaikan = hasil_perbaikan.drop_duplicates(subset= ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel"], keep= "last")
        data_perbaikan.to_csv(csv_file_path, index=False)

with tab3:
    #Import dataframe hasil masukan
    hasil_input = pd.read_csv(csv_file_path)

    #Import List Kode Anomali
    kode_anomali = pd.read_csv("arunika_app/List_Anomali.csv", sep="\t")
    kode_anomali = kode_anomali["Kode Anomali"].to_list()

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
        
        with st.container(height= 500, border= True):
            st.write("## Pastikan isian dokumen sudah diperbaiki dan dientri ulang pada menu Entri Lembar Jaga setelah diperbaiki!")
            st.write("------------------")
            st.write("Hasil pemeriksaan untuk rumah tangga ini adalah sebagai berikut:")

            #Rule Validasi Pemeriksaan

            if review_temp["Tidak Mempunyai NIK"].values == "Ada" :
                st.markdown(f"- {kode_anomali[0]}. Konfirmasi ulang ke petugas! Jika benar, berikan penjelasan secara rinci di Blok Catatan.")

            if review_temp["Buta Huruf"].values == "Ada" :
                st.markdown(f"- {kode_anomali[1]}. Konfirmasi ulang ke petugas! Jika benar, berikan penjelasan secara rinci di Blok Catatan.")
            
            if review_temp["Luas Lantai Rumah"].values/review_temp["Jumlah ART"].values < 8 :
                st.markdown(f"- {kode_anomali[2]}. Konfirmasi ulang ke petugas! Jika benar, berikan penjelasan secara rinci di Blok Catatan.")

            if review_temp["Jumlah Komoditas Makanan"].values < 13 :
                st.markdown(f"- {kode_anomali[3]}. Konfirmasi ulang ke petugas!")
            
            if review_temp["Jumlah Komoditas Non Makanan"].values < 19 :
                st.markdown(f"- {kode_anomali[4]}. Konfirmasi ulang ke petugas!")
            
            if review_temp["Jumlah Beras dalam Kg"].values/review_temp["Jumlah ART"].values < 1.8 or review_temp["Jumlah Beras dalam Kg"].values/review_temp["Jumlah ART"].values >= 2.8 :
                st.markdown(f"- {kode_anomali[5]}. Konfirmasi ulang ke petugas!")
            
            if review_temp["Jumlah Konsumsi Gula dalam Ons"].values/review_temp["Jumlah ART"].values > 2.8 :
                st.markdown(f"- {kode_anomali[6]}. Konfirmasi ulang ke petugas!")
            
            if review_temp["Jumlah Konsumsi Garam dalam Gram"].values/review_temp["Jumlah ART"].values > 28 :
                st.markdown(f"- {kode_anomali[7]}. Konfirmasi ulang ke petugas!")

            if review_temp["Kepemilikan Kendaraan Bermotor"].values == "Ada":
                if review_temp["Pengeluaran Bensin dalam Rupiah"].values == 0 or review_temp["Pengeluaran Solar dalam Rupiah"].values == 0 :
                    st.markdown(f"- {kode_anomali[8]}. Konfirmasi ulang ke petugas!")
                if review_temp["Pengeluaran Minyak Pelumas dalam Rupiah"].values == 0 :
                    st.markdown(f"- {kode_anomali[9]}. Konfirmasi ulang ke petugas!")
                if review_temp["Pengeluaran Perbaikan dan Pemeliharaan Kendaraan Bermotor"].values == 0 :
                    st.markdown(f"- {kode_anomali[10]}. Konfirmasi ulang ke petugas!")
                if review_temp["Pengeluaran Pajak Kendaraan Bermotor"].values == 0 :
                    st.markdown(f"- {kode_anomali[11]}. Konfirmasi ulang ke petugas!")

            if review_temp["Jumlah ART dibawah 1 Tahun"].values > 0 :
                if review_temp["Biaya Melahirkan"].values == 0 :
                    st.markdown(f"- {kode_anomali[12]}. Konfirmasi ulang ke petugas!")
                if review_temp["Biaya Periksa Kehamilan"].values == 0 :
                    st.markdown(f"- {kode_anomali[13]}. Konfirmasi ulang ke petugas!")
                if review_temp["Biaya Imunisasi"].values == 0 :
                    st.markdown(f"- {kode_anomali[14]}. Konfirmasi ulang ke petugas!")
                if review_temp["Biaya Pakaian Bayi"].values == 0 :
                    st.markdown(f"- {kode_anomali[15]}. Konfirmasi ulang ke petugas!")
                if review_temp["Biaya Barang Lainnya"].values == 0 :
                    st.markdown(f"- {kode_anomali[16]}. Konfirmasi ulang ke petugas!")
                if review_temp["Kereta Bayi"].values == 0 :
                    st.markdown(f"- {kode_anomali[17]}. Konfirmasi ulang ke petugas!")

            if review_temp["Jumlah ART dibawah 5 Tahun"].values > 0 :
                if review_temp["Mainan Anak"].values == 0 :
                    st.markdown(f"- {kode_anomali[18]}. Konfirmasi ulang ke petugas!")

            if review_temp["Jumlah ART Wanita Kawin Usia 10-54 Tahun"].values > 0 :
                if review_temp["Barang Kecantikan dan Pembalut Wanita"].values == 0 :
                    st.markdown(f"- {kode_anomali[19]}. Konfirmasi ulang ke petugas!")
                if review_temp["Pengeluaran Keluarga Berencana"].values == 0 :
                    st.markdown(f"- {kode_anomali[20]}. Konfirmasi ulang ke petugas!")

            if review_temp["Jumlah ART diatas 60 Tahun"].values > 0 or review_temp["Jumlah ART dibawah 1 Tahun"].values > 0 :
                if review_temp["Biaya Pemeliharaan Kesehatan Lainnya"].values == 0 :
                    st.markdown(f"- {kode_anomali[21]}. Konfirmasi ulang ke petugas!")

            if review_temp["Jumlah ART yang masih sekolah"].values > 0 :
                if review_temp["Sumbangan Pembangunan Sekolah"].values == 0 :
                    st.markdown(f"- {kode_anomali[22]}. Konfirmasi ulang ke petugas!")
                if review_temp["Uang Sekolah dan Iuran Komite"].values == 0 :
                    st.markdown(f"- {kode_anomali[23]}. Konfirmasi ulang ke petugas!")
                if review_temp["Iuran Sekolah Lainnya"].values == 0 :
                    st.markdown(f"- {kode_anomali[24]}. Konfirmasi ulang ke petugas!")
                if review_temp["Biaya Buku Pelajaran"].values == 0 :
                    st.markdown(f"- {kode_anomali[25]}. Konfirmasi ulang ke petugas!")
                if review_temp["Alat-alat Tulis"].values == 0 :
                    st.markdown(f"- {kode_anomali[26]}. Konfirmasi ulang ke petugas!")
                if review_temp["Uang Kursus di Luar Sekolah"].values == 0 :
                    st.markdown(f"- {kode_anomali[27]}. Konfirmasi ulang ke petugas!")

            if review_temp["Kepemilikan Kendaraan Bermotor"].values == "Tidak ada" :
                if review_temp["Pengeluaran Transportasi Darat"].values == 0 :
                    st.markdown(f"- {kode_anomali[28]}. Konfirmasi ulang ke petugas!")

            if review_temp["Penerimaan Bantuan Pemerintah"].values == "Ada" :
                if review_temp["Bantuan Pemerintah dalam bentuk uang"].values == 0 and review_temp["Bantuan Pemerintah dalam bentuk barang"].values == 0 :
                    st.markdown(f"- {kode_anomali[29]}. Konfirmasi ulang ke petugas!")

            for var_wajib in list_var_wajib :
                if review_temp[var_wajib].values == 0 :
                    st.markdown(f"- {kode_anomali[30]}. Konfirmasi ulang ke petugas!")
                    break

with tab4:
    #Import dataframe hasil masukan
    response_data = pd.read_csv(csv_file_path)

    #Import List Kode Anomali
    kode_anomali = pd.read_csv("arunika_app/List_Anomali.csv", sep="\t")
    kode_anomali = kode_anomali["Kode Anomali"].to_list()

    #Anomali dan Rumah Tangga yang terkait
    st.subheader("Daftar Anomali dan Hasil Pemeriksaan Terkini secara Umum")
    st.write("---")

    #Ada ART yang tidak mempunyai NIK
    st.write(kode_anomali[0])
    st.write(response_data.loc[response_data["Tidak Mempunyai NIK"] == "Ada", ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Tidak Mempunyai NIK"]])

    #Ada ART yang buta huruf
    st.write(kode_anomali[1])
    st.write(response_data.loc[response_data["Buta Huruf"] == "Ada", ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Buta Huruf"]])
    
    #Luas Lantai Rumah kurang dari 8 m2 per kapita
    st.write(kode_anomali[2])
    st.write(response_data.loc[(response_data["Luas Lantai Rumah"]/response_data["Jumlah ART"] < 8), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART", "Luas Lantai Rumah"]])

    #Jumlah Komoditas Makanan kurang dari 13
    st.write(kode_anomali[3])
    st.write(response_data.loc[response_data["Jumlah Komoditas Makanan"] < 13, ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah Komoditas Makanan"]])

    #Jumlah Komoditas Non Makanan kurang dari 19
    st.write(kode_anomali[4])
    st.write(response_data.loc[response_data["Jumlah Komoditas Non Makanan"] < 19, ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah Komoditas Non Makanan"]])

    #Jumlah Konsumsi Beras Kg/Kapita kurang dari 1.8 atau lebih dari sama dengan 2.8
    st.write(kode_anomali[5])
    st.write(response_data.loc[(response_data["Jumlah Beras dalam Kg"]/response_data["Jumlah ART"] < 1.8) | (response_data["Jumlah Beras dalam Kg"]/response_data["Jumlah ART"] >= 2.8), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART", "Jumlah Beras dalam Kg"] ])

    #Jumlah Konsumsi Gula Ons/Kapita > 2.5
    st.write(kode_anomali[6])
    st.write(response_data.loc[(response_data["Jumlah Konsumsi Gula dalam Ons"]/response_data["Jumlah ART"] > 2.5), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART", "Jumlah Konsumsi Gula dalam Ons"] ])

    #Jumlah Konsumsi Garam Gram/Kapita > 28
    st.write(kode_anomali[7])
    st.write(response_data.loc[(response_data["Jumlah Konsumsi Garam dalam Gram"]/response_data["Jumlah ART"] > 28), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART", "Jumlah Konsumsi Garam dalam Gram"] ])

    #Memiliki Kendaraan Bermotor akan tetapi Pengeluaran Bensin atau Solar tidak ada
    st.write(kode_anomali[8])
    st.write(response_data.loc[(response_data["Kepemilikan Kendaraan Bermotor"] == "Ada") & (response_data["Pengeluaran Bensin dalam Rupiah"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Kepemilikan Kendaraan Bermotor", "Pengeluaran Bensin dalam Rupiah"] ])
    st.write(response_data.loc[(response_data["Kepemilikan Kendaraan Bermotor"] == "Ada") & (response_data["Pengeluaran Solar dalam Rupiah"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Kepemilikan Kendaraan Bermotor", "Pengeluaran Solar dalam Rupiah"] ])

    #Memiliki Kendaraan Bermotor akan tetapi Pengeluaran Minyak Pelumas tidak ada
    st.write(kode_anomali[9])
    st.write(response_data.loc[(response_data["Kepemilikan Kendaraan Bermotor"] == "Ada") & (response_data["Pengeluaran Minyak Pelumas dalam Rupiah"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Kepemilikan Kendaraan Bermotor", "Pengeluaran Minyak Pelumas dalam Rupiah"] ])

    #Memiliki Kendaraan Bermotor akan tetapi Pengeluaran Perbaikan dan Pemeliharaan Kendaraan Bermotor tidak ada
    st.write(kode_anomali[10])
    st.write(response_data.loc[(response_data["Kepemilikan Kendaraan Bermotor"] == "Ada") & (response_data["Pengeluaran Perbaikan dan Pemeliharaan Kendaraan Bermotor"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Kepemilikan Kendaraan Bermotor", "Pengeluaran Perbaikan dan Pemeliharaan Kendaraan Bermotor"] ])

    #Memiliki Kendaraan Bermotor akan tetapi Pengeluaran Pajak Kendaraan Bermotor tidak ada
    st.write(kode_anomali[11])
    st.write(response_data.loc[(response_data["Kepemilikan Kendaraan Bermotor"] == "Ada") & (response_data["Pengeluaran Pajak Kendaraan Bermotor"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Kepemilikan Kendaraan Bermotor", "Pengeluaran Pajak Kendaraan Bermotor"] ])

    #Terdapat ART berusia dibawah 1 Tahun akan tetapi tidak ada Biaya Melahirkan
    st.write(kode_anomali[12])
    st.write(response_data.loc[(response_data["Jumlah ART dibawah 1 Tahun"] > 0) & (response_data["Biaya Melahirkan"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART dibawah 1 Tahun", "Biaya Melahirkan"] ])

    #Terdapat ART berusia dibawah 1 Tahun akan tetapi tidak ada Biaya Periksa Kehamilan
    st.write(kode_anomali[13])
    st.write(response_data.loc[(response_data["Jumlah ART dibawah 1 Tahun"] > 0) & (response_data["Biaya Periksa Kehamilan"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART dibawah 1 Tahun", "Biaya Periksa Kehamilan"] ])

    #Terdapat ART berusia dibawah 1 Tahun akan tetapi tidak ada Biaya Imunisasi
    st.write(kode_anomali[14])
    st.write(response_data.loc[(response_data["Jumlah ART dibawah 1 Tahun"] > 0) & (response_data["Biaya Imunisasi"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART dibawah 1 Tahun", "Biaya Imunisasi"] ])

    #Terdapat ART berusia dibawah 1 Tahun akan tetapi tidak ada Biaya Pakaian Bayi
    st.write(kode_anomali[15])
    st.write(response_data.loc[(response_data["Jumlah ART dibawah 1 Tahun"] > 0) & (response_data["Biaya Pakaian Bayi"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART dibawah 1 Tahun", "Biaya Pakaian Bayi"] ])

    #Terdapat ART berusia dibawah 1 Tahun akan tetapi tidak ada Biaya Barang Lainnya
    st.write(kode_anomali[16])
    st.write(response_data.loc[(response_data["Jumlah ART dibawah 1 Tahun"] > 0) & (response_data["Biaya Barang Lainnya"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART dibawah 1 Tahun", "Biaya Barang Lainnya"] ])

    #Terdapat ART berusia dibawah 1 Tahun akan tetapi tidak ada Kereta Bayi (Barang Tahan Lama Lainnya)
    st.write(kode_anomali[17])
    st.write(response_data.loc[(response_data["Jumlah ART dibawah 1 Tahun"] > 0) & (response_data["Kereta Bayi"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART dibawah 1 Tahun", "Kereta Bayi"] ])

    #Terdapat ART berusia dibawah 5 Tahun akan tetapi tidak ada Pembelian Mainan Anak
    st.write(kode_anomali[18])
    st.write(response_data.loc[(response_data["Jumlah ART dibawah 5 Tahun"] > 0) & (response_data["Mainan Anak"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART dibawah 5 Tahun", "Mainan Anak"] ])

    #Terdapat ART Wanita Kawin Usia 10-54 Tahun akan tetapi tidak ada Pengeluaran Barang Kecantikan dan Pembalut Wanita
    st.write(kode_anomali[19])
    st.write(response_data.loc[(response_data["Jumlah ART Wanita Kawin Usia 10-54 Tahun"] > 0) & (response_data["Barang Kecantikan dan Pembalut Wanita"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART Wanita Kawin Usia 10-54 Tahun", "Barang Kecantikan dan Pembalut Wanita"] ])

    #Terdapat ART Wanita Kawin Usia 10-54 Tahun akan tetapi tidak ada Pengeluaran Keluarga Berencana
    st.write(kode_anomali[20])
    st.write(response_data.loc[(response_data["Jumlah ART Wanita Kawin Usia 10-54 Tahun"] > 0) & (response_data["Pengeluaran Keluarga Berencana"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART Wanita Kawin Usia 10-54 Tahun", "Pengeluaran Keluarga Berencana"] ])

    #Terdapat ART berusia diatas 60 Tahun atau ART berusia dibawah 1 Tahun akan tetapi tidak ada Biaya Pemeliharaan Kesehatan Lainnya
    st.write(kode_anomali[21])
    st.write(response_data.loc[(response_data["Jumlah ART diatas 60 Tahun"] > 0) & (response_data["Biaya Pemeliharaan Kesehatan Lainnya"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART diatas 60 Tahun", "Biaya Pemeliharaan Kesehatan Lainnya"] ])
    st.write(response_data.loc[(response_data["Jumlah ART dibawah 1 Tahun"] > 0 ) & (response_data["Biaya Pemeliharaan Kesehatan Lainnya"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART dibawah 1 Tahun", "Biaya Pemeliharaan Kesehatan Lainnya"] ])

    #Terdapat ART yang masih bersekolah akan tetapi tidak ada Sumbangan Pembangunan Sekolah
    st.write(kode_anomali[22])
    st.write(response_data.loc[(response_data["Jumlah ART yang masih sekolah"] > 0) & (response_data["Sumbangan Pembangunan Sekolah"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART yang masih sekolah", "Sumbangan Pembangunan Sekolah"] ])

    #Terdapat ART yang masih bersekolah akan tetapi tidak ada Uang Sekolah dan Iuran Komite
    st.write(kode_anomali[23])
    st.write(response_data.loc[(response_data["Jumlah ART yang masih sekolah"] > 0) & (response_data["Uang Sekolah dan Iuran Komite"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART yang masih sekolah", "Uang Sekolah dan Iuran Komite"] ])

    #Terdapat ART yang masih bersekolah akan tetapi tidak ada Iuran Sekolah Lainnya
    st.write(kode_anomali[24])
    st.write(response_data.loc[(response_data["Jumlah ART yang masih sekolah"] > 0) & (response_data["Iuran Sekolah Lainnya"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART yang masih sekolah", "Iuran Sekolah Lainnya"] ])

    #Terdapat ART yang masih bersekolah akan tetapi tidak ada Biaya Buku Pelajaran
    st.write(kode_anomali[25])
    st.write(response_data.loc[(response_data["Jumlah ART yang masih sekolah"] > 0) & (response_data["Biaya Buku Pelajaran"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART yang masih sekolah", "Biaya Buku Pelajaran"] ])

    #Terdapat ART yang masih bersekolah akan tetapi tidak ada Alat-alat Tulis
    st.write(kode_anomali[26])
    st.write(response_data.loc[(response_data["Jumlah ART yang masih sekolah"] > 0) & (response_data["Alat-alat Tulis"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART yang masih sekolah", "Alat-alat Tulis"] ])

    #Terdapat ART yang masih bersekolah akan tetapi tidak ada Uang Kursus di Luar Sekolah
    st.write(kode_anomali[27])
    st.write(response_data.loc[(response_data["Jumlah ART yang masih sekolah"] > 0) & (response_data["Uang Kursus di Luar Sekolah"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Jumlah ART yang masih sekolah", "Uang Kursus di Luar Sekolah"] ])

    #Tidak Memiliki Kendaraan Bermotor akan tetapi Pengeluaran Transportasi Darat tidak ada
    st.write(kode_anomali[28])
    st.write(response_data.loc[(response_data["Kepemilikan Kendaraan Bermotor"] == "Tidak ada") & (response_data["Pengeluaran Transportasi Darat"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Kepemilikan Kendaraan Bermotor", "Pengeluaran Transportasi Darat"] ])

    #Menerima Bantuan Pemerintah akan tetapi rincian Bantuan Pemerintah dalam bentuk uang atau barang tidak ada
    st.write(kode_anomali[29])
    st.write(response_data.loc[(response_data["Penerimaan Bantuan Pemerintah"] == "Ada") & (response_data["Bantuan Pemerintah dalam bentuk uang"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Penerimaan Bantuan Pemerintah", "Bantuan Pemerintah dalam bentuk uang"] ])
    st.write(response_data.loc[(response_data["Penerimaan Bantuan Pemerintah"] == "Ada") & (response_data["Bantuan Pemerintah dalam bentuk barang"] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", "Penerimaan Bantuan Pemerintah", "Bantuan Pemerintah dalam bentuk barang"] ])

    #Biaya Wajib ada yang tidak terisi
    st.write(kode_anomali[30])
    
    for var_wajib in list_var_wajib :
        st.write(response_data.loc[(response_data[var_wajib] == 0), ["Nama PML", "Nama PPL", "NKS", "Nomor Urut Sampel", var_wajib] ])

with tab5:
    #Metriks Dataframe
    data_input = pd.read_csv(csv_file_path)
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
    st.dataframe(data_input, hide_index=True)
                
with tab6:
    st.title("Progres Pemeriksaan Dokumen :bar_chart:")
    st.write("---")
    
    progres_pml = data_input.groupby(by = ["Nama PML", "NKS"]).NKS.value_counts()
    st.write("Jumlah Sampel yang Sudah Diperiksa :", progres_pml)

    st.write("---")
    sum_nks_df = data_input.groupby(by="Nama PML").NKS.count().sort_values(ascending=False).reset_index()
    st.bar_chart(data=sum_nks_df.sort_values(by="NKS", ascending=True), x="Nama PML", y="NKS", x_label= "Pemeriksa", y_label= "Jumlah Sampel")
