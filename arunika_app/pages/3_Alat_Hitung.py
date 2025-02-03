import streamlit as st
import pandas as pd
import os

#Judul Halaman
st.title("Alat Hitung Susenas 2025 :computer:")
st.markdown("Halaman ini masih dalam pengembangan")


masih_dikembangkan = """ tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Imputasi dan Konverter", "Blok IV.3.2", "Blok IV.3.3", "Blok V", "Blok VI", "Blok VII"])

with tab1:
    st.subheader("Imputasi dan Konverter")

with tab2:
    #Blok IV.3.2
    st.write("")
    st.subheader("Blok IV.3.2")
    rinc_432_15_3 = st.number_input("Subjumlah Pembelian Seminggu Terakhir", min_value=0)
    st.success(f"{rinc_432_15_3:,.0f}")
    rinc_432_15_4a = st.number_input("Subjumlah Produksi Sendiri Seminggu Terakhir", min_value=0)
    st.success(f"{rinc_432_15_4a:,.0f}")
    rinc_432_15_4b = st.number_input("Subjumlah Pemberian Seminggu Terakhir", min_value=0)
    st.success(f"{rinc_432_15_4b:,.0f}")
    rinc_432_15_5 = rinc_432_15_3 + rinc_432_15_4a + rinc_432_15_4b #Total Subjumlah
    st.metric(label="R.432.15(5) SUBJUMLAH", value=f"Rp. {rinc_432_15_5:,.0f}", border=True)
    rinc_432_16 = rinc_432_15_5*30/7 #Rata-rata pengeluaran makanan sebulan
    st.metric(label="R.432.16(5) RATA-RATA PENGELUARAN MAKANAN SEBULAN", value=f"Rp. {rinc_432_16:,.0f}", border=True)

with tab3:
    #Blok IV.3.3
    st.write("")
    st.subheader("Blok IV.3.3")
    rinc_433_1_a = st.number_input("Perumahan dan Fasilitas Rumah Tangga Sebulan Terakhir (R. 226 Kolom 4)", min_value=0)
    st.success(f"{rinc_433_1_a:,.0f}")
    rinc_433_1_b = st.number_input("Perumahan dan Fasilitas Rumah Tangga Setahun Terakhir (R. 226 Kolom 5)", min_value=0)
    st.success(f"{rinc_433_1_b:,.0f}")
    rinc_433_2_a = st.number_input("Aneka Barang dan Jasa Sebulan Terakhir (R. 268 Kolom 4)", min_value=0)
    st.success(f"{rinc_433_2_a:,.0f}")
    rinc_433_2_b = st.number_input("Aneka Barang dan Jasa Setahun Terakhir (R. 268 Kolom 5)", min_value=0)
    st.success(f"{rinc_433_2_b:,.0f}")
    rinc_433_3 = st.number_input("Pakaian, Alas Kaki, dan Tutup Kepala (R. 307)", min_value=0)
    st.success(f"{rinc_433_3:,.0f}")
    rinc_433_4 = st.number_input("Barang Tahan Lama (R. 316)", min_value=0)
    st.success(f"{rinc_433_4:,.0f}")
    rinc_433_5 = st.number_input("Pajak, Pungutan, dan Asuransi (R. 334)", min_value=0)
    st.success(f"{rinc_433_5:,.0f}")
    rinc_433_6 = st.number_input("Keperluan Pesta dan Upacara/Kenduri (R. 341)", min_value=0)
    st.success(f"{rinc_433_6:,.0f}")
    rinc_433_7_a = rinc_433_1_a + rinc_433_2_a #Jumlah pengeluaran sebulan terakhir
    st.metric(label="R.433.7A(3) Jumlah Pengeluaran Barang-Barang Bukan Makanan Sebulan Terakhir", value=f"Rp. {rinc_433_7_a:,.0f}", border=True)
    rinc_433_7_b = rinc_433_1_b + rinc_433_2_b + rinc_433_3 + rinc_433_4 + rinc_433_5 + rinc_433_6 #Jumlah pengeluaran setahun terakhir
    st.metric(label="R.433.7B(4) Jumlah Pengeluaran Barang-Barang Bukan Makanan Setahun Terakhir", value=f"Rp. {rinc_433_7_b:,.0f}", border=True)
    rinc_433_8 = rinc_433_7_a +(rinc_433_7_b/12) #Rata-rata pengeluaran bukan makanan sebulan
    st.metric(label="R.433.8(3) Rata-rata Pengeluaran Bukan Makanan Sebulan", value=f"Rp. {rinc_433_8:,.0f}", border=True)
    rinc_433_9 = rinc_432_16 + rinc_433_8 #Rata-rata pengeluaran rumah tangga sebulan
    st.metric(label="R.433.9(3) Rata-rata Pengeluaran Rumah Tangga Sebulan", value=f"Rp. {rinc_433_9:,.0f}", border=True)

with tab4:
    #Blok VA
    st.write("Blok VA PENDAPATAN DARI UPAH/GAJI BAIK BERUPA UANG MAUPUN BARANG/JASA YANG DITERIMA SELAMA SETAHUN TERAKHIR")
    rinc_5A_5_sum = st.number_input("Jumlah Upah/gaji dalam Bentuk Uang", min_value=0)
    st.success(f"{rinc_5A_5_sum:,.0f}")
    rinc_5A_6_sum = st.number_input("Jumlah Upah/gaji dalam Bentuk Barang/Jasa", min_value=0)
    st.success(f"{rinc_5A_6_sum:,.0f}")
    rinc_5A_7_sum = st.number_input("Jumlah Lembur, Honorarium, THR", min_value=0)
    st.success(f"{rinc_5A_7_sum:,.0f}")

    #Blok VB
    st.write("---")
    st.write("Blok VB PENDAPATAN DARI USAHA RUMAH TANGGA SELAMA SETAHUN TERAKHIR")
    rinc_5B_5_sum = st.number_input("R5B Jumlah Nilai Produksi", min_value=0)
    st.success(f"{rinc_5B_5_sum:,.0f}")
    rinc_5B_6_sum = st.number_input("R5B Jumlah Biaya Produksi", min_value=0)
    st.success(f"{rinc_5B_6_sum:,.0f}")
    rinc_5B_7_sum = rinc_5B_5_sum - rinc_5B_6_sum
    st.metric(label="R5B Surplus Usaha/*Mixed Income*", value=f"Rp. {rinc_5B_7_sum:,.0f}", border=True)

    #Blok VC
    st.write("---")
    st.write("Blok VC PENDAPATAN DARI PRODUKSI RUMAH TANGGA YANG DIKONSUMSI/DIGUNAKAN SENDIRI SELAMA SETAHUN TERAKHIR")
    rinc_5C_2_sum = st.number_input("R5C Jumlah Nilai Produksi", min_value=0)
    st.success(f"{rinc_5C_2_sum:,.0f}")
    rinc_5C_3_sum = st.number_input("R5C Jumlah Biaya Produksi", min_value=0)
    st.success(f"{rinc_5C_3_sum:,.0f}")
    rinc_5C_4_sum = rinc_5C_2_sum - rinc_5C_3_sum
    st.metric(label="R5C Jumlah Surplus Usaha/*Mixed Income*", value=f"Rp. {rinc_5C_4_sum:,.0f}", border=True)

    #Blok VD
    st.write("---")
    st.write("Blok VD PENDAPATAN KEPEMILIKAN SELAMA SETAHUN TERAKHIR")
    rinc_5D_2_sum = st.number_input("R5D Jumlah Diterima", min_value=0)
    st.success(f"{rinc_5D_2_sum:,.0f}")
    rinc_5D_3_sum = st.number_input("R5D Jumlah Dibayar", min_value=0)
    st.success(f"{rinc_5D_3_sum:,.0f}")

    #Blok VE
    st.write("---")
    st.write("Blok VE TRANSFER BERJALAN (SELAIN ASET) SELAMA SETAHUN TERAKHIR")
    rinc_5E_2_sum = st.number_input("R5E Jumlah Transfer Diterima (Uang)", min_value=0)
    st.success(f"{rinc_5E_2_sum:,.0f}")
    rinc_5E_3_sum = st.number_input("R5E Jumlah Transfer Diterima (Barang/Jasa)", min_value=0)
    st.success(f"{rinc_5E_3_sum:,.0f}")
    rinc_5E_4_sum = st.number_input("R5E Jumlah Transfer Dibayarkan/Diberikan (Uang)", min_value=0)
    st.success(f"{rinc_5E_4_sum:,.0f}")
    rinc_5E_5_sum = st.number_input("R5E Jumlah Transfer Dibayarkan/Diberikan (Barang/Jasa)", min_value=0)
    st.success(f"{rinc_5E_5_sum:,.0f}")

    #Blok VF
    st.write("---")
    st.write("Blok VF TRANSFER MODAL / ASET SELAMA SETAHUN TERAKHIR")
    rinc_5F_2_sum = st.number_input("R5F Jumlah Transfer Diterima (Bangunan, Alat Produksi, Kendaraan, dll)", min_value=0)
    st.success(f"{rinc_5F_2_sum:,.0f}")
    rinc_5F_3_sum = st.number_input("R5F Jumlah Transfer Diterima (Lahan/Tanah dan Barang Berharga)", min_value=0)
    st.success(f"{rinc_5F_3_sum:,.0f}")
    rinc_5F_4_sum = st.number_input("R5F Jumlah Transfer Dibayarkan/Diberikan (Bangunan, Alat Produksi, Kendaraan, dll)", min_value=0)
    st.success(f"{rinc_5F_4_sum:,.0f}")
    rinc_5F_5_sum = st.number_input("R5F Jumlah Transfer Dibayarkan/Diberikan (Lahan/Tanah dan Barang Berharga)", min_value=0)
    st.success(f"{rinc_5F_5_sum:,.0f}")

    #Blok VG
    st.write("---")
    st.write("Blok VG PENAMBAHAN DAN PENGURANGAN ASET SELAMA SETAHUN TERAKHIR")
    rinc_5G_2_sum = st.number_input("R5G Jumlah Penambahan", min_value=0)
    st.success(f"{rinc_5G_2_sum:,.0f}")
    rinc_5G_3_sum = st.number_input("R5G Jumlah Pengurangan", min_value=0)
    st.success(f"{rinc_5G_3_sum:,.0f}")
    rinc_5G_4_sum = rinc_5G_2_sum + rinc_5G_3_sum
    st.metric(label="R5G Jumlah Neto", value=f"Rp. {rinc_5G_4_sum:,.0f}", border=True)

with tab5:
    #Blok VI
    st.subheader("Blok VI REKAPITULASI PENERIMAAN DAN PENGELUARAN RUMAH TANGGA SELAMA SETAHUN TERAKHIR")
    st.write("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Rincian Penerimaan")
        rinc_61_2 = rinc_5A_5_sum + rinc_5A_6_sum + rinc_5A_7_sum
        st.metric(label="1. Upah dan Gaji", value=f"Rp. {rinc_61_2:,.0f}", border=True)
        rinc_62_2 = rinc_5B_7_sum
        st.metric(label="2. Pendapatan/Surplus dari Usaha Rumah Tangga", value=f"Rp. {rinc_62_2:,.0f}", border=True)
        rinc_63_2 = rinc_5C_4_sum
        st.metric(label="3. Pendapatan/Surplus dari Produksi Rumah Tangga yang Dikonsumsi/Digunakan Sendiri", value=f"Rp. {rinc_63_2:,.0f}", border=True)
        rinc_64_2 = rinc_5D_2_sum
        st.metric(label="4. Pendapatan Kepemilikan yang Diterima", value=f"Rp. {rinc_64_2:,.0f}", border=True)
        rinc_65_2 = rinc_5E_2_sum + rinc_5E_3_sum
        st.metric(label="5. Transfer Berjalan (selain aset) Diterima", value=f"Rp. {rinc_65_2:,.0f}", border=True)
        rinc_66_2 = rinc_5F_2_sum + rinc_5F_3_sum
        st.metric(label="6. Transfer Modal/Aset Diterima", value=f"Rp. {rinc_66_2:,.0f}", border=True)
        jumlah_6_2 = rinc_61_2 + rinc_62_2 + rinc_63_2 + rinc_64_2 + rinc_65_2 + rinc_66_2
        st.metric(label="Jumlah Penerimaan (Kolom 2)", value=f"Rp. {jumlah_6_2:,.0f}", border=True)
    
    with col2:
        st.subheader("Rincian Pengeluaran")
        rinc_61_4 = rinc_433_9 * 12
        st.metric(label="1. Pengeluaran Konsumsi Rumah Tangga", value=f"Rp. {rinc_61_4:,.0f}", border=True)
        rinc_62_4 = rinc_5D_3_sum
        st.metric(label="2. Pendapatan Kepemilikan yang Dibayar", value=f"Rp. {rinc_62_4:,.0f}", border=True)
        rinc_63_4 = rinc_5E_4_sum + rinc_5E_5_sum
        st.metric(label="3. Transfer Berjalan (selain Aset) Dibayar", value=f"Rp. {rinc_63_4:,.0f}", border=True)
        rinc_64_4 = rinc_5F_4_sum + rinc_5F_5_sum
        st.metric(label="4. Transfer Modal/Aset Dibayar", value=f"Rp. {rinc_64_4:,.0f}", border=True)
        rinc_65_4 = rinc_5G_4_sum
        st.metric(label="5. Total Aset Neto", value=f"Rp. {rinc_65_4:,.0f}", border=True)
        jumlah_6_4 = rinc_61_4 + rinc_62_4 + rinc_63_4 + rinc_64_4 + rinc_65_4
        st.metric(label="Jumlah Pengeluaran (Kolom 4)", value=f"Rp. {jumlah_6_4:,.0f}", border=True)

    #Selisih Penerimaan dan Pengeluaran
    selisih_terima_keluar = jumlah_6_2 - jumlah_6_4
    st.metric(label="Selisih Penerimaan dan Pengeluaran", value=f"Rp. {selisih_terima_keluar:,.0f}", border=True)

with tab6:
    st.write("Blok VII TRANSAKSI KEUANGAN RUMAH TANGGA SELAMA SETAHUN TERAKHIR")

"""