from flask import Flask, render_template, request
import pickle
app = Flask(__name__)


# Load the model
model = pickle.load('model.pkl')
print('model loaded!')

# function for the conditions

def process_loan_application(data):
    if (data['Dependents'] >= "3+") or data['ApplicantIncome'] >= 65000 or data['Monthly Debt'] >= 30000 or (data['Home Ownership'] == 'Own Home'):
        return 'Your application for loan has been rejected.'

    else:
        # make prediction using ML model

        prediction = model.predict([data])

        if prediction[0] == 1:
            return 'Congratulations! Your loan application has been approved'

        else:
            return 'Your application for loan is not approved'





@app.route('/', methods=['GET', 'POST'])
def first():

    if request.method == 'POST':
        data = {
            'Gender' : request.form['Gender'],
            'Home Ownership' : request.form['Home Owndership'],
            'Purpose' : request.form['Purpose'],
            'Monthly Debt' : float(request.form['Monthly Debt']),
            'Current Credit Balance' : float(request.form['Current Credit Balance']),
            'Interest Rate' : float(request.form['interest_rate']),
            'Dependents' : str(request.form['Dependents']),
            'Married' : request.form['Married'],
            'Self_Employed' : request.form['Self_Employed'],
            'Applicant Income': float(request.form['ApplicantIncome']),
            'Credit History' : float(request.form['Credit_History']),
            'Country': request.form['country']
        }

        #process the loan application

        result = process_loan_application(data)
        return render_template('index.html', result=result)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)    