from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from articles.models import ArticlePage

class HomePage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ], null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    parent_page_types = ['wagtailcore.Page']  # Ensure it's allowed as the site root
    subpage_types = ['articles.ArticlePage']  # Allow AsrticlePage as a child

    def get_context(self, request):
        context = super().get_context(request)
        context['articles'] = (
            self.get_children().type(ArticlePage).live().public().specific().order_by('-first_published_at')
        )
        return context

    template = "home/home_page.html"  # Specify the template
