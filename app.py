import streamlit as st

dashboard = st.Page("fitur/dashboard.py", title="dashboard")
nabung = st.Page("fitur/nabung.py", title="menabung")

pg = st.navigation(
    {
        "menu utama" : [dashboard],
        "Transaksi" : [nabung],

    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()

