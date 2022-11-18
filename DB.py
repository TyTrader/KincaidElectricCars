from peewee import *
from os import path

db_connection_path = path.dirname(path.realpath(__file__))

db = SqliteDatabase(path.join(db_connection_path, "DB.db"))


class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


class Cars(Model):
    make = CharField()
    model = CharField()
    yom = CharField()
    power = CharField()
    price = CharField()

    class Meta:
        database = db


class Bikes(Model):
    make = CharField()
    model = CharField()
    yom = CharField()
    power = CharField()
    price = CharField()

    class Meta:
        database = db


class Trucks(Model):
    make = CharField()
    model = CharField()
    yom = CharField()
    power = CharField()
    price = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)
Cars.create_table(fail_silently=True)
Bikes.create_table(fail_silently=True)
Trucks.create_table(fail_silently=True)
