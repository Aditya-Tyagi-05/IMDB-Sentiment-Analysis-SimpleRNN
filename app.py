import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.models import load_model
import streamlit as st

model=load_model('model.h5')

word_index=imdb.get_word_index()
reverse_word_index={value: key for key, value in word_index.items()}

def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i-3,'?') for i in encoded_review])

def preprocess_text(text):
    words=text.lower().split()
    encoded_review=[word_index.get(word,2) + 3 for word in words]
    padded_review=sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review 

def predict_sentiment(review):
    preprocessed_input=preprocess_text(review)
    prediction=model.predict(preprocessed_input)
    sentiment='Positive' if prediction[0][0]>0.5 else 'Negative'
    return sentiment, prediction[0][0]

st.title("IMDB Review Sentiment Analysis")
st.write("This web app will predict weather your review sentiment is positive or not")

user_input=st.text_input("Enter review")

if st.button("Predict"):
    sentiment, score=predict_sentiment(user_input)
    if sentiment=='Positive':
        st.success("Positive")
    else:
        st.error("Negative")    