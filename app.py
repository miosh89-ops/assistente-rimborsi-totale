import streamlit as st
from groq import Groq

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="SmartUtility Lab - Generatore Diffide IA",
    page_icon="⚖️",
    layout="centered", # Torniamo al layout centrato come concordato
    menu_items={
        'Get Help': 'https://revolut.me/gdelgiudice94',
        'About': "# SmartUtility Lab\nTool AI gratuito per rimborsi e tutela consumatori."
    }
)

# --- CSS PERSONALIZZATO PER MIGLIORARE IL LOOK ---
st.markdown("""
    <style>
    /* Cambia il colore del tasto principale */
    div.stButton > button:first-child {
        background-color: #004a99;
        color: white;
        border-radius: 10px;
        border: none;
        height: 3em;
        font-weight: bold;
        transition: all 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #003366;
        border: none;
        transform: scale(1.02);
    }
    /* Arrotonda i box delle recensioni */
    .stAlert {
        border-radius: 15px;
    }
    /* Stile per il titolo */
    h1 {
        color: #1E1E1E;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Recupero API Key dai Secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

# 2. BARRA LATERALE
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/scales.png", width=80)
    st.title("SmartUtility Lab")
    st.markdown("---")
    st.info("**Sostieni il progetto**\nSviluppiamo strumenti AI gratuiti. Se il tool ti è utile, offrici un caffè!")
    st.link_button("💳 Caffè rapido (Revolut)", "https://revolut.me/gdelgiudice94", use_container_width=True)
    st.link_button("☕ Supporta su Buy Me a Coffee", "https://www.buymeacoffee.com/SmartUtilityLab", use_container_width=True)
    st.markdown("---")
    st.caption("© 2026 SmartUtility Lab")

# 3. CORPO PRINCIPALE
st.title("⚖️ SmartUtility Lab: Generatore Diffide")
st.markdown("##### Recupera i tuoi soldi dagli e-commerce in 30 secondi con l'IA.")

# Box informativo e tasti donazione subito visibili (soprattutto su mobile)
with st.container():
    st.success("💡 **Strumento 100% Gratuito.** Se risparmi tempo o denaro, considera una piccola donazione!")
    c_top1, c_top2 = st.columns(2)
    with c_top1:
        st.link_button("☕ Offrimi un Caffè (Revolut)", "https://revolut.me/gdelgiudice94", use_container_width=True)
    with c_top2:
        st.link_button("⭐ Supporta il Progetto", "https://www.buymeacoffee.com/SmartUtilityLab", use_container_width=True)

st.markdown("---")

# INPUT UTENTE
col_a, col_b = st.columns(2)
with col_a:
    sito = st.text_input("Sito web", placeholder="Esempio: Amazon, Shein, Temu")
    ordine = st.text_input("Numero Ordine (Opzionale)", placeholder="es: 403-1234567")
with col_b:
    problema = st.selectbox("Seleziona il problema:", [
        "Pacco mai arrivato", 
        "Pacco arrivato vuoto/manomesso", 
        "Rimborso non ricevuto dopo reso",
        "Prodotto non conforme/difettoso"
    ])

dettagli = st.text_area("Cosa è successo? (Sii breve)", placeholder="Esempio: Il tracking dice consegnato ma non ho ricevuto nulla.")

# GENERAZIONE
if st.button("🚀 GENERA DIFFIDA ORA", use_container_width=True):
    if not sito or not dettagli:
        st.error("Inserisci il nome del sito e i dettagli!")
    else:
        with st.spinner('L\'IA sta scrivendo...'):
            try:
                prompt = f"""
                Agisci come un cittadino italiano esperto dei propri diritti. Scrivi una diffida formale in PRIMA PERSONA.
                Dati: Sito {sito}, Ordine {ordine}, Problema {problema}, Dettagli {dettagli}.
                Includi: Mittente, Destinatario, Oggetto, Codice del Consumo (D. Lgs. 206/2005), termine 48h, minaccia AGCM.
                Tono: Fermo e risoluto.
                """
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile", 
                )
                diffida_ai = chat_completion.choices[0].message.content
                
                st.success("✅ Diffida Pronta!")
                st.text_area("Copia il testo qui sotto:", value=diffida_ai, height=400)
                
                # Tasti post-generazione
                st.info("🎯 **Ti abbiamo fatto risparmiare tempo e stress?** Offrici un caffè per ringraziarci!")
                st.link_button("☕ Invia un Caffè (Revolut)", "https://revolut.me/gdelgiudice94", use_container_width=True)
            except Exception as e:
                st.error(f"Errore: {e}")

# RECENSIONI
st.markdown("---")
st.subheader("🗣️ Cosa dicono gli utenti")
t1, t2, t3 = st.columns(3)
with t1:
    st.info("⭐⭐⭐⭐⭐\n\n*Rimborsato in 24h dopo aver inviato questo testo ad Amazon!*")
with t2:
    st.info("⭐⭐⭐⭐⭐\n\n*Facilissimo da usare, professionale e gratuito.*")
with t3:
    st.info("⭐⭐⭐⭐⭐\n\n*Un risparmio di tempo incredibile. Consigliatissimo!*")

st.markdown("---")
st.caption("⚠️ **Disclaimer:** Questo tool utilizza l'IA e non sostituisce un parere legale ufficiale.")
