from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

class HomePage(Page):
    pass


class ArticlePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class BlogIndexPage(Page):
    introduction = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['articles'] = ArticlePage.objects.live().descendant_of(self)
        return context