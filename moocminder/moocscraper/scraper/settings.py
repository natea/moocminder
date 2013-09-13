import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") #Changed in DDS v.0.3

BOT_NAME = 'moocscraper'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'moocscraper.scraper',]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = [
    'dynamic_scraper.pipelines.ValidationPipeline',
    'moocscraper.scraper.pipelines.DjangoWriterPipeline',
]