import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Imposta il layout a larghezza piena
st.set_page_config(layout="wide")

# Stato persistente per i dati casuali
if "random_data" not in st.session_state:
    st.session_state.random_data = True

# Layout con colonne: slider e controlli nella colonna di destra, grafico a sinistra
col1, col2 = st.columns([3, 1])  # Colonna sinistra piu' larga per il grafico

with col2:  # Controlli nella colonna di destra
    st.header("Parametri della Retta")
    a = st.slider("Coefficiente angolare (a)", -5.0, 5.0, 1.0, 0.1)
    b = st.slider("Intercetta (b)", -10.0, 10.0, 0.0, 0.1)

    st.header("Controllo Dati")
    noise_level = st.slider("Livello di Rumore", 0.0, 5.0, 1.0, 0.1)
    if st.button("Genera Nuovi Dati"):
        st.session_state.random_data = True  # Flag per generare nuovi dati

# Genera o aggiorna i dati casuali con rumore
if st.session_state.random_data:
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    noise = np.random.normal(0, noise_level, x.shape)
    y = 2 * x + 5 + noise  # Retta originale con rumore
    st.session_state.x = x
    st.session_state.y = y
    st.session_state.random_data = False  # Resetta il flag

x = st.session_state.x
y = st.session_state.y

# Calcola la retta approssimante
y_fit = a * x + b

# Calcola l'errore quadratico medio (MSE)
mse = np.mean((y - y_fit) ** 2)

# Creazione del grafico
with col1:
    st.header("Distribuzione Lineare")
    fig, ax = plt.subplots(figsize=(8, 4))  # Ridimensiona la figura
    ax.scatter(x, y, label="Dati con rumore", color="blue", alpha=0.7)
    ax.plot(x, y_fit, label=f"f(x) = {a:.2f} + {b:.2f} * x", color="red", linewidth=2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid()

    # Adattamento al layout di Streamlit
    st.container()
    st.pyplot(fig)

# Mostra la metrica MSE
with col2:
    st.header("Metriche di Fitting")
    st.metric(label="Errore Quadratico Medio (MSE)", value=f"{mse:.3f}")
