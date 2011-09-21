from os import path

MEDIA_ROOT = path.join(path.dirname(__file__), "media")

TEMPLATE_DIRS = (path.join(path.dirname(__file__), "templates"),)

STATIC_ROOT = path.join(path.dirname(__file__), "static")
