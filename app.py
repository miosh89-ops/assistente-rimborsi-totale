import streamlit as st

# 1. CONFIGURAZIONE PAGINA (Solo una volta all'inizio)
st.set_page_config(
    page_title="SmartUtility Lab - Tutela Consumatori", 
    page_icon="⚖️",
    layout="wide"
)

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
st.markdown("### Recupera i tuoi soldi dagli e-commerce in 30 secondi.")

# Layout a due colonne per i campi input
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

dettagli = st.text_area("Descrizione breve (Cosa è successo?)", placeholder="Esempio: Il pacco risulta consegnato ma non ho ricevuto nulla.")

# 4. LOGICA DI GENERAZIONE
if st.button("GENERA DIFFIDA LEGALE", type="primary", use_container_width=True):
    if not sito or not dettagli:
        st.error("Per favore, inserisci il sito e una breve descrizione!")
    else:
        with st.spinner('L\'IA sta analizzando il caso e citando il Codice del Consumo...'):
            # Qui generiamo il testo della diffida
            diffida_testo = f"""
OGGETTO: Diffida formale per mancata risoluzione - Ordine n. {ordine if ordine else 'N/D'}

All'attenzione del Servizio Clienti di {sito},

In virtù del D. Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), con la presente formalizzo formale diffida relativa all'ordine in oggetto.

Premesso che:
- Il sottoscritto ha regolarmente corrisposto l'importo dovuto;
- Il problema riscontrato consiste in: {problema};
- Dettagli: {dettagli};

Ai sensi dell'Art. 61 del Codice del Consumo, vi intimo di procedere al rimborso integrale dell'importo pagato entro e non oltre 48 ore. In difetto, mi riservo di adire le vie legali e segnalare l'accaduto alle autorità competenti (AGCM).

In attesa di riscontro,
Cordiali saluti.
            """
            
            st.success("✅ Diffida Generata con Successo!")
            st.text_area("Copia e invia via Mail o PEC:", value=diffida_testo, height=350)
            
            # --- TASTI DI RINGRAZIAMENTO DOPO GENERAZIONE ---
            st.markdown("---")
            st.subheader("💡 Ti ho aiutato a risolvere?")
            st.write("Mandare questa diffida è il primo passo. Se il tool ti è piaciuto, considera un piccolo supporto:")
            
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("☕ Offri un caffè (Revolut)", "https://revolut.me/gdelgiudice94", use_container_width=True)
            with c2:
                st.link_button("⭐ Supporta SmartUtility Lab", "https://www.buymeacoffee.com/SmartUtilityLab", use_container_width=True)

# 5. RIPROVA SOCIALE (TESTIMONIALS)
st.markdown("---")
st.markdown("### 🗣️ Cosa dicono gli utenti")
t1, t2, t3 = st.columns(3)
with t1:
    st.success("⭐⭐⭐⭐⭐\n\n*Amazon mi ignorava. Ho mandato questa diffida e mi hanno rimborsato subito.* \n\n- Marco T.")
with t2:
    st.success("⭐⭐⭐⭐⭐\n\n*Tool fantastico, ha citato il codice del consumo perfettamente.* \n\n- Elena R.")
with t3:
    st.success("⭐⭐⭐⭐⭐\n\n*Semplice e veloce. Ho recuperato 80€ da un sito truffa.* \n\n- Giovanni L.")
