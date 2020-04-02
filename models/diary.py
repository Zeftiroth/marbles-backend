from models.base_model import BaseModel
import peewee as pw
from models.user import User


class Diary(BaseModel):
    user = pw.ForeignKeyField(User, backref="diaries")
    content = pw.TextField(null=True)
