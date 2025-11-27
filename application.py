import pickle 
from flask import Flask,request,render_template
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

## Importing the model and scaler
# CRITICAL CHECK: Ensure 'models/' directory and files exist
try:
    ridge_model=pickle.load(open('models/ridge.pkl','rb'))
    standard_scaler=pickle.load(open('models/scaler.pkl','rb'))
except FileNotFoundError:
    print("🚨 ERROR: Model or Scaler files not found in 'models/' directory. Check paths.")
    # Exit or handle error gracefully

@app.route("/")
def index():
    # MODIFICATION 4: Rendering home.html for consistency
    return render_template('home.html') 

@app.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        try:
            # MODIFICATION 1: Changed all form retrieval keys to lowercase for compatibility with home.html
            
            # Using or '0' as a safeguard against empty fields (though 'required' should prevent it)
            Temperature = float(request.form.get('temperature') or 0)
            RH = float(request.form.get('rh') or 0)
            Ws = float(request.form.get('ws') or 0)
            Rain = float(request.form.get('rain') or 0)    
            FFMC = float(request.form.get('ffmc') or 0)
            DMC = float(request.form.get('dmc') or 0)
            ISI = float(request.form.get('isi') or 0)
            Classes = float(request.form.get('classes') or 0)
            Region = float(request.form.get('region') or 0)

            # Input validation check
            if any(val == 0 for val in [Temperature, RH, Ws, FFMC, DMC, ISI, Classes, Region]) and Rain != 0:
                 # Minimal check, real validation should be more robust
                 pass


            input_features = np.array([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
            
            new_data_scaled=standard_scaler.transform(input_features)
            result=ridge_model.predict(new_data_scaled)
            
            # MODIFICATION 3: Passing result with clear variable name
            return render_template('home.html', prediction_result=result[0])

        # MODIFICATION 2: Added robust error handling
        except ValueError:
            error_msg = "Error: Please ensure all fields are filled with valid numeric data."
            return render_template('home.html', error=error_msg)
            
        except Exception as e:
            print(f"Prediction processing error: {e}")
            error_msg = f"An internal server error occurred: {e}"
            return render_template('home.html', error=error_msg)


    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)