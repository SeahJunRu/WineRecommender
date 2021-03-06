"""wine_recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.urls import include, re_path
from . import views

urlpatterns = [
    # ex: /
    re_path(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    re_path(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    re_path(r'^wine$', views.wine_list, name='wine_list'),
    # ex: /wine/5/
    re_path(r'^wine/(?P<wine_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),
	re_path(r'^wine/(?P<wine_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]
