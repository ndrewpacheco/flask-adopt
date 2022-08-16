from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import AnyOf, NumberRange, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")
    species = StringField("Species", validators=[
        AnyOf(['dog', 'cat', 'porcupine'])])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Available?")


# Create a form for adding pets. This should use Flask-WTF, and should have the following fields:

# Pet name
# Species
# Photo URL
# Age
# Notes
# This should be at the URL path /add. Add a link to this from the homepage.


validators = [
    AnyOf(['dog', 'cat', 'porcupine'])]
