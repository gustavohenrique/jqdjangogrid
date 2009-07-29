from django.db import models

class Bookmark(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = models.URLField(max_length=254)
    category = models.CharField(max_length=100)

    def __unicode__(self):
        return self.site_name

