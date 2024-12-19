import streamlit as st

st.title("Halaman nabung")

#folmulir input
with st.form("menabung"):
    nama = st.text_input("nama")
    jumlah = st.number_input("jumlah(Rp.)", min_value=0)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("waktu")
    submit_button = st.form_submit_button(label="menabung") 

    if submit_button and jumlah >= 50000:
        st.session_state['total_semua']. append({
            'tipe' : 'menabung',
            'jumlah' : jumlah
        })
        st.success("menabung berhasil")
    else:
        st.error("menabung gagal")
