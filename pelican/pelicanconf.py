# -*- coding: utf-8 -*- #
import csv
from os import listdir, scandir

SITENAME = {
    'full': 'Воронежская весенняя математическая школа',
    'short': 'ВВМШ'
}
SITEURL = 'vvmsh.math-vsu.ru'

DESCRIPTION = 'Воронежская весенняя математическая школа «Понтрягинские чтения – XXXIII»'
KEYWORDS = 'Воронежская весенняя математическая школа, ВВМШ'
YEAR = '2022'

THEME = 'theme'

SLUGIFY_SOURCE = 'basename'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

PAGE_ORDER_BY = 'order'

STATIC_PATHS = ['files', 'albums']

PHOTOS = [(x.name, listdir('content/albums/' + x.name))
          for x in scandir('content/albums') if x.is_dir()]

PARTICIPANTS = []
with open('participants.csv', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    PARTICIPANTS = enumerate(tuple(reader), 1)

# Disable generations some files
ARCHIVES_SAVE_AS = None
AUTHORS_SAVE_AS = None
CATEGORIES_SAVE_AS = None
FEED_ALL_ATOM = None
TAGS_SAVE_AS = None
