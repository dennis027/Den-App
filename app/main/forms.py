from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,BooleanField,PasswordField,
from wtforms.validators import Email, Required

class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Poster review',validators=[Required()])
    submit=SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Your email adress',Validators=[Required(),Email()])
    password= PasswordField('Your password',Validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])    
    submit = SubmitField('Update Profile')
