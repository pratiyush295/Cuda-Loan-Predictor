from flask import Flask,render_template,redirect,request,url_for
import joblib
import urwid


app=Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')


@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=="POST":
        gender=request.form.get('gender')
        married=request.form.get('married')
        dependent=request.form.get('dependent')
        education=request.form.get('education')
        self_employed=request.form.get('self_employed')
        applicant_income=request.form.get('applicant_income')
        coapplicant_income=request.form.get('coapplicant_income')
        loan_amount=request.form.get('loan_amount')
        loan_term=request.form.get('loan_term')
        credit_history=request.form.get('credit_history')
        property_area=request.form.get('property_area')

        if(gender==None or married==None or dependent==None  or education==None or self_employed==None or applicant_income==None or coapplicant_income==None or loan_amount==None or loan_term==None or credit_history==None or property_area==None):
            print(loan_term,credit_history,property_area)
            return render_template('home.html',empty="Empty Field")
        else:

        # since male--->1    female---->0
            if gender=='male':
                gender=1
            if gender=='female':
                gender=0
            if married=='yes':
                married=1
            if married=='no':
                married=0
            if education=='graduate':
                education=1
            if education=='not_graduate':
                education=0
            if self_employed=='yes':
                self_employed=1
            if self_employed=='no':
                self_employed=0
            if property_area=="rural":
                property_area=0
            if property_area=="urban":
                property_area=1
            if property_area=="semiurban":
                property_area=2
            if credit_history=="good":
                credit_history=1
            if credit_history=="bad":
                credit_history=0



            input=[]
        
            input.append(gender)
            input.append(married)
            input.append(int(dependent))
            input.append(education)
            input.append(self_employed)
            input.append(int(applicant_income))
            input.append(int(coapplicant_income))
            input.append(int(loan_amount))
            input.append(int(loan_term))
            input.append(int(credit_history))
            input.append(int(property_area))

            test=[]
            test.append(input)

            print(input)
            model = joblib.load('model_logestic_regressor')
            result = model.predict(test)
            if(result==1):
                message="Loan Sanctioned"
            else:
                message="Loan Not Sanctioned"
            print(message)
            # return redirect(url_for('home'))
            return render_template('home.html',message=message)
        
        
    message=gender
    return render_template('home.html',message=message)



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')