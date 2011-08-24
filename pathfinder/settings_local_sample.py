import os.path

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "media")

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), "templates"),)

STATIC_ROOT = os.path.join(os.path.dirname(__file__), "static")
