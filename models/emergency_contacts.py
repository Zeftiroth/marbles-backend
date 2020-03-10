from models.base_model import BaseModel
import peewee as pw
from models.user import Users


class EmergencyContacts(BaseModel):
    user = pw.ForeignKeyField(Users, backref="emergency_contacts")
    name = pw.CharField(null=True)
    contact_no = pw.CharField(null=True)
    email = pw.CharField(null=True)
