from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, ValidationError
from shorturl.model import Reg


class MainForm(FlaskForm):
    website = StringField('Website', validators=[DataRequired(), URL()])
    slug = StringField('Extension', validators=None)
    submit = SubmitField('Submit', validators=None)

    def validate_slug(self, slug):
        dat = Reg.query.filter_by(slug=slug.data).first()
        if dat:
            raise ValidationError("Extension already taken")
