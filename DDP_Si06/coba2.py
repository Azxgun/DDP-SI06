import streamlit as st

# Judul aplikasi
st.title("ATM Virtual")
#not in = jika tidak 0      

# Variabel saldo awal
if "uang_saya" not in st.session_state:
    st.session_state.uang_saya = 0

# Menu utama
st.sidebar.title("Menu")
option = st.sidebar.radio("Pilih opsi transaksi:", ["Cek Uang Saya", "Ambil Uang Saya", "Tabung Uang Saya"])

# Fungsi untuk cek saldo
def cek_uang():
    st.subheader("Cek Uang Saya")
    st.write(f"Saldo Anda saat ini: Rp {st.session_state.uang_saya}")

# Fungsi untuk ambil uang
def ambil_uang():
    st.subheader("Ambil Uang Saya")
    st.write(f"Saldo Anda saat ini: Rp {st.session_state.uang_saya}")
    jumlah_ambil = st.number_input("Masukkan jumlah uang yang ingin diambil:", min_value=0, step=1)
    
    if st.button("Ambil Uang"):
        if st.session_state.uang_saya - jumlah_ambil < 0:
            st.error("Saldo tidak mencukupi!")
        else:
            st.session_state.uang_saya -= jumlah_ambil
            st.success(f"Berhasil mengambil uang sebesar Rp {jumlah_ambil}")
            st.write(f"Saldo Anda sekarang: Rp {st.session_state.uang_saya}")

# Fungsi untuk tabung uang
def tabung_uang():
    st.subheader("Tabung Uang Saya")
    st.write(f"Saldo Anda saat ini: Rp {st.session_state.uang_saya}")
    jumlah_tabung = st.number_input("Masukkan jumlah uang yang ingin ditabung:", min_value=0, step=1)
    
    if st.button("Tabung Uang"):
        st.session_state.uang_saya += jumlah_tabung
        st.success(f"Berhasil menabung uang sebesar Rp {jumlah_tabung}")
        st.write(f"Saldo Anda sekarang: Rp {st.session_state.uang_saya}")

# Pilih menu berdasarkan opsi yang dipilih
if option == "Cek Uang Saya":
    cek_uang()
elif option == "Ambil Uang Saya":
    ambil_uang()
elif option == "Tabung Uang Saya":
    tabung_uang()

# Footer
# untuk memisah kan antara body dan footer
st.sidebar.write("---")
st.sidebar.write("Terima kasih telah menggunakan ATM Virtual!")
