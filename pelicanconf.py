AUTHOR = 'Hystoria'
SITENAME = 'Hystoria – Historia por una IA'
SITEURL = ""
DEFAULT_CATEGORY = 'Historia'

PATH = "content"
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'
# Handle both old format (single digit minutes) and new format (double digit)
DEFAULT_DATE_FORMAT = '%d-%m-%Y %H:%M'

# Plugin configuration
PLUGIN_PATHS = ['plugins']
PLUGINS = ['date_normalizer']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Ensure articles are sorted by date in descending order (newest first)
ARTICLE_ORDER_BY = 'date'
DEFAULT_ORPHANS = 0

# Disable standalone pages for tags, categories, and authors
DIRECT_TEMPLATES = ['index']
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/hystoria"