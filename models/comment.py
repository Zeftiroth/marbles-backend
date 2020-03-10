from models.base_model import BaseModel
import peewee as pw
from models.user import Users
from models.thread import Threads


class Comments(BaseModel):
    thread = pw.ForeignKeyField(Threads, backref="comments")
    user = pw.ForeignKeyField(Threads, backref="comments")
    text = pw.TextField(null=True)
