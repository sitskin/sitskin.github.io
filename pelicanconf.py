#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Sam Itskin'
SITENAME = 'The Itskin Blog'
SITESUBTITLE = 'Here I blog about stuff that I find interresting'
SITEURL = 'https://sitskin.github.io'
SITE_DESCRIPTION = 'I\'m a recent graduate of Baylor University in Computer Science.  Although I\'ve just graduated, I\'m passionate about my field.  Living in Austin, Tx means that I\'m in close proximity to a plethera of established and up-and-coming software companies.'
YEAR = date.today().year
EMAIL = 'sitskin@gmail.com'
SIDEBAR_DIGEST = 'I\'m a recent graduate of Baylor University in Computer Science.  Although I\'ve just graduated, I\'m passionate about my field.  Living in Austin, Tx means that I\'m in close proximity to a plethera of established and up-and-coming software companies.'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/sitskin'),
          ('Twitter', 'https://twitter.com/samitskin'),
		  ('Linkedin', 'https://www.linkedin.com/in/sam-itskin-5617195a/'),)

DEFAULT_PAGINATION = 10
#PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

STATIC_PATHS = ['images',]
AVATAR = '../images/meAndLexi.jpg'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
TYPOGRAPHY = True
#THEME = "../pelican-themes/notebook"

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = []

MARKUP = ('rst', 'md', )
