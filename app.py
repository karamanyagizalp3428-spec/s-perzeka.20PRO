import streamlit as st
import google.generativeai as genai
import time
import pandas as pd

# GEMINI AYARLARI
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="SÜPERZEKA PRO v20", layout="wide")

# CSS: SİBER TEMA
st.markdown("""<style>
    .stApp { background-color: #050505 !important; }
    h1, h2, b, p, label { color: #00ffcc !important; }
    .chat-box { border: 1px dashed #00ffcc; padding: 15px; background: #0c0c0c; border-radius: 10px; }
    .info-box { border: 1px solid #00ffcc; padding: 10px; background: #111; color: #fff; }
</style>""", unsafe_allow_html=True)

# SIDEBAR (SENİN İMZANLA)
st.sidebar.title("🛠️ SİBER ÜS")
yapimci_tablo = pd.DataFrame({"Özellik": ["Geliştirici", "Versiyon"], "Bilgi": ["Yağızalp", "v20.0"]})
st.sidebar.table(yapimci_tablo)

# GİRİŞ VE MOD
sifre = st.sidebar.text_input("Giriş:", type="password")
mod = "ÖĞRETMEN" if sifre == time.strftime("%M") else "ÖĞRENCİ"

# PANORAMA
st.title("🧠 SÜPERZEKA PRO v20")
col1, col2, col3 = st.columns(3)
col1.metric("⏱️ Pomodoro", "25:00")
col2.markdown("<div class='info-box'>🌟 <b>Günün Bilgisi:</b> Gemini modelleri çok geniş bir veri havuzuna sahiptir.</div>", unsafe_allow_html=True)
col3.markdown("<div class='info-box'>🕋 <b>Hadis-i Şerif:</b> 'İlim öğrenmek farzdır.'</div>", unsafe_allow_html=True)

# SORU SORMA (GEMINI DESTEKLİ)
st.markdown("---")
girdi = st.text_input("Soru sor:")
if girdi:
    cevap = model.generate_content(girdi).text
    st.session_state.setdefault("gecmis", []).append((girdi, cevap))

# GEÇMİŞ
for q, a in reversed(st.session_state.get("gecmis", [])):
    st.markdown(f"<div class='chat-box'>👤 {q}<br>🤖 {a}</div>", unsafe_allow_html=True)
