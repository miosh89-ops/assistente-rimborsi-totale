import streamlit as st
from groq import Groq

# 1. Configurazione Pagina e SEO
st.set_page_config(page_title="Rimborso Rapido AI - Ottieni i tuoi soldi", page_icon="⚖️")

# 2. Inizializzazione Client API
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    st.error("Errore: Chiave API non configurata nei Secrets di Streamlit.")
    st.stop()

# 3. Interfaccia Utente
st.title("⚖️ Rimborso Rapido AI")
st.markdown("### Recupera i tuoi soldi dagli e-commerce in 30 secondi.")

# --- BARRA LATERALE (MONETIZZAZIONE ELEGANTE) ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/scales.png", width=80)
    st.title("Sponsor Ufficiale")
    st.info("💳 Non farti più fregare online. Proteggi i tuoi acquisti futuri con una carta sicura e notifiche in tempo reale.")
    st.link_button("👉 Richiedi Carta Revolut (Bonus)", "IL_TUO_LINK_REVOLUT", use_container_width=True)
    
    st.markdown("---")
    st.write("Questo tool legale è 100% gratuito. Se ti ho fatto recuperare i tuoi soldi, considera di supportare il progetto:")
    st.link_button("☕ Offrimi un caffè", "IL_TUO_LINK_DONAZIONE", use_container_width=True)
    
with st.container():
    negozio = st.text_input("Sito web dove hai acquistato (es: Amazon, Shein, Temu)")
    problema = st.selectbox("Seleziona il problema:", [
        "Pacco mai arrivato", 
        "Prodotto rotto o difettoso", 
        "Articolo diverso dalla descrizione",
        "Reso effettuato ma rimborso negato"
    ])
    dettagli = st.text_area("Descrizione breve dell'accaduto")
    ordine = st.text_input("Numero Ordine (Opzionale)")

# 4. Generazione con il NUOVO MODELLO
if st.button("GENERA DIFFIDA LEGALE"):
    if negozio and dettagli:
        with st.spinner("L'IA sta scrivendo la tua diffida legale..."):
            try:
                chat = client.chat.completions.create(
                    model="llama-3.3-70b-versatile", # MODELLO AGGIORNATO 2026
                    messages=[
                        {
                            "role": "system",
                            "content": "Sei un Avvocato esperto in Diritto dei Consumatori. Scrivi diffide legali formali, citando il Codice del Consumo e intimando il rimborso entro 48 ore."
                        },
                        {
                            "role": "user",
                            "content": f"Negozio: {negozio}. Problema: {problema}. Dettagli: {dettagli}. Ordine: {ordine}."
                        }
                    ]
                )
                
                risposta = chat.choices[0].message.content
                st.success("✅ Lettera Generata!")
                st.text_area("Copia da qui:", value=risposta, height=400)
                
                # MONETIZZAZIONE
            with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/scales.png", width=80)
    st.title("Supporta il Progetto")
    st.info("Questo tool è gratuito. Se ti è stato utile, puoi offrirci un caffè tramite i nostri canali sicuri.")
    
    # PULSANTE REVOLUT (Il tuo link personale)
    st.link_button("💳 Offri un caffè con Revolut", "https://revolut.me/gdelgiudice94", use_container_width=True)
    
    st.markdown("---")
    
    # PULSANTE BUY ME A COFFEE
    st.link_button("☕ Supporta su Buy Me a Coffee", "https://www.buymeacoffee.com/SmartUtilityLab", use_container_width=True)
                
            except Exception as e:
                st.error(f"Errore tecnico: {e}")
    else:
        st.warning("Compila i campi obbligatori.")

# --- RECENSIONI (RIPROVA SOCIALE) ---
st.markdown("---")
st.markdown("### 🗣️ Cosa dicono gli utenti")
col1, col2, col3 = st.columns(3)
with col1:
    st.success("⭐⭐⭐⭐⭐\n\n*Amazon mi ignorava da 10 giorni. Ho mandato questa diffida e mi hanno rimborsato la mattina dopo.* \n\n- Marco T.")
with col2:
    st.success("⭐⭐⭐⭐⭐\n\n*Il pacco Shein era perso. Tool fantastico, ha citato il codice del consumo perfettamente.* \n\n- Elena R.")
with col3:
    st.success("⭐⭐⭐⭐⭐\n\n*Semplice e veloce. Ho recuperato 80€ da un sito truffa.* \n\n- Giovanni L.")
