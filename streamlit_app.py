pip install yfinance
import streamlit as st
import pandas as pd
import numpy as np




st.markdown("Simulador de inversión")
st.markdown("Selecciona uno, dos o tres ETFs para comparar su rendimiento y simular la inversión:")

# Selector de periodos de tiempo
periodos = ['1mo', '3mo', '6mo', '1y', 'ytd', '3y', '5y', '10y']
seleccion_periodo = st.selectbox('Selecciona el periodo de tiempo', periodos)




