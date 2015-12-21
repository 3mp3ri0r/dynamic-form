""" ``config`` module.
"""

from wheezy.caching.memory import MemoryCache
from wheezy.caching.patterns import Cached
from wheezy.html.ext.template import WidgetExtension
from wheezy.html.utils import html_escape
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader
from wheezy.web.templates import WheezyTemplate


cache = MemoryCache()

options = {}

# HTTPCacheMiddleware
options.update({
    'http_cache': cache
})


# Template Engine
searchpath = ['templates']
engine = Engine(
    loader=FileLoader(searchpath),
    extensions=[
        CoreExtension(),
        WidgetExtension(),
    ])
engine.global_vars.update({
    'h': html_escape,
    's': lambda s: s
})
options.update({
    'render_template': WheezyTemplate(engine)
})
