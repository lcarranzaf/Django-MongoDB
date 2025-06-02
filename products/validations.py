import unicodedata
from mongoengine import ValidationError

def validate_name(value):
    if not all(char.isalpha() or char.isspace() for char in value):
        raise ValidationError("El nombre solo debe contener letras.")


def validate_positive_float(value):
    if not isinstance(value, (float, int)) or value <= 0:
        raise ValidationError("El precio debe ser un número positivo mayor a 0.")

def validate_positive_int(value):
    if not isinstance(value, int) or value <= 0:
        raise ValidationError("El stock debe ser un entero positivo mayor a 0.")
