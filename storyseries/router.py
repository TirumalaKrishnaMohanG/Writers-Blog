# Headers
from rest_framework import routers
from storyseries.views import StoryseriesViewSet

# Define Route
router = routers.DefaultRouter()
router.register('assignment',StoryseriesViewSet)