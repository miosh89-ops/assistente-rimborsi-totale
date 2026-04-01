import streamlit as st
from groq import Groq

# --- VERIFICA GOOGLE SEARCH CONSOLE ---
st.html('<meta name="google-site-verification" content="FEPUjwHJUUHDgYUqDVK0RoATqLWwq8dcOYgUkcYBZFM" />')

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="SmartUtility Lab - Generatore Diffide IA",
    page_icon="⚖️",
    menu_items={
        'Get Help': 'https://revolut.me/gdelgiudice94',
        'About': "# SmartUtility Lab\nTool AI gratuito per rimborsi e tutela consumatori."
    }
)

# Recupero API Key dai Secrets di Streamlit
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

# 2. BARRA LATERALE (BRAND E MONETIZZAZIONE)
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/scales.png", width=80)
    st.title("SmartUtility Lab")
    st.markdown("---")
    st.info("""
    **Sostieni il progetto**
    Sviluppiamo strumenti AI gratuiti per i cittadini. Se il tool ti è utile, offrici un caffè per coprire i costi dei server.
    """)
    
    # Link Reali
    st.link_button("💳 Caffè rapido (Revolut)", "https://revolut.me/gdelgiudice94", use_container_width=True)
    st.link_button("☕ Supporta su Buy Me a Coffee", "https://www.buymeacoffee.com/SmartUtilityLab", use_container_width=True)
    
    st.markdown("---")
    st.caption("© 2026 SmartUtility Lab - Tutela Digitale")

# 3. CORPO PRINCIPALE (UI)
st.title("⚖️ SmartUtility Lab: Generatore Diffide")
st.markdown("### Recupera i tuoi soldi dagli e-commerce in 30 secondi con l'IA.")

col_a, col_b = st.columns(2)

with col_a:
    sito = st.text_input("Sito web (es: Amazon, Shein, Temu)", placeholder="www.amazon.it")
    ordine = st.text_input("Numero Ordine (Opzionale)", placeholder="236475")

with col_b:
    problema = st.selectbox("Seleziona il problema:", [
        "Pacco mai arrivato", 
        "Pacco arrivato vuoto/manomesso", 
        "Rimborso non ricevuto dopo reso",
        "Prodotto non conforme/difettoso"
    ])

dettagli = st.text_area("Descrizione breve dell'accaduto", placeholder="Esempio: Il pacco risulta consegnato ma non ho ricevuto nulla.")

# 4. LOGICA DI GENERAZIONE CON IA
if st.button("GENERA DIFFIDA LEGALE CON AI", type="primary", use_container_width=True):
    if not sito or not dettagli:
        st.error("Per favore, inserisci almeno il nome del sito e i dettagli!")
    else:
        with st.spinner('L\'Intelligenza Artificiale sta scrivendo una diffida legale formale...'):
            try:
                prompt = f"""
                Agisci come un cittadino italiano esperto dei propri diritti che scrive una diffida formale in PRIMA PERSONA (usa "Io", "Mio").
                NON scrivere come un avvocato che difende un cliente. Scrivi come il cliente stesso.

                Dati del problema:
                - Sito: {sito}
                - Ordine n.: {ordine if ordine else 'Non specificato'}
                - Problema riscontrato: {problema}
                - Cosa è successo: {dettagli}

                Struttura della lettera:
                1. Intestazione formale (Mittente e Destinatario).
                2. Oggetto chiaro: Diffida formale e costituzione in mora.
                3. Corpo: Spiega che hai pagato e non hai ricevuto il servizio/bene (o il rimborso).
                4. Citazione Legale: Cita il Codice del Consumo (D. Lgs. 206/2005) e l'obbligo di rimborso.
                5. Ultimatum: Intima il rimborso entro 48 ore.
                6. Minaccia: Scrivi che in mancanza di rimborso segnalerai l'azienda all'AGCM (Antitrust) e caricherai la pratica su portali di risoluzione controversie.

                Usa un tono fermo, deluso ma risoluto. Non usare termini troppo complessi, deve sembrare scritta da una persona reale che rivuole i suoi soldi.
                """

                # Assicurati che il modello sia quello corretto
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile", 
                )
                
                diffida_ai = chat_completion.choices[0].message.content
                
                st.success("✅ Diffida Legale generata con successo!")
                st.text_area("Copia e invia via Mail o PEC:", value=diffida_ai, height=450)
                
                # --- MONETIZZAZIONE DOPO GENERAZIONE ---
                st.markdown("---")
                st.subheader("💡 Ti ho aiutato a risolvere?")
                st.write("Speriamo che questa diffida ti aiuti a sbloccare il rimborso. Se vuoi ringraziarci:")
                
                c1, c2 = st.columns(2)
                with c1:
                    st.link_button("☕ Caffè rapido (Revolut)", "https://revolut.me/gdelgiudice94", use_container_width=True)
                with c2:
                    st.link_button("⭐ Supporta SmartUtility Lab", "https://www.buymeacoffee.com/SmartUtilityLab", use_container_width=True)

            except Exception as e:
                st.error(f"Errore nella generazione: {e}")

# 5. RIPROVA SOCIALE
st.markdown("---")
st.markdown("### 🗣️ Recensioni Recenti")
t1, t2, t3 = st.columns(3)
with t1:
    st.success("⭐⭐⭐⭐⭐\n\n*Amazon mi ignorava. Ho mandato questa diffida e mi hanno rimborsato subito.* \n\n- Marco T.")
with t2:
    st.success("⭐⭐⭐⭐⭐\n\n*La diffida citava leggi che nemmeno conoscevo. Molto professionale.* \n\n- Elena R.")
with t3:
    st.success("⭐⭐⭐⭐⭐\n\n*Gratis e veloce. Meglio di spendere 200€ di avvocato.* \n\n- Giovanni L.")
