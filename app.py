import streamlit as st
from groq import Groq

# 1. Configurazione Pagina e SEO
st.set_page_config(page_title="Rimborso Rapido AI - Ottieni i tuoi soldi", page_icon="⚖️")

# 2. Inizializzazione Client API in modo sicuro
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except KeyError:
    st.error("Errore di configurazione: Chiave API Groq non trovata nei secrets. Controlla le impostazioni su Streamlit Cloud.")
    st.stop()

# 3. Interfaccia Utente Principale
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
    dettagli = st.text_area("Descrizione breve dell'accaduto (sii chiaro e conciso)")
    ordine = st.text_input("Numero Ordine (Opzionale ma consigliato)")

# 4. Motore IA e Generazione
if st.button("GENERA DIFFIDA LEGALE"):
    if negozio and dettagli:
        with st.spinner("L'IA sta elaborando la tua diffida legale, attendi..."):
            try:
                # Chiamata API ottimizzata per Llama3 su Groq
                chat = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[
                        {
                            "role": "system",
                            "content": "Sei un Avvocato specializzato in tutela del consumatore e-commerce. Il tuo compito è scrivere una formale lettera di messa in mora. Usa un tono imperativo e legale. Cita il Decreto Legislativo 206/2005 (Codice del Consumo) italiano. Intima il rimborso entro 48 ore minacciando la segnalazione all'AGCM (Antitrust)."
                        },
                        {
                            "role": "user",
                            "content": f"Scrivi un reclamo per il negozio {negozio}. Problema riscontrato: {problema}. Numero ordine: {ordine}. Fatti specifici: {dettagli}."
                        }
                    ],
                    temperature=0.7, # Bilancia precisione legale e naturalezza del testo
                )
                
                risposta = chat.choices[0].message.content
                
                # 5. Risultato e Monetizzazione
                st.success("✅ Lettera Generata con Successo! Copiala e inviala via mail o PEC al negozio.")
                st.text_area("Testo della diffida pronto all'uso:", value=risposta, height=400)
                
                st.markdown("---")
                st.subheader("🛡️ Proteggi i tuoi prossimi acquisti")
                st.write("Per evitare ritardi e truffe, usa una carta con protezione acquisti integrata e notifiche in tempo reale.")
                
                # Sostituisci questo link con il tuo referral Revolut
                st.link_button("🔥 Attiva Revolut e ricevi il Bonus sicurezza", "INCOLLA_QUI_IL_TUO_LINK_REVOLUT")
                
                st.markdown("---")
                st.write("Ti ho aiutato a recuperare i tuoi soldi? Se ti va, offrimi un caffè per sostenere il sito!")
                
                # Sostituisci questo link con il tuo BuyMeACoffee
                st.link_button("☕ Offrimi un caffè (Donazione)", "INCOLLA_QUI_IL_TUO_LINK_BUYMEACOFFEE")
                
            except Exception as e:
                st.error(f"Si è verificato un errore di comunicazione con il server: {e}")
    else:
        st.warning("⚠️ Compila almeno il nome del negozio e la descrizione dell'accaduto per procedere.")
