from django.conf.urls import url, include
from rest_framework import routers
from views import DeploymentViewSet, TemplateViewSet

router = routers.DefaultRouter()
router.register(r'deployments', DeploymentViewSet)
router.register(r'templates', TemplateViewSet)

urlpatterns = router.urls
