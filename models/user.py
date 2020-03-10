from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    name = pw.CharField(unique=True)
    email = pw.CharField(unique=True)
    password = pw.CharField(null=True)
    profile_picture = pw.CharField(null=True)
    anonymous = pw.BooleanField(default=True)
    gender = pw.CharField(null=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def validate(self):
        pass
