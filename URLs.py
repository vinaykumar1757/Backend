from django.urls import include, path
from rest_framework import routers
from faq import views

router = routers.DefaultRouter()
router.register(r'faqs', views.FAQViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
