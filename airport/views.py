from rest_framework import viewsets, mixins

from airport.models import AirplaneType, Airplane, Crew, Country, City, Airport
from airport.serializers import (
    AirplaneTypeSerializer,
    AirplaneSerializer,
    AirplaneDetailSerializer,
    AirplaneListSerializer,
    CrewSerializer,
    CountrySerializer,
    CitySerializer,
    CityListSerializer,
    AirportSerializer,
    AirportDetailSerializer,
    AirportListSerializer
)


class AirplaneTypeViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer


class AirplaneViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Airplane.objects.select_related("airplane_type")

    @staticmethod
    def _params_to_ints(qs):
        """Converts a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        """Retrieve the airplanes with airplane_type filter"""
        airplane_types = self.request.query_params.get("airplane_type")

        queryset = self.queryset

        if airplane_types:
            airplane_types_ids = self._params_to_ints(airplane_types)
            queryset = queryset.filter(airplane_type__id__in=airplane_types_ids)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "list":
            return AirplaneListSerializer

        if self.action == "retrieve":
            return AirplaneDetailSerializer

        return AirplaneSerializer


class CrewViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class CountryViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    queryset = City.objects.select_related("country")

    def get_serializer_class(self):
        if self.action == "list":
            return CityListSerializer

        return CitySerializer


class AirportViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Airport.objects.select_related("closest_big_city")

    @staticmethod
    def _params_to_ints(qs):
        """Converts a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        """Retrieve the airports with closest_big_city filter"""
        closest_big_cities = self.request.query_params.get("closest_big_city")

        queryset = self.queryset

        if closest_big_cities:
            closest_big_cities_ids = self._params_to_ints(closest_big_cities)
            queryset = queryset.filter(closest_big_city__id__in=closest_big_cities_ids)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "list":
            return AirportListSerializer

        if self.action == "retrieve":
            return AirportDetailSerializer

        return AirportSerializer
