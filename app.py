import streamlit as st
import time

st.set_page_config(page_title="SÜPERZEKA PRO", layout="wide")

# CSS: SİBER TEMA
st.markdown("""<style>
    .stApp { background-color: #050505 !important; }
    h1, b, p { color: #00ffcc !important; }
    .chat-box { border: 1px dashed #00ffcc; padding: 10px; background: #0c0c0c; }
</style>""", unsafe_allow_html=True)

# GÜVENLİK SİSTEMİ
if "hata_sayisi" not in st.session_state: st.session_state.hata_sayisi = 0

st.sidebar.title("🔐 GÜVENLİK")
sifre = st.sidebar.text_input("Şifre (Dakika):", type="password")

if sifre:
    if sifre == time.strftime("%M"):
        st.sidebar.success("Giriş Başarılı!")
        st.session_state.hata_sayisi = 0
    else:
        st.session_state.hata_sayisi += 1
        st.sidebar.error(f"Hatalı Şifre! {st.session_state.hata_sayisi}/3")

# 3 HATA OLURSA FOTOĞRAF GÖSTER
if st.session_state.hata_sayisi >= 3:
    st.warning("⚠️ Güvenlik ihlali! Sisteme girişin geçici olarak kısıtlandı.")
     # İşte 3 hata sonrası güvenlik şeması
else:
    st.title("🧠 SÜPERZEKA PRO")
    st.write("Sistem aktif. Şifreni gir ve devam et.")
