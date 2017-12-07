from flask_wtf import FlaskForm
from wtforms import BooleanField, HiddenField, PasswordField, StringField
from wtforms.validators import DataRequired, equal_to, StopValidation

__all__ = ["CreateForm", "DeleteForm", "UpdateForm"]


class UpdateForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    superuser = BooleanField("Superuser", default=False)
    password = PasswordField("Password")
    password_confirm = PasswordField("Confirm Password", [equal_to("password")])


class CreateForm(UpdateForm):
    @staticmethod
    def data_required(field):
        if field.data.strip() == "":
            raise StopValidation("This field is required.")

    def validate_password(self, field):
        self.data_required(field)

    def validate_password_confirm(self, field):
        self.data_required(field)


class DeleteForm(FlaskForm):
    name = HiddenField("Name", [DataRequired()])

