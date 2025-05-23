from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class DiabetesForm(FlaskForm):
    pregnancies = IntegerField('Number of Pregnancies', 
                              validators=[DataRequired(), NumberRange(min=0, max=20)],
                              default=0)
    
    glucose = FloatField('Glucose Level (mg/dL)', 
                        validators=[DataRequired(), NumberRange(min=70, max=200)],
                        default=120)
    
    blood_pressure = FloatField('Blood Pressure (mm Hg)', 
                              validators=[DataRequired(), NumberRange(min=40, max=140)],
                              default=70)
    
    skin_thickness = FloatField('Skin Thickness (mm)', 
                              validators=[DataRequired(), NumberRange(min=7, max=99)],
                              default=20)
    
    insulin = FloatField('Insulin Level (mu U/ml)', 
                        validators=[DataRequired(), NumberRange(min=15, max=276)],
                        default=80)
    
    bmi = FloatField('BMI', 
                    validators=[DataRequired(), NumberRange(min=18, max=50)],
                    default=25)
    
    diabetes_pedigree = FloatField('Diabetes Pedigree Function', 
                                  validators=[DataRequired(), NumberRange(min=0.08, max=2.42)],
                                  default=0.5)
    
    age = IntegerField('Age', 
                     validators=[DataRequired(), NumberRange(min=21, max=81)],
                     default=30)
    
    submit = SubmitField('Predict')