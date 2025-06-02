from mongoengine import Document, StringField, FloatField, IntField
from .validations import validate_name, validate_positive_float, validate_positive_int

class Product(Document):
    name = StringField(required=True, validation=validate_name)
    description = StringField()
    price = FloatField(required=True, validation=validate_positive_float)
    stock = IntField(required=True, validation=validate_positive_int)

# Create your models here.
