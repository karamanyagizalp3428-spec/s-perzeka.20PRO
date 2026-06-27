import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="SÜPERZEKA PRO", layout="wide")

# Tasarım: Karanlık ve siber tema
st.markdown("""
    <style>
    .stApp { background-color: #050505 !important; }
    h1, b, p { color: #00ffcc !important; font-family: sans-serif !important; }
    .chat-box { border: 1px dashed #00ffcc; padding: 15px; margin: 10px 0; background: #0c0c0c; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# Hafıza sistemi
if "mod" not in st.session_state: st.session_state.mod = "ÖĞRENCİ"
if "gecmis" not in st.session_state: st.session_state.gecmis = []

# Sidebar (Sol menü)
st.sidebar.title("🔐 SİBER ÜS")
mod_secim = st.sidebar.radio("Mod Seçimi:", ["ÖĞRENCİ", "ÖĞRETMEN"])

if mod_secim == "ÖĞRETMEN":
    sifre = st.sidebar.text_input("Şifre gir:", type="password")
    if sifre == "123": # Basit şifre sistemi
        st.session_state.mod = "ÖĞRETMEN"
        st.sidebar.success("YETKİLİ GİRİŞİ BAŞARILI!")
    else:
        st.sidebar.error("Yetkisiz Erişim!")
        st.session_state.mod = "ÖĞRENCİ"
else:
    st.session_state.mod = "ÖĞRENCİ"

# Ana ekran
st.title("🧠 SÜPERZEKA PRO")
st.write(f"Aktif Yetki: **{st.session_state.mod}**")

# Sorgu kutusu
girdi = st.text_input("Komut gir ve Enter'a bas:")
if girdi:
    cevap = "Detaylı açıklama yapılıyor..." if st.session_state.mod == "ÖĞRETMEN" else "İpucu veriliyor..."
    st.session_state.gecmis.append((girdi, cevap))

# Geçmişi göster
for q, a in reversed(st.session_state.gecmis):
    st.markdown(f"<div class='chat-box'>👤 {q}<br>🤖 {a}</div>", unsafe_allow_html=True)
