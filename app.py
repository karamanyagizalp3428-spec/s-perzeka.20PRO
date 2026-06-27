import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title="SÜPERZEKA PRO v20", layout="wide")

# CSS: SİBER TEMA
st.markdown("""<style>
    .stApp { background-color: #050505 !important; }
    h1, h2, b, p, label { color: #00ffcc !important; }
    .chat-box { border: 1px dashed #00ffcc; padding: 15px; background: #0c0c0c; border-radius: 10px; }
    .info-box { border: 1px solid #00ffcc; padding: 10px; background: #111; color: #fff; }
</style>""", unsafe_allow_html=True)

# 1. SIDEBAR (YAPIMCI TABLOSU)
st.sidebar.title("🛠️ SİBER ÜS")
yapimci_tablo = pd.DataFrame({"Özellik": ["Geliştirici", "Versiyon"], "Bilgi": ["SüperZeka", "v20.0"]})
st.sidebar.table(yapimci_tablo)

# 2. GİRİŞ VE MOD
sifre = st.sidebar.text_input("Giriş:", type="password")
mod = "ÖĞRETMEN" if sifre == time.strftime("%M") else "ÖĞRENCİ"

# 3. PANORAMA: POMODORO, BİLGİ VE HADİS
st.title("🧠 SÜPERZEKA PRO v20")
col1, col2, col3 = st.columns(3)
col1.metric("⏱️ Pomodoro", "25:00")
col2.markdown("<div class='info-box'>🌟 <b>Günün Bilgisi:</b> Arılar, dünyanın en çalışkan canlılarıdır!</div>", unsafe_allow_html=True)
col3.markdown("<div class='info-box'>🕋 <b>Hadis-i Şerif:</b> 'İlim öğrenmek her Müslümana farzdır.'</div>", unsafe_allow_html=True)

# 4. SORU SORMA
st.markdown("---")
girdi = st.text_input("Soru sor:")
if girdi:
    cevap = "Analiz ediliyor..."
    st.session_state.setdefault("gecmis", []).append((girdi, cevap))
    st.success("Soru buluta gönderildi!")

# 5. GEÇMİŞ
for q, a in reversed(st.session_state.get("gecmis", [])):
    st.markdown(f"<div class='chat-box'>👤 {q}<br>🤖 {a}</div>", unsafe_allow_html=True)
