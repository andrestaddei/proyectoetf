
import streamlit as st
import yfinance as yf
import seaborn as sns


#Titulo
st.markdown("Simulador de instrumentos Allianz Patrimonial")

st.markdown("Seleccionar ETFs")

# Desplegable para elegir el periodo
periodos = ['1mo', '3mo', '6mo', '1y', 'ytd', '3y', '5y', '10y']
seleccion_periodo = st.selectbox('Selecciona el periodo de tiempo', periodos)



