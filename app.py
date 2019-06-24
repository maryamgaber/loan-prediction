from flask import Flask
from flask import jsonify,request
import pickle
import Mapping as mp

app = Flask(__name__)
	
@app.route("/predict",methods=['GET'])
def predict():
	gender = mp.transform_gender(request.args.get('gender'))
	married = mp.transform_married(request.args.get('married'))
	dependents = int(request.args.get('dependents'))
	education = mp.transform_education(request.args.get('education'))
	selfemployed = mp.transform_self_emp(request.args.get('selfemployed'))
	applicant_income = int(request.args.get('app_income'))
	co_appllicant_income = int(request.args.get('co_income'))
	loan_amount = int(request.args.get('loan_amount'))
	loan_amt_term = int(request.args.get('loan_amt_term'))
	credit_hist = int(request.args.get('credit_hist'))
	prop_area = mp.transform_prop_area(request.args.get('prop_area'))

	trained_model = pickle.load(open('finalModel', 'rb'))
	result = trained_model.predict_proba([[gender,married,dependents,education,selfemployed,applicant_income
	,co_appllicant_income,loan_amount,loan_amt_term,credit_hist,prop_area]])
	status_false = result[0][0]
	status_true = result[0][1]
	if  status_false> status_true:
		return "The Result of The Prediction: <b>Loan Status for this user is False with Probablity "+str(status_false)+"</b>."
	else:
		return "The Result of The Prediction: <b>Loan Status for this user is True with Probablity "+str(status_true)+"</b>."
	
	
if __name__ == '__main__':
    app.run(port = 9000, debug = True)	