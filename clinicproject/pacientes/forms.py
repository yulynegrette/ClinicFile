from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, SelectField, StringField, PasswordField
from wtforms.fields.html5 import DateTimeLocalField, DateField, EmailField, IntegerField
from wtforms import validators

class AgendarCitaForm(FlaskForm):
    selectNombreMedico = SelectField('Seleccionar el Medico: ',
                        choices=[(1, 'new medico 1'),
                                 (2, 'new medico 2')])
    fechaCita = DateField('Consultar disponibilidad', format='%Y-%m-%d')
    terminos = BooleanField("Acepto términos y condiciones")
    confirmar = SubmitField('Confirmar')

class RegistroPacienteForm(FlaskForm):
    nombre = StringField('Nombres y Apellidos')
    telefono = IntegerField('Télefono de contacto')
    tipo_documento = SelectField('Tipo de documento',
                     choices=[(1, 'Cédula de ciudadanía'),
                              (2, 'Cédula extranjera'),
                              (3, 'Pasaporte'),
                              (4, 'Tarjeta de identidad'),
                              (5, 'Registro civil')])
    no_documento = IntegerField('Número de documento')
    fecha_nacimiento = DateField('Fecha de nacimiento',  format='%Y-%m-%d')
    correo = EmailField('Correo electrónico', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Contraseña')
    terminos = BooleanField("Declaro haber leído y aceptado la normativa sobre protección de datos.")
    enviar = SubmitField('Enviar')