from django.conf.urls import url

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'cats', views.CatViewSet, base_name='cats')
router.register(r'dogs', views.DogViewSet, base_name='dogs')

urlpatterns = router.urls



# urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^/cats$', views.CatViewSet.as_view(), name='cats'),
# ]

