from peewee import *
import datetime

db = SqliteDatabase("database.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    ROLE_USER = 1
    ROLE_MODERATOR = 2
    ROLE_ADMIN = 3
    id = PrimaryKeyField()
    username = CharField()
    password = CharField()
    role = IntegerField(default=ROLE_USER)
    created_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        table_name = "users"

    def signup(self):
        self.save()

    @staticmethod
    def login(username="", password=""):
        user = User.get(User.username == username)
        if user.password == password:
            return user
        return None


class Moderator(User):
    def __init__(self):
        super().__init__()
        self.role = User.ROLE_MODERATOR


class Admin(Moderator):

    def __init__(self):
        super().__init__()
        self.role = User.ROLE_ADMIN


class Comment(BaseModel):
    id = PrimaryKeyField()
    author = ForeignKeyField(User, backref="comments")
    message = CharField()
    timestamp = DateTimeField(datetime.datetime.now())
    parent = ForeignKeyField('self', backref="comments")

    def __init__(self, author=None, message="", parent=None):
        super().__init__()
        self.message = message
        self.author = author
        self.parent = parent

    class Meta:
        table_name = "comments"


db.connect()
if User.table_exists() and not Comment.table_exists():
    db.create_tables([User, Comment])
