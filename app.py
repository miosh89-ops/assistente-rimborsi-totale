import streamlit as st
from groq import Groq

# Configurazione Tecnica
st.set_page_config(page_title="Rimborso Rapido AI - Ottieni i tuoi soldi", page_icon="⚖️")
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Interfaccia Utente
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

if st.button("GENERA DIFFIDA LEGALE"):
    if negozio and dettagli:
        # PROMPT PROFESSIONALE OTTIMIZZATO
        prompt = f"""
        Agisci come un Avvocato specializzato in tutela del consumatore e-commerce. 
        Scrivi una lettera di messa in mora formale indirizzata a {negozio}.
        Oggetto del reclamo: {problema}.
        Numero ordine: {ordine}.
        Fatti: {dettagli}.
        REGOLE:
        1. Usa un tono imperativo e legale.
        2. Cita il Decreto Legislativo 206/2005 (Codice del Consumo).
        3. Intima il rimborso entro 48 ore.
        4. Minaccia la segnalazione immediata all'AGCM (Antitrust) e al Centro Europeo Consumatori.
        """
        
        chat = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        
        risposta = chat.choices[0].message.content
        st.success("✅ Lettera Generata con Successo!")
        st.text_area("Copia il testo qui sotto:", value=risposta, height=400)
        
        # MONETIZZAZIONE
        st.markdown("---")
        st.error("⚠️ **IMPORTANTE:** Per evitare questi problemi in futuro, usa una carta con protezione acquisti.")
        st.markdown("[👉 CLICCA QUI: Attiva la protezione acquisti e ricevi un bonus (Partner Sicuro)](TUO_LINK_AFFILIATO)")
        st.markdown("[☕ Offrimi un caffè per aver recuperato i tuoi soldi](TUO_LINK_DONAZIONE)")
    else:
        st.error("Compila tutti i campi richiesti.")
