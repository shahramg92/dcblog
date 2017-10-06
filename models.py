import datetime
import os

import peewee
from playhouse.db_url import connect

DB = connect(
  os.environ.get(
    'DATABASE_URL',
    'postgres://localhost:5432/blog' #532 is default port for postgres
  )
)

class BaseModel (peewee.Model):
  class Meta:
    database = DB

class BlogPost (BaseModel):
  title = peewee.CharField(max_length=60)
  slug = peewee.CharField(max_length=50, unique=True)
  body = peewee.TextField()
  created = peewee.DateTimeField(
              default=datetime.datetime.utcnow)
