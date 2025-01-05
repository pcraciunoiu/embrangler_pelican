#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Paul Craciunoiu"
SITENAME = "Life's twists and turns"
SITEURL = "http://embrangler.com"

# TODO: check that this feed domain works for category, etc other feeds
FEED_DOMAIN = "http://feeds.feedburner.com"
FEED_RSS = "all.rss"
FEED_ATOM = "all.atom.xml"
# TODO category feed, tag feed

TIMEZONE = "America/Denver"

DEFAULT_LANG = "en"
LOCALE = ""
DEFAULT_DATE_FORMAT = "%b %d, %Y"
DEFAULT_HOVER_DATE_FORMAT = "%b %d, %Y %I:%M%p"

BLOG_KEYWORDS = "Paul Craciunoiu, software engineer, web developer, entrepreneurship, consulting, pursuit of happiness"
BLOG_DESCRIPTION = (
    "The life blog of Paul Craciunoiu. Consultant, adventurer, traveler, pursuer of happiness."
)

PLUGINS = []

# Article settings
ARTICLE_PATHS = ["posts/"]
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

PAGE_URL = "{slug}/index.html"
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_LANG_URL = "{lang}/{slug}/index.html"
PAGE_LANG_SAVE_AS = "{lang}/{slug}/index.html"


# Blogroll
LINKS = (
    ("@embrangler", "http://twitter.com/embrangler/"),
    ("paul [at] craciunoiu {dot} net", "#"),
    ("github", "http://github.com/pcraciunoiu/"),
    ("about", "/about"),
)

GOOGLE_ANALYTICS = "UA-15382775-1"

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

THEME = "./themes/embrangler/"
MARKUP = "md"
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

STATIC_PATHS = ["static", "favicon.ico"]

# default value is ('index', 'tags', 'categories', 'archives')
DIRECT_TEMPLATES = ("index", "tags", "sitemap")
SITEMAP_SAVE_AS = "sitemap.xml"


# Related posts
PLUGINS.append("plugins.related_posts")

# Temporary fix, see https://github.com/getpelican/pelican/issues/3431
IGNORE_FILES = [".#*"]
