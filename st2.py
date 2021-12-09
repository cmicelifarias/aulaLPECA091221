import streamlit as st
import pandas as pd #manipulação de tabelas
import numpy as np #algebra linear

#sklearn -> sci-kit learn para aprendizado máquina

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris 

st.write("""
Predicao do dataset do Iris

""")

st.sidebar.header("Vamos colocar coisas aqui")

def usuario():
    sepal_length = st.sidebar.slider("Tamanho do sepal", 4,6,8) 
    sepal_width = st.sidebar.slider("Largura do sepal", 4,6,8)
    petal_length = st.sidebar.slider("Tamando da petala", 1,4,8)
    petal_width = st.sidebar.slider("Largura da Petala", 1,4,8)
    data = {"sepal_length":sepal_length,
            "sepal_width":sepal_width,
            "petal_length":petal_length,
            "petal_width":petal_width
    }
    features = pd.DataFrame(data,index=[0])
    return features

df = usuario()

st.subheader("Input do usuario")
st.write(df)

iris = load_iris()
X = iris.data
Y = iris.target

cls = RandomForestClassifier()
cls.fit(X,Y)

predicao = cls.predict(df)
predicao_proba = cls.predict_proba(df)

st.subheader("Classes possiveis")
st.write(iris.target_names)

st.subheader("Predicao")
st.write(iris.target_names[predicao])

st.subheader("Prediction_proba")
st.write(predicao_proba)