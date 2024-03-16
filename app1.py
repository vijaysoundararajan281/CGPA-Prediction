import operator
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("cgpa.pkl","rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_cgpa(cgpa1, cgpa2, cgpa3, math, sem1, sem2, sem3):
    prediction = classifier.predict([[cgpa1, cgpa2, cgpa3, math, sem1, sem2, sem3]])
    return prediction

def main():
    
    st.title("CGPA Predictor and Coure Recommendation System")
    menu = ["Home", "CGPA Prediction", "Course Recommendation"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Home":
        st.write("Welcome to the CGPA Predictor and Course Recommender App.")
        st.write("Please choose an option from the sidebar.")

    elif choice == "CGPA Prediction":
        st.subheader("CGPA Prediction")
        cgpa1 = st.text_input("CGPA 1")
        cgpa2 = st.text_input("CGPA 2")
        cgpa3 = st.text_input("CGPA 3")
        math = st.text_input("HSLC Mathematics marks")
        sem1 = st.text_input("Semester 1 Mathematics marks")
        sem2 = st.text_input("Semester 2 Mathematics marks")
        sem3 = st.text_input("Semester 3 Mathematics marks")
        if st.button("Predict"):
            result = predict_cgpa(cgpa1, cgpa2, cgpa3, math, sem1, sem2, sem3)
            st.success("The predicted CGPA is {}".format(result))

    elif choice == "Course Recommendation":
        st.subheader("Course Recommendation")
        arr = [0] * 7
        mark = {}
        var1 = st.number_input("Problem solving and C Programming")
        var2 = st.number_input("Python Programming")
        var3 = st.number_input("Statistical Analysis")
        var4 = st.number_input("Digital Engineering")
        var5 = st.number_input("Foundations of Data Science")
        var6 = st.number_input("Programming Using Java")
        var7 = st.number_input("Data Structures Design")
        var8 = st.number_input("Fundamentals of Artificial Intelligence")
        var9 = st.number_input("Machine Learning - Essentials")
        var10 = st.number_input("Database Design and Management")
        var11 = st.number_input("Networks and Communication")
        vertical1 = var5
        arr[0] = vertical1
        mark["vertical1"] = var5

        vertical2 = (var2 + var8 + var9) / 3
        arr[1] = vertical2
        mark["vertical2"] = vertical2

        vertical3 = var10
        arr[2] = vertical3
        mark["vertical3"] = vertical3

        vertical4 = var11
        arr[3] = vertical4
        mark["vertical4"] = vertical4

        vertical5 = (var1 + var2 + var6 + var7) / 4
        arr[4] = vertical5
        mark["vertical5"] = vertical5

        vertical6 = var3
        arr[5] = vertical6
        mark["vertical6"] = vertical6

        vertical7 = var4
        arr[6] = vertical7
        mark["vertical7"] = vertical7
        sorted_mark = sorted(mark.items(), key=operator.itemgetter(1), reverse=True)
        if st.button("Predict"):
            st.success("Priority order will be :")
            i=1
            for key, value in sorted_mark:
                if key == "vertical1":
                    st.text(". Vertical-1")
                elif key == "vertical2":
                    st.text(". Vertical-2")
                elif key == "vertical3":
                    st.text(". Vertical-3")
                elif key == "vertical4":
                    st.text(". Vertical-4")
                elif key == "vertical5":
                    st.text(". Vertical-5")
                elif key == "vertical6":
                    st.text(". Vertical-6")
                elif key == "vertical7":
                    st.text(". Vertical-7")
        oglist= ["Select one Vertical","Vertical-1","Vertical-2","Vertical-3","Vertical-4","Vertical-5","Vertical-6","Vertical-7"]
        r=st.selectbox("Verticals",oglist)
        if r=="Vertical-1":
            st.write("""
            ```
            Vertical - 1 Data Science
            . Mathematical foundation for Data Science
            . Pattern Recognition
            . Speech Processing and Analytics
            . Web Mining
            . Exploratory Data Analysis and Visualization
            . Predictive Analysis
            . Time Series Analysis and Forecasting
            . Health Care Analytics
            ```
            """)
        if r=="Vertical-2":
            st.write("""
            ```
             Vertical - 2 Artificial Intelligence and Machine Learning
            . Knowledge Engineering
            . Soft Computing
            . Deep Neural Networks
            . Reinforecement Learning
            . Computer Vision
            . Feature Engineering
            . Object Detection & Facial Recognition
            . Text And Visual Analytics
            ```
            """)
        if r=="Vertical-3":
            st.write("""
            ```
             Vertical - 3 Cloud Computing and Data Processing Technologies
            . Foundations of Cloud Computing
            . Data Storage and Management in Cloud
            . Virtualization Techniques
            . Security and Privacy in Cloud
            . Data Analysis in Cloud Computing
            . Edge Computing
            . Cloud Service Management
            . Big Data Integration and Processing
            ```
            """)
        if r=="Vertical-4":
            st.write("""
            ```
             Vertical - 4 Networking and Cyber Security
            . Parallel and Distributing Computing
            . Mobile Computing
            . Wireless Sensor Networks
            . Software Defined Networks
            . Cyber Security
            . Internet Security
            . Ethical Hacking
            . Digital Forensics
            ```
            """)
        if r=="Vertical-5":
            st.write("""
            ```
             Vertical - 5 Full stack Development
            . UI / UX Design
            . Python Web Development
            . App Development
            . JavaScript Frameworks
            . Webservices and API Design
            . SOA and Microservies
            . Cloud Native Applications Development
            . Devops
             ```
            """)
        if r=="Vertical-6":
            st.write("""
            ```
             Vertical - 6 IT and IT Enabled Services(ITeS)
            . Next Generation Networks 
            . Game Development
            . Blockchain Technologies
            . Augmented Reality / Virtual Reality
            . Quantum Computing
            . Graphics Processing Unit
            . Agile Methodologies
            . Software Testing Tools and Techniques
            ```
            """)
        if r=="Vertical-7":
            st.write("""
            ```
             Vertical - 7 Management and Marketing
            . Human Resource Management for Entrepreneurs
            . Project IT Management
            . Behavioural Economics
            . Recommender Systems
            . Industrial Psychology
            . Marketing Research and Marketing Management
            . Introduction to Innovation, IP Management and Entrepreneurship development
            . Computational Finance and Modeling
            ```
            """)




if __name__ == '__main__':
    main()
