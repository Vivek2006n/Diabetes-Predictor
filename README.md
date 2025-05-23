# Diabetes Predictor Web Application

A web-based application that predicts diabetes risk based on health metrics input by the user. This project uses Flask for the web framework and scikit-learn for the machine learning model.

## Features

- User-friendly web interface for inputting health data
- Form validation to ensure proper data entry
- Machine learning model to predict diabetes risk
- Responsive design that works on desktop and mobile devices
- About page with project information and limitations

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the source code

2. Navigate to the project directory

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Running the Application

1. From the project directory, run:

```
python app.py
```

2. Open a web browser and go to `http://127.0.0.1:5000/`

3. Fill out the form with your health metrics and click "Predict" to see the results

## Project Structure

- `app.py`: Main Flask application file
- `forms.py`: Form definitions using Flask-WTF
- `model.py`: Machine learning model for diabetes prediction
- `templates/`: HTML templates for the web pages
- `static/`: CSS and other static files
- `diabetes_model.pkl`: Serialized machine learning model (created on first run)
- `scaler.pkl`: Serialized data scaler (created on first run)

## Disclaimer

This application is for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. The predictions made by this application are based on a machine learning model trained on a specific dataset and may not be accurate for all individuals.

## License

This project is licensed under the MIT License - see the LICENSE file for details.