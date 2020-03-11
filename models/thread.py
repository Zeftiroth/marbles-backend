from models.base_model import BaseModel
import peewee as pw
from models.user import User


class Thread(BaseModel):
    user = pw.ForeignKeyField(User, backref="threads")
    template = pw.CharField(null=True)
    content = pw.TextField(null=True)
