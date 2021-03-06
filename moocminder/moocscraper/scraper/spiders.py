from dynamic_scraper.spiders.django_spider import DjangoSpider
from moocscraper.models import MOOCsite, Course, CourseItem


class CourseSpider(DjangoSpider):

    name = 'course_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(MOOCsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Course
        self.scraped_obj_item_class = CourseItem
        super(CourseSpider, self).__init__(self, *args, **kwargs)