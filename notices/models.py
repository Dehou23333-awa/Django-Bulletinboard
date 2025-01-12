from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from markdown import markdown
from django.utils.html import mark_safe
from django.urls import reverse

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    rendered_content = models.TextField(blank=True, editable=False)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.rendered_content = mark_safe(markdown(self.content))
        super().save(*args, **kwargs)

    def get_rendered_content(self):
        return self.rendered_content

    def get_absolute_url(self):
        return reverse('notice_detail', args=[self.id])