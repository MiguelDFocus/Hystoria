AUTHOR = 'Hystoria'
SITENAME = 'Hystoria – Historia por una IA'
SITEURL = ""
DEFAULT_CATEGORY = 'Historia'

PATH = "content"
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'
DATE_FORMATS = {
    'es': '%d/%m/%Y %H:%M',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Disable standalone pages for tags, categories, and authors
DIRECT_TEMPLATES = ['index']
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/hystoria"