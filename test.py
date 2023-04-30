import joblib
import pandas as pd
import pickle

df = pd.DataFrame({
    'Gender':1,
    'Married':1,
    'Dependents':2,
    'Education':0,
    'Self_Employed':0,
    'ApplicantIncome':2889,
    'CoapplicantIncome':0.0,
    'LoanAmount':45,
    'Loan_Amount_Term':180,
    'Credit_History':0,
    'Property_Area':1
},index=[0])

# print(df)
arr=[[1,1,2,0,0,2889,0.0,45,180,0,1]]
# model = joblib.load('loan_status_predict')
model = joblib.load('loan_status_predict')

result = model.predict(arr)
print(result[0])

# model = pickle.load(open("model2.pkl", 'rb'))
# print(model.predict(df))