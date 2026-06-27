import streamlit as st
import time

# SAYFA AYARLARI
st.set_page_config(page_title="SÜPERZEKA v20 PRO", layout="wide")

# CSS: SİBER KARANLIK TEMA
st.markdown("""
    <style>
    .stApp, [data-testid="stSidebar"] { background-color: #050505 !important; }
    h1, h2, b, p, label { color: #00ffcc !important; font-family: 'Consolas', monospace !important; }
    .chat-box { border: 1px dashed #00ffcc; padding: 15px; margin: 10px 0; background: #0c0c0c; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

if "gecmis" not in st.session_state: st.session_state.gecmis = []

# SIDEBAR
st.sidebar.title("🔐 SİBER ÜS")
sifre = st.sidebar.text_input("Şifre (Şu anki dakika):", type="password")

# ÖĞRETMEN Mİ ÖĞRENCİ Mİ?
if sifre == time.strftime("%M"):
    mod = "ÖĞRETMEN"
    st.sidebar.success("YETKİLİ: ÖĞRETMEN")
else:
    mod = "ÖĞRENCİ"
    st.sidebar.info("MOD: ÖĞRENCİ")

# ANA EKRAN
st.title("🧠 SÜPERZEKA v20 PRO")

# BİLGİ VE HADİS
col1, col2 = st.columns(2)
col1.info("🌟 Günün Bilgisi: Işık hızı saniyede yaklaşık 300.000 km'dir.")
col2.info("🕋 Hadis: 'İlim Çin'de bile olsa gidip alınız.'")

# SOHBET MANTIĞI (DÜZELTİLMİŞ)
girdi = st.text_input("Bir şeyler yaz:")
if girdi:
    # 1. Selamlaşma kontrolü
    if any(kelime in girdi.lower() for kelime in ["selam", "merhaba", "hi"]):
        cevap = "Merhaba! SüperZeka v20 Pro hizmetinde."
    # 2. Matematik kontrolü
    elif any(islem in girdi for islem in ["+", "-", "*", "/"]):
        cevap = "Matematiksel işlem tespit edildi! " + ("Sonuç: " + str(eval(girdi)) if mod=="ÖĞRETMEN" else "Bu işlemi nasıl yapacağını biliyorsun, bir düşün!")
    # 3. Genel
    else:
        cevap = "Harika bir soru! " + ("Şöyle ki: [DETAYLI ANLATIM]" if mod=="ÖĞRETMEN" else "İşte sana bir ipucu...")
    
    st.session_state.gecmis.append((girdi, cevap))

# EKRANA BAS
for q, a in reversed(st.session_state.gecmis):
    st.markdown(f"<div class='chat-box'>👤 {q}<br>🤖 {a}</div>", unsafe_allow_html=True)
