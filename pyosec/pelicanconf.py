#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Josh Pyorre'
SITENAME = u'pyosec'
SITEURL = 'https://pyosec.com'
# SITEURL = 'http://localhost:8000'

PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images','presentations','documents','extra']
ARTICLE_EXCLUDES = ['extra']
PLUGIN_PATHS = ['pelican-plugins']
INDEX_SAVE_AS = 'blog_index.html'

# Display posts by date in the URL
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
DISPLAY_CATEGORIES_ON_MENU = False

# RSS:
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
FEED_USE_SUMMARY = False

TIMEZONE = 'America/Los_Angeles'
THEME = 'bootstrap2'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True
# Blogroll
# LINKS = (
         # ('About', 'pages/about'),
#          ('Research & Presentations', 'research-and-presentations'),
#          ('Contact', 'pages/contact'),
         # ('RSS','feeds/all.rss.xml'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/joshpyorre'),
          ('LinkedIn', 'https://www.linkedin.com/in/josh-pyorre-5aa5955/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
