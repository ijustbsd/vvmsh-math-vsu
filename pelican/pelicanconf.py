# -*- coding: utf-8 -*- #

SITENAME = {
    'full': 'Воронежская весенняя математическая школа',
    'short': 'ВВМШ'
}
SITEURL = 'vvmsh.math-vsu.ru'

DESCRIPTION = 'Воронежская весенняя математическая школа «Понтрягинские чтения – XXXVI»'
KEYWORDS = 'Воронежская весенняя математическая школа, ВВМШ'
YEAR = '2025'

THEME = 'theme'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["participants_list"]

SLUGIFY_SOURCE = 'basename'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

PAGE_ORDER_BY = 'order'

STATIC_PATHS = ['files']

# Disable generations some files
ARCHIVES_SAVE_AS = None
AUTHORS_SAVE_AS = None
CATEGORIES_SAVE_AS = None
FEED_ALL_ATOM = None
TAGS_SAVE_AS = None
