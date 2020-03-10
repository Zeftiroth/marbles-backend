from models.base_model import BaseModel
import peewee as pw
from models.user import User


class EmergencyContact(BaseModel):
    user = pw.ForeignKeyField(User, backref="contacts")
    name = pw.CharField(null=True)
    contact_no = pw.CharField(null=True)
    email = pw.CharField(null=True)
