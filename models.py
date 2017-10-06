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

class Author (BaseModel):
  name = peewee.CharField(max_length=60)
  twitter = peewee.CharField(max_length=60)

  def __str__ (self):
    return self.name



class BlogPost (BaseModel):
  author = peewee.ForeignKeyField(Author, null=True)
  title = peewee.CharField(max_length=60)
  slug = peewee.CharField(max_length=50, unique=True)
  body = peewee.TextField()
  created = peewee.DateTimeField(
              default=datetime.datetime.utcnow)

  def __str__ (self):
    return self.title

    # me = Author.create(name='Paul', twitter='pizzapanther')
    # post.author = me
    # post.save()
    # # Reverse Relationships
    # me.blogpost_set.count()
    # # or
    # me.blogpost_set[0]
