from .views import check_user_legacy
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [url(r"^oidc/", include("mozilla_django_oidc.urls"))]
urlpatterns += [url(r"^check-user-legacy/(?P<email>.*\\w+)/$", check_user_legacy, name="check-user-legacy")]
urlpatterns += staticfiles_urlpatterns()
