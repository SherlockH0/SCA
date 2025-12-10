from typing import Any

from rest_framework import mixins, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from missions.models import Mission, Target
from missions.serializers import (
    FullMissionSerializer,
    MissionSerializer,
    TargetSerializer,
)


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return FullMissionSerializer
        return super().get_serializer_class()

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if self.get_object().cat:
            return Response(
                {
                    "detail": "You can't delete a mission that is already assigned to a cat"
                },
                status=400,
            )
        return super().destroy(request, *args, **kwargs)


class TargetViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
