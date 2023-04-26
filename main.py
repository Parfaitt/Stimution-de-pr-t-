import streamlit as st
import pandas as pd
import pickle
model=pickle.load(open('model.pkl','rb'))

st.write('''
# Application de prédiction de prêt bancaire
Cette Application prédite le statut du crédit  
Auteur: Parfait Tanoh N'goran
''')

st.sidebar.header("les parametres d'entrées")

def user_input():
    Gender=st.sidebar.slider('Genre',0,1,2) 
    Married=st.sidebar.slider('Statut matrimonial',0,1,2)
    Dependents=st.sidebar.slider('Dependents',0,1,2)
    Education=st.sidebar.slider('Education',0,1,2) 
    Self_Employed=st.sidebar.slider('Travailleur indépendant',0,1,2)
    ApplicantIncome=st.sidebar.slider('Revenu demandeur',5.01,10.07,20.7)
    CoapplicantIncome=st.sidebar.slider('Revenu du Codemandeur',0.0,9.33,15.30)
    LoanAmount=st.sidebar.slider('Montant prêt',9.0,650.0,1000.0)
    Loan_Amount_Term=st.sidebar.slider('Durée prêt',12.0,480.0,580.0)
    Credit_History=st.sidebar.slider('Antécedents prêt',0.0,1.0,2.0)
    Property_Area=st.sidebar.slider('Zone',1,2,3)
    
    data={'Gender':Gender,
    'Married':Married,
    'Dependents':Dependents,
    'Education':Education,
    'Self_Employed':Self_Employed,
    'ApplicantIncome':ApplicantIncome,
    'CoapplicantIncome':CoapplicantIncome,
    'LoanAmount':LoanAmount,
    'Loan_Amount_Term':Loan_Amount_Term,
    'Credit_History':Credit_History,
    'Property_Area':Property_Area,
    }
    Credit_parametres=pd.DataFrame(data,index=[0])
    return Credit_parametres
df=user_input()
st.subheader('On veut trouver le statut du prêt')
st.write(df)

prediction = model.predict(df)

st.subheader("Le statut du prêt est:")
st.write(prediction)
st.write(''' 0 signifie prêt Refusé ''')
st.write(''' 1 signifie prêt accepté''')
