from rest_framework import routers

from airport.views import (
    AirplaneTypeViewSet,
    AirplaneViewSet,
    CrewViewSet
)


router = routers.DefaultRouter()

router.register("airplane_types", AirplaneTypeViewSet)
router.register("airplanes", AirplaneViewSet)
router.register("crews", CrewViewSet)

urlpatterns = router.urls

app_name = "airport"
