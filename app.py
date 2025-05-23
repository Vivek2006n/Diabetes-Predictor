from flask import Flask, render_template, request, redirect, url_for, flash, session
from forms import DiabetesForm
from model import DiabetesModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'diabetes-predictor-secret-key'

# Initialize the model
diabetes_model = DiabetesModel()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DiabetesForm()
    prediction_result = None

    # Initialize history in session if not present
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST' and form.validate_on_submit():
        # Get form data
        pregnancies = form.pregnancies.data
        glucose = form.glucose.data
        blood_pressure = form.blood_pressure.data
        skin_thickness = form.skin_thickness.data
        insulin = form.insulin.data
        bmi = form.bmi.data
        diabetes_pedigree = form.diabetes_pedigree.data
        age = form.age.data
        
        # Make prediction
        input_data = [
            pregnancies, glucose, blood_pressure, skin_thickness,
            insulin, bmi, diabetes_pedigree, age
        ]
        
        prediction = diabetes_model.predict([input_data])
        prediction_result = 'Positive' if prediction[0] == 1 else 'Negative'

        # Add result to history
        history_entry = {
            'pregnancies': pregnancies,
            'glucose': glucose,
            'blood_pressure': blood_pressure,
            'skin_thickness': skin_thickness,
            'insulin': insulin,
            'bmi': bmi,
            'diabetes_pedigree': diabetes_pedigree,
            'age': age,
            'result': prediction_result
        }
        session['history'].append(history_entry)
        session.modified = True

    # Pass history to template
    history = session.get('history', [])
    return render_template('index.html', form=form, prediction=prediction_result, history=history)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)