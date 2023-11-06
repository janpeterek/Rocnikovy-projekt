from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField

class UploadImageForm(FlaskForm):
    image = FileField('Nahrát obrázek', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Nahrát')
