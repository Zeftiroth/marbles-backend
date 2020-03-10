from models.base_model import BaseModel
import peewee as pw
from models.user import Users


class Threads(BaseModel):
    thread = pw.ForeignKeyField(Users, backref="threads")
    template = pw.CharField(null=True)
    content = pw.TextField(null=True)
