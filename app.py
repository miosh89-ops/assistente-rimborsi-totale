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
                st.markdown("---")
                st.subheader("🛡️ Proteggi i tuoi prossimi acquisti")
                st.link_button("🔥 Attiva Revolut e ricevi il Bonus sicurezza", "IL_TUO_LINK_REVOLUT")
                st.markdown("---")
                st.link_button("☕ Offrimi un caffè (Donazione)", "IL_TUO_LINK_DONAZIONE")
                
            except Exception as e:
                st.error(f"Errore tecnico: {e}")
    else:
        st.warning("Compila i campi obbligatori.")
