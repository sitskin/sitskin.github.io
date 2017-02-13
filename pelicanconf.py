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
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

STATIC_PATHS = ['images',]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
TYPOGRAPHY = True
THEME = "..\pelican-themes\backdrop"

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
        'sitemap',
        'representative_image'
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

MARKUP = ('rst', 'md', )
