

















import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image
pickle_in = open("cgpa.pkl","rb")
classifier=pickle.load(pickle_in)
def welcome():
    return "Welcome All"
def predict_note_authentication(cgpa1,cgpa2,cgpa3,math,sem1,sem2,sem3):
    prediction=classifier.predict([[cgpa1,cgpa2,cgpa3,math,sem1,sem2,sem3]])
    print(prediction)
    return prediction
def main():
    st.title("CGPA Predictor")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">CGPA Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    cgpa1 = st.text_input("cgpa1")
    cgpa2 = st.text_input("cgpa2")
    cgpa3 = st.text_input("cgpa3")
    math = st.text_input("math")
    sem1 = st.text_input("sem1")
    sem2 = st.text_input("sem2")
    sem3 = st.text_input("sem3")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(cgpa1,cgpa2,cgpa3,math,sem1,sem2,sem3)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()