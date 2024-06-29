from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

class ArticlePage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('featured_image'),
    ]

    class Meta:
        verbose_name = "Article Page"
        verbose_name_plural = "Article Pages"
