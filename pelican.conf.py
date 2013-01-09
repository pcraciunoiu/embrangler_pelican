#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Paul Craciunoiu'
SITENAME = 'Disembrangling Programming'
SITEURL = 'http://embrangler.com'

# TODO: check that this feed domain works for category, etc other feeds
FEED_DOMAIN = 'http://feeds.feedburner.com'
FEED_RSS = 'all.rss'
FEED_ATOM = 'all.atom.xml'
# TODO category feed, tag feed

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
LOCALE = ''
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DEFAULT_HOVER_DATE_FORMAT = '%b %d, %Y %I:%M%p'

BLOG_KEYWORDS = 'Paul Craciunoiu, programming, django, python, mozilla, humble bundle, software engineer, entrepreneurship'
BLOG_DESCRIPTION = 'The personal and professional blog of Paul Craciunoiu, general cool web guy and entrepreneur.'

PLUGINS = []

# Article settings
ARTICLE_DIR = 'posts/'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_URL = '{slug}/index.html'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{lang}/{slug}/index.html'
PAGE_LANG_SAVE_AS = '{lang}/{slug}/index.html'


# Blogroll
LINKS =  (('@embrangler', 'http://twitter.com/embrangler/'),
          ('paul [at] craciunoiu {dot} net', '#'),
          ('github', 'http://github.com/pcraciunoiu/'),
          ('about', '/about'))

GOOGLE_ANALYTICS = 'UA-15382775-1'

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

THEME = './themes/embrangler/'
MARKUP = 'md'
MD_EXTENSIONS = ['headerid', 'codehilite']

STATIC_PATHS = ['images', 'files']
FILES_TO_COPY = (
  ('favicon.ico', 'favicon.ico'),
)

# default value is ('index', 'tags', 'categories', 'archives')
DIRECT_TEMPLATES = ('index', 'tags', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'


# Related posts
from pelican.plugins import related_posts
PLUGINS.append(related_posts)
