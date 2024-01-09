import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

# Import del modello
model = pickle.load(open('model.pkl', 'rb'))

# Realizzo applicazione
st.title("CCF Detector - APP")

st.sidebar.header('Input Dettagli Transazione')

# User
user = st.number_input("Id Utente:")
if not user:
    st.warning("Per favore, compila il campo.")
# Card
card = st.number_input("Id Carta:")
if not card:
    st.warning("Per favore, compila il campo.")
# Year
year = st.number_input("Anno:")
if not year:
    st.warning("Per favore, compila il campo.")
# Month
month = st.text_input("Mese:")
if not month:
    st.warning("Per favore, compila il campo.")
# Day
day = st.text_input("Giorno:")
if not day:
    st.warning("Per favore, compila il campo.")
# Amount
amount = st.number_input("Importo:")
if not amount:
    st.warning("Per favore, compila il campo.")
# Use Chip
useChip = st.text_input("Modalita' pagamento:")
if not useChip:
    st.warning("Per favore, compila il campo.")
# Merchant Name
merchantName = st.number_input("Nome venditore:")
if not merchantName:
    st.warning("Per favore, compila il campo.")
# Merchant City
merchantCity = st.text_input("Posizione venditore:")
if not merchantCity:
    st.warning("Per favore, compila il campo.")
# MCC
mcc = st.number_input("Codice categoria venditore:")
if not mcc:
    st.warning("Per favore, compila il campo.")
# Errors
errors = st.text_input("Errori:")
if not errors:
    st.warning("Per favore, compila il campo.")