#!/usr/bin/env python3
import os
import tornado.ioloop
import tornado.web
import tornado.log

import tornado.web
from jinja2 import \
  Environment, PackageLoader, select_autoescape
ENV = Environment(
  loader=PackageLoader('blog', 'templates'),
  autoescape=select_autoescape(['html', 'xml'])
)
class TemplateHandler(tornado.web.RequestHandler):
  def render_template (self, tpl, context):
    template = ENV.get_template(tpl)
    self.write(template.render(**context))

class MainHandler(TemplateHandler):
  def get (self):
    posts = BlogPost.select().order_by(BlogPost.created.desc())
    self.render_template("home.html", {'posts': posts})

class PostHandler(TemplateHandler):
  def get (self, slug):
    post = BlogPost.select().\
      where(BlogPost.slug == slug).get()
    self.render_template("post.html", {'post': post})

def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
    (r"/static/(.*)",
      tornado.web.StaticFileHandler, {'path': 'static'}),
  ], autoreload=True)

if __name__ == "__main__":
  tornado.log.enable_pretty_logging()
  app = make_app()
  app.listen(int(os.environ.get('PORT', '8080')))
  tornado.ioloop.IOLoop.current().start()
