from django.views.generic.base import TemplateView

# from articles.models import Article

# https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/#templateview

class SightingsPageView(TemplateView):

    template_name = "pages/sightings_page.html"

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        # return context
        return