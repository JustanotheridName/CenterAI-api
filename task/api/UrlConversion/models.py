from django.db import models

class UrlConversion(models.Model):
    link = models.CharField(max_length=200)
    link_converted = models.CharField(max_length=200)
    ip = models.CharField(max_length=30)
    user_agent = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return self.link