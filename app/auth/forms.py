# from flask_wtf import FlaskForm
# from wtforms import StringField,PasswordField,SubmitField
# from wtforms.fields.core import BooleanField
# from wtforms.validators import Required,Email,EqualTo
# from ..models import User
# from wtforms import ValidationError


# class RegistrationForm(FlaskForm):
#     email = StringField('Your Email Adress',validators=[Required(),Email()])
#     username = StringField('enter your username',validators=[Required()])
#     password = StringField('password',validators=[Required(),EqualTo('password_confirm',message="passwords must match")])
#     password_confirm = StringField('password_confirm',validators=[Required()])
#     submit = SubmitField('Sign Up')

#     def validate_email(self,data_field):
#         if User.query.filter_by(email =data_field.data).first():
#             raise ValidationError('there is an account with these email')
#     def validate_username(self,data_field):
#         if User.query.filter_by(username =data_field.data).first():
#             raise ValidationError("this username is taken")     

# class LoginForm(FlaskForm):
#     email = StringField('Your Email Address',validators=[Required(),Email()])
#     password = PasswordField('Password',validators =[Required()])
#     remember = BooleanField('Remember me')
#     submit = SubmitField('Sign In')                  


from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Length,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password2',message = 'Passwords must match')])
    password2 = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')


    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')