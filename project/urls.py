from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve as staticfiles_serve
from django.urls import include, path
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.views.static import serve

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from core.views import server_error

handler500 = server_error

# Standard Wagtail site
urlpatterns = [
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("sitemap.xml", sitemap, name="sitemap"),
    path(
        "robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")
    ),
]

# Allow testing of all styles locally
if settings.DEBUG:
    urlpatterns += [path("demo-styles/", TemplateView.as_view(template_name="demo_styles.html"))]

# Make it easier to see a 404 page under debug
if settings.DEBUG:
    from django.views.defaults import page_not_found

    urlpatterns += [path("404/", page_not_found, {"exception": None})]

# Only enable debug toolbar if it's an installed app
if apps.is_installed("debug_toolbar"):
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]

# Serving static/media under debug
urlpatterns += static(settings.STATIC_URL, never_cache(staticfiles_serve))
urlpatterns += static(settings.MEDIA_URL, never_cache(serve), document_root=settings.MEDIA_ROOT)

# Wagtail catch-all
urlpatterns += [path("", include(wagtail_urls))]
