import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

label_encoder = LabelEncoder()


def load_model():
    # Carica il modello addestrato con Pickle
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model


# def load_label_encoder():
    # with open('label_encoder.pkl', 'rb') as le_file:
        # label_encoder = pickle.load(le_file)
    # return label_encoder


def load_scaler():
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return scaler

# Funzione per processing dei dati


def prepare_data(df, label_encoder_arg, scaler_arg):
    # Trasforma in valori numerici con LabelEncoder
    df["Merchant City"] = label_encoder_arg.fit_transform(df["Merchant City"])
    df["Use Chip"] = label_encoder_arg.fit_transform(df["Use Chip"])
    df["Errors"] = label_encoder_arg.fit_transform(df["Errors"])
    st.write(df)
    # Applica MinMax Scaler
    to_normalize = df.columns
    df[to_normalize] = scaler_arg.transform(df[to_normalize])

    return df


def main():
    model = load_model()
    # Realizzo applicazione
    st.title("CCF Detector - APP")

    st.sidebar.header('Input Dettagli Transazione')
    # Hour
    hour = st.number_input('Orario:', value=None, placeholder='Orario transazione', step=1)
    if not hour:
        st.warning("Per favore, compila il campo.")
    # Amount
    amount = st.number_input("Importo:", value=None, placeholder='Importo transazione')
    if not amount:
        st.warning("Per favore, compila il campo.")
    # Use Chip
    use_chip = st.selectbox(
       "Seleziona tipologia di pagamento",
       ("Chip Transaction", "Online Transaction", "Swipe Transaction"),
       index=None,
       placeholder="Seleziona tipologia di pagamento...",
    )
    if not use_chip:
        st.warning("Per favore, compila il campo.")
    # Merchant City
    merchant_city = st.text_input("Città del venditore: (se online, digita ONLINE)", value=None,
                                  placeholder='Città del venditore')
    if not merchant_city:
        st.warning("Per favore, compila il campo.")
    # MCC
    mcc = st.number_input("Codice categoria venditore:", value=None, placeholder='Codice categoria venditore', step=1)
    if not mcc:
        st.warning("Per favore, compila il campo.")
    # Errors
    errors = st.selectbox(
       "Seleziona tipologia di errore",
       ("No error", "Bad Pin", "Insufficient Balance", "Technical Glitch", "Bad Card Number", "Bad Expiration",
        "Bad CVV", "Bad Zipcode", "Insufficient Balance,Technical Glitch", "Bad Card Number,Bad CVV",
        "Bad CVV,Insufficient Balance", "Bad Card Number,Insufficient Balance", "Bad PIN,Technical Glitch",
        "Bad PIN,Insufficient Balance", "Bad Card Number, Bad Expiration",
        "Bad Expiration,Bad CVV", "Bad Expiration,Insufficient Balance"),
       index=None,
       placeholder="Select contact method...",
    )
    if not errors:
        st.warning("Per favore, compila il campo.")
    if st.button("Effettua la previsione"):
        # Crea un dataframe con i dati inseriti dall'utente
        user_data = pd.DataFrame({
            'Amount': [amount],
            'Merchant City': [merchant_city],
            'Hour': [hour],
            'MCC': [mcc],
            'Use Chip': [use_chip],
            'Errors': [errors]
        })

        features = ["Amount", "Merchant City", "Hour", "MCC", "Use Chip", "Errors"]
        st.write(user_data[features])
        # Lavorazione dei dati
        # label_encoder = load_label_encoder()
        scaler = load_scaler()
        user_data = prepare_data(user_data, label_encoder, scaler)

        prediction = model.predict(user_data)

        # Visualizza il risultato
        st.write(f"Risultato della previsione: {prediction}")
        prediction_probability = model.predict_proba(user_data)
        st.write(prediction_probability)
        st.write(user_data["Merchant City"])


if __name__ == "__main__":
    main()

    