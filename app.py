import streamlit as st
from groq import Groq

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="SmartUtility Lab - Tutela Consumatori", 
    page_icon="⚖️",
    layout="wide"
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

# 4. LOGICA DI GENERAZIONE CON IA (IL "CERVELLO")
if st.button("GENERA DIFFIDA LEGALE CON AI", type="primary", use_container_width=True):
    if not sito or not dettagli:
        st.error("Per favore, inserisci almeno il nome del sito e i dettagli!")
    else:
        with st.spinner('L\'Intelligenza Artificiale sta scrivendo una diffida legale formale...'):
            try:
                # Prompt personalizzato per l'IA
                prompt = f"""
                Sei un avvocato esperto in diritto del consumo in Italia. 
                Scrivi una lettera di diffida formale e minacciosa per un cliente che ha avuto un problema con {sito}.
                Dettagli del problema: {problema}. 
                Dettagli aggiuntivi: {dettagli}. 
                Numero ordine: {ordine if ordine else 'Non specificato'}.
                
                Nella lettera devi assolutamente:
                1. Citare il Codice del Consumo (D. Lgs. 206/2005), in particolare gli articoli 61 e 66.
                2. Intimare il rimborso entro 48 ore.
                3. Minacciare di ricorrere alle autorità (AGCM) e adire le vie legali.
                4. Usare un tono formale, freddo e professionale.
                """

                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-specdec", # Il modello più potente
                )
                
                diffida_ai = chat_completion.choices[0].message.content
                
                st.success("✅ Diffida Legale generata dall'IA!")
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
    st.success("⭐⭐⭐⭐⭐\n\n*Incredibile. Ho copiato il testo dell'IA e Amazon mi ha rimborsato in 2 ore.* \n\n- Marco T.")
with t2:
    st.success("⭐⭐⭐⭐⭐\n\n*La diffida citava leggi che nemmeno conoscevo. Molto professionale.* \n\n- Elena R.")
with t3:
    st.success("⭐⭐⭐⭐⭐\n\n*Gratis e veloce. Meglio di spendere 200€ di avvocato.* \n\n- Giovanni L.")
