from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy.contrib.djangoitem import DjangoItem


class MOOCsite(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    mooc_site = models.ForeignKey(MOOCsite)
    description = models.TextField(blank=True)
    url = models.URLField()
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title


class CourseItem(DjangoItem):
    django_model = Course