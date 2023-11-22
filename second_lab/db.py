import peewee


db = peewee.SqliteDatabase('users.db')


class User(peewee.Model):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    full_name = peewee.CharField()
    birth_date = peewee.DateField()
    birth_place = peewee.CharField()
    phone_number = peewee.CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([User])

